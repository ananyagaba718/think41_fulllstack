import pandas as pd
from sqlalchemy.orm import Session
from database import engine, SessionLocal
from models import *
Base.metadata.create_all(bind=engine)

def load_csv_data():
    db = SessionLocal()
    for file, model in [
        ("distribution_centers.csv", DistributionCenter),
        ("products.csv", Product),
        ("inventory_items.csv", InventoryItem),
        ("orders.csv", Order),
        ("order_items.csv", OrderItem),
        ("users.csv", User),
    ]:
        df = pd.read_csv(file)
        for row in df.to_dict(orient="records"):
            db.add(model(**row))
        db.commit()
    db.close()
  
if__name__== "__main__":
  load_csv_data()
