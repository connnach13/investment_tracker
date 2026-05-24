from models.base import Base, engine
from models.stock import Stock
from models.transaction import Transaction
from services.csv_importer import import_csv

def initialize_db():
    Base.metadata.create_all(engine)
    print("DBを初期化しました")

if __name__ == "__main__":
    initialize_db()
    import_csv("SaveFile_000001_000067.csv")