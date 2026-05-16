from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base

class Transaction(Base):
    __tablename__ = "transaction"

    id               = Column(Integer, primary_key=True, autoincrement=True)
    stock_id         = Column(Integer, ForeignKey("stock.id"), nullable=False)
    transaction_type = Column(String, nullable=False)
    quantity         = Column(Integer, nullable=False)
    price            = Column(Float, nullable=False)
    amount           = Column(Integer, nullable=True)
    account_type     = Column(String, nullable=True)
    commission       = Column(Float, nullable=True)
    date             = Column(Date, nullable=False)

    stock = relationship("Stock", backref="transactions")

    def __repr__(self):
        return f"<Transaction {self.transaction_type} {self.quantity}株 @{self.price}>"