from pydantic import BaseModel
from typinf import Optional, List

class ChatRequest(BaseModel):
  user_id: int
  message: str
  conversation_id: Optional[int] = None

class MessageSchema(BaseModel):
  sender: str
  message: str

class ChatResponse(BaseModel):
  coversation_id: int
  message: List[MessageSchema]
  
