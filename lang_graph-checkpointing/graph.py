from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph.message import add_messages
from langchain.chat_models import init_chat_model
from langgraph.graph import StateGraph, START, END

llm = init_chat_model(model_provider="openai", model="gpt-4.1")

class State(TypedDict):
    messages: Annotated[list, add_messages]


def chatbot(state: State):
    messages = state.get("messages")
    response = llm.invoke(messages)
    return {"messages": [response]}

graph_builder = StateGraph(State)

graph_builder.add_node("chatbot", chatbot)

graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", END)

#without any memory
graph = graph_builder.compile()

#Creates a new graph with given checkpointer
def create_chat_graph(checkpointer):
    return graph_builder.compile(checkpointer=checkpointer)