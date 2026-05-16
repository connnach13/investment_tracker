from models.base import Base, engine
from models.stock import Stock
from models.transaction import Transaction

def initialize_db():
    Base.metadata.create_all(engine)
    print("DBを初期化しました")

if __name__ == "__main__":
    initialize_db()