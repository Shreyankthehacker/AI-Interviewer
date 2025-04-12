from langgraph.graph import StateGraph, END
from nodes import start_message,call_model,summarizer,grading,cheatingcheck,ending,human_answer,should_continue_interview
from states import State

builder = StateGraph(State)

builder.add_node("start_message", start_message)
builder.add_node("call_model", call_model)
builder.add_node("summarizer", summarizer)
builder.add_node("grading", grading)
builder.add_node("cheatingcheck", cheatingcheck)
builder.add_node("ending", ending)
builder.add_node(human_answer)


builder.set_entry_point("start_message")


builder.add_edge("start_message", "call_model")
builder.add_edge("call_model","human_answer")
builder.add_edge("human_answer", "summarizer")
builder.add_edge("human_answer", "grading")
builder.add_edge("human_answer", "cheatingcheck")


builder.add_conditional_edges(
    "human_answer",
    should_continue_interview,
    {
        "continue": "call_model",
        "end": "ending"
    }
)


builder.add_edge("ending", END)

graph = builder.compile()

summary = '''The interview covered key topics in machine learning, including supervised vs. unsupervised learning and decision tree algorithms. The candidate demonstrated a solid understanding of the differences between labeled and unlabeled data, as well as appropriate examples for each learning type. They also explained the decision tree mechanism well, mentioning feature splits and criteria like information gain and Gini impurity. However, their explanation could have been improved by discussing pruning methods in more detail.'''
state = State(questions=[], answers=[], grade=0, summary=summary,cheating_penalty=0)

