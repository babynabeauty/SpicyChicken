from pydantic import BaseModel
from typing import Optional, List

class SubmitAnswer(BaseModel):
    user_id: str
    question_id: int
    selected: str

class Login(BaseModel):
    user_id: str
    user_name: str
    avatar: str
    
class Login2(BaseModel):
    user_name: str
    user_psw:str
    avatar: str