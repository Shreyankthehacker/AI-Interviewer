import google.generativeai as genai
from jarvis.schema import QA


model = genai.GenerativeModel("gemini-2.0-flash-exp")
from schema import QA
from google.adk.tools.tool_context import ToolContext

async def ask_question(tool_context: ToolContext):
    
    # here we just need to yk get the questios from llm based on the topic 

    topic = tool_context.state['topic']
    state: QA = tool_context.state['state']

    llm_prompt = '''''' # here we have to pass the list of questions and also the answers given previously using state 

    question = model.generate_content(llm_prompt)
    state.question.append(question)
    tool_context.state['state'] = state


    return {"question_to_be_asked": question}


