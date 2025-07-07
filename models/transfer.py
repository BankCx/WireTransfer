from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

class WireTransfer:
    __tablename__ = 'wire_transfers'

    id = Column(Integer, primary_key=True)
    
    source_account = Column(String(50))
    destination_account = Column(String(50))
    amount = Column(Float)
    currency = Column(String(3))
    status = Column(String(20))
    created_at = Column(DateTime, default=datetime.utcnow)
    
    user_id = Column(Integer, ForeignKey('users.id'))
    
    transactions = relationship("Transaction", backref="wire_transfer")

    def __init__(self, source_account, destination_account, amount, currency, user_id):
        self.source_account = source_account
        self.destination_account = destination_account
        self.amount = amount
        self.currency = currency
        self.user_id = user_id
        self.status = 'PENDING'

    def update_status(self, status):
        self.status = status

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def to_dict(self):
        return {
            'id': self.id,
            'source_account': self.source_account,
            'destination_account': self.destination_account,
            'amount': self.amount,
            'currency': self.currency,
            'status': self.status,
            'created_at': self.created_at.isoformat(),
            'user_id': self.user_id
        }

class Transaction:
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True)
    
    amount = Column(Float)
    transaction_type = Column(String(50))
    created_at = Column(DateTime, default=datetime.utcnow)
    
    wire_transfer_id = Column(Integer, ForeignKey('wire_transfers.id'))

    def __init__(self, amount, transaction_type, wire_transfer_id):
        self.amount = amount
        self.transaction_type = transaction_type
        self.wire_transfer_id = wire_transfer_id

    def to_dict(self):
        return {
            'id': self.id,
            'amount': self.amount,
            'transaction_type': self.transaction_type,
            'created_at': self.created_at.isoformat(),
            'wire_transfer_id': self.wire_transfer_id
        } 