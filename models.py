from pydantic import BaseModel, Field
from typing import List

class QA(BaseModel):
    q: str = Field(..., description="Quiz question")
    a: str = Field(..., description="Correct answer")

class TopicAnalysis(BaseModel):
    summary: str = Field(..., description="Short summary of the topic")
    keywords: List[str] = Field(..., description="Important terms related to the topic")
    quiz: List[QA] = Field(..., description="Quiz questions and answers")
    difficulty: int = Field(..., description="Difficulty rating from 1–5")

class TopicRequest(BaseModel):
    topic: str = Field(..., description="The topic to analyze")
