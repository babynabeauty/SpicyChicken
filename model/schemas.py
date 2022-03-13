from pydantic import BaseModel
from typing import Optional, List

class SubmitAnswer(BaseModel):
    user_id: str
    question_id: int
    selected: str
class Login(BaseModel):
    user_id: str