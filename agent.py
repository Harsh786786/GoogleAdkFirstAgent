from google.adk.agents import LlmAgent
from .tools import get_device_support
from .tools import analyze_sentiment
from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.getenv('GOOGLE_API_KEY')

#RagAgent
rag_agent = LlmAgent(
    model="gemini-2.0-flash",
    name="rag_agent",
    description = (
    "You are the RAG Agent. Your primary task is to retrieve relevant documentation, reference materials, or information "
    "to address the user's query. Use the retrieval-augmented generation (RAG) process to provide the most accurate and "
    "concise answers. Ensure your responses are clear, professional, and focused on the user's needs, utilizing the tools "
    "and resources available to you."
),
    instruction = (
    "You are the RAG Agent. Your role is to retrieve the most relevant documentation and reference materials based on "
    "the user's query. When a user asks a question, use the RAG corpus to find and deliver the best possible answer. "
    "Ensure your responses are clear, concise, and professional, making complex topics easy to understand. Always prioritize "
    "clarity and precision in your answers. Maintain a professional tone and ensure that the user receives the most accurate "
    "information possible."
),
    tools=[get_device_support],
)


bug_report_agent = LlmAgent(
    model="gemini-2.0-flash",
    name="bug_report_agent",
    description=(
        "You are the Bug Report Agent. Your primary task is to handle user-reported bugs and issues. "
        "You will assess the user's sentiment and provide appropriate responses. If the user seems frustrated, offer to escalate "
        "the issue to a human agent. If the user is satisfied, thank them and close the issue. If the issue involves harmful behavior, "
        "politely reject it."
    ),
    instruction=(
        "You are the Bug Report Agent. Evaluate the user's sentiment and respond accordingly. "
        "If the user mentions hacking, harmful behavior, or inappropriate content, reject the issue and inform them politely. "
        "If the user seems frustrated (negative sentiment), offer them the option to speak with a human agent. "
        "If the user seems satisfied (positive sentiment), thank them and close the issue. "
        "Use sentiment analysis to assess the user's tone and respond appropriately."
    ),
    tools=[analyze_sentiment],  # Include the sentiment analysis function as a tool
)



# Now, create the Root Agent (Supervisor)
root_agent = LlmAgent(
    model="gemini-2.0-flash",
    name="root_agent",
    description="Decides whether to forward user queries to bug reporting or RAG agent.",
    instruction=(
        "You are the root agent. "
        "If the user question is about a BUG or PROBLEM, forward it to the Bug Reporting Agent. "
        "If it is about DOCUMENTATION, REFERENCE, or INFORMATION, forward it to the RAG Agent. "
        "Choose the correct agent wisely based on the user's query."
    ),
    sub_agents=[rag_agent,bug_report_agent],
)





