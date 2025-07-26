from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas import ChatRequest, ChatResponse, MessageSchema
from crud import get_or_create_conversation, save_message
from chat import query_llm

app = FastAPI()

def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()

@app.post("/api/chat", response_model=ChatResponse)
def chat(req: ChatRequest, db: Session = Depends(get_db)):
  conv = get_or_create_conversation(db, req.user_id, req.conversation_id)
  save_message(db, conv.id, "user", req.message)
  ai_reply = query_llm(req.message)
  save_message(db, conv.id, "ai", ai_reply)
  return ChatResponse(
    conversation_id=conv.id,
    messages=[
      MessageSchema(sender="user", message=req.message),
      MessageSchema(sender="ai", message=ai_reply),
    ]
  )
