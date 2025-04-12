from langgraph.graph import MessagesState
import dotenv
from langchain_core.messages import SystemMessage
from langgraph.graph import END
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from states import State
from prompts import system_msg,cheating_prompt,grading_prompt,initial_message,intro_msg
from utils.stt import transcribe
from utils.tts import audio

dotenv.load_dotenv()
llm = ChatGoogleGenerativeAI(model = 'gemini-1.5-flash')


def summarizer(state: State):
    
    dialogue = ""
    for i, (q, a) in enumerate(zip(state.questions, state.answers), 1):
        dialogue += f"Q{i}: {q}\nA{i}: {a}\n\n"

    
    messages = [
        SystemMessage(
            content="You are an expert interviewer assistant. Your job is to create a concise and coherent summary of the interview so far."
        )
    ]

    
    if state.summary:
        messages.append(AIMessage(content=f"Previous summary: {state.summary}"))

    
    messages.append(
        HumanMessage(content=f"Here are the latest interview questions and answers:\n{dialogue}\n\nPlease generate or improve the summary.")
    )

    
    response = llm.invoke(messages)

    return {"summary": response.content}




def call_model(state: State):
    print("call model")
    last_question = state.questions[-1] if state.questions else "What are your expertise in technology?"
    last_answer = state.answers[-1] if state.answers else "I am very much interested in Machine Learning for how beautiful it is."

    messages = [
        SystemMessage(content=system_msg.format(
            topic="Machine Learning",
            conversation_history=state.summary
        )),
        AIMessage(content=last_question),
        HumanMessage(content=last_answer)
    ]

    question = llm.invoke(messages)
    question_text = question.content if hasattr(question, "content") else str(question)
    print("Generated Question:", question_text)

    
    state.questions.append(question_text)

    
    audio(question_text)  
    #play_audio("output.wav")  

    return {"questions": state.questions}


def human_answer(state: State):
    print("Listening for answer...")

    #record_audio("input.wav")  
    answer = transcribe("input.wav")  

    print("Transcribed Answer:", answer)
    state.answers.append(answer)
    return {"answers": state.answers}


def start_message(state):
    return {
        "intro": (
            "👋 Hello! Welcome to your AI-powered technical interview.\n\n"
            "We'll be diving into a series of questions on the topic of *Machine Learning*.\n"
            "Please try to answer each question in your own words as clearly and concisely as possible.\n\n"
            "Your responses will be evaluated for accuracy, depth, and clarity.\n"
            "You can speak naturally — the system is designed to adapt based on your answers.\n\n"
            "Let's get started. Good luck! 🚀"
        )
    }

def should_continue_interview(state):
    print("Should continue")
    
    if(len(state.questions)>=2):
        return "end" 
    return "continue"


def grading(state):
    print("grading")
    question = state.questions[-1]
    answer = state.answers[-1]
    
    grade = llm.invoke([SystemMessage(content = grading_prompt.format(question = question , answer = answer))]+[f"Question is {question} and the answer is {answer} just return a integer or even float no text anything i just want number "])
    print(grade)
    return {"grade":state.grade+(int)(grade.content)}


def cheatingcheck(state):
    print("cheating check")
    question = state.questions[-1]
    answer = state.answers[-1]

    sys_prompt = SystemMessage(content = cheating_prompt)
    human_msg = HumanMessage(content = answer )
    ai_msg = AIMessage(content = question)
    prompt = [
        sys_prompt,
        ai_msg,
        human_msg
    ]
    result = llm.invoke(prompt)
    print(result)

    return {"cheating_penalty": state.cheating_penalty+(int)(result.content)}






def ending(state: State):
    message = "\n🎉 Thank you for attending the interview!\n"
    message += f"🧠 Final Score: {state.grade}/100\n"
    message += "\n📋 Here's a summary of your responses:\n"

    for i, (q, a) in enumerate(zip(state.questions, state.answers), 1):
        message += f"\nQ{i}: {q}\nA{i}: {a}\n"

    message += "\nBest of luck for your future opportunities! 🚀"
    
    return {"final_message": message}




