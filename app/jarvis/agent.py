from pydantic import Field,BaseModel
from typing import List,Dict
from dotenv import load_dotenv
load_dotenv()


from google.adk.agents import Agent
from jarvis.tools import ask_question


agent = Agent(
    model="gemini-2.0-flash-exp",
    name = 'medical_agent',
    description="A AI Interviewer who asks question to check the knowledge of the user.",
    instruction='''''',
    tools = [ask_question]
)

