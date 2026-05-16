from sqlalchemy import Column, Integer, String
from models.base import Base

class Stock(Base):
    __tablename__ = "stock"

    id   = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String, nullable=False, unique=True)
    name = Column(String, nullable=False)
    market = Column(String, nullable=True)

    def __repr__(self):
        return f"<Stock code={self.code} name={self.name}>"