from pydantic import BaseModel,Field

from pydantic import BaseModel, Field
from typing import List

class State(BaseModel):
    questions: List[str] = Field(default_factory=list, description="List of questions asked by the AI")
    answers: List[str] = Field(default_factory=list, description="List of answers given by the candidate")
    grade: int = Field(default=0, description="Total grade scored by the candidate")
    summary: str = Field(default="", description="Summary of the whole conversation")
    cheating_penalty: int = Field(default=0, description="Penalty applied due to cheating detection")