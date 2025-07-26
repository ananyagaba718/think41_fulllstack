from sqlalchemy.orm import Session
from models import Conversation, Message
def get_or_create_conversation(db: Session, user_id: int, conversation_id:int = None):
  if conversation_id:
    return db.query(Conversation).filter(Conversation.id == conversation_id).first()
  conv = Conversation(user_id=user_id)
  db.add(conv)
  db.commit()
  db.refresh(conv)
  return conv

def save_message(db: Session, conv_id:int, sender: str, msg: str):
  message = Message(conversation_id=conv_id, sender=sender, message=msg)
  db.add(message)
  db.commit()
