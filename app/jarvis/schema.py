
from pydantic import BaseModel,Field
from typing import List


class QA(BaseModel):
    question: List[str] = Field(description="The text of the follow-up question asked.")
    answer: List[str] = Field(description="The user's answer to the follow-up question.")

