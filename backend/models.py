from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:password@localhost:5432/ai_chat"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False)
Base = declarative_base()

# models.py
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from database import Base
import datetime

class DistributionCenter(Base):
    __tablename__ = 'distribution_centers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    cost = Column(Float)
    category = Column(String)
    name = Column(String)
    brand = Column(String)
    retail_price = Column(Float)
    department = Column(String)
    sku = Column(String)
    distribution_center_id = Column(Integer)

class InventoryItem(Base):
    __tablename__ = 'inventory_items'
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer)
    created_at = Column(DateTime)
    sold_at = Column(DateTime)
    cost = Column(Float)
    product_category = Column(String)
    product_name = Column(String)
    product_brand = Column(String)
    product_retail_price = Column(Float)
    product_department = Column(String)
    product_sku = Column(String)
    product_distribution_center_id = Column(Integer)

class Order(Base):
    __tablename__ = 'orders'
    order_id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    status = Column(String)
    gender = Column(String)
    created_at = Column(DateTime)
    returned_at = Column(DateTime)
    shipped_at = Column(DateTime)
    delivered_at = Column(DateTime)
    num_of_item = Column(Integer)

class OrderItem(Base):
    __tablename__ = 'order_items'
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer)
    user_id = Column(Integer)
    product_id = Column(Integer)
    inventory_item_id = Column(Integer)
    status = Column(String)
    created_at = Column(DateTime)
    shipped_at = Column(DateTime)
    delivered_at = Column(DateTime)
    returned_at = Column(DateTime)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    age = Column(Integer)
    gender = Column(String)
    state = Column(String)
    street_address = Column(String)
    postal_code = Column(String)
    city = Column(String)
    country = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    traffic_source = Column(String)
    created_at = Column(DateTime)

class Conversation(Base):
    __tablename__ = 'conversations'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    started_at = Column(DateTime, default=datetime.datetime.utcnow)

class Message(Base):
    __tablename__ = 'messages'
    id = Column(Integer, primary_key=True)
    conversation_id = Column(Integer, ForeignKey('conversations.id'))
    sender = Column(String)  # 'user' or 'ai'
    message = Column(Text)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
