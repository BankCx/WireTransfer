from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

# Intentionally vulnerable - no proper model validation
class WireTransfer:
    __tablename__ = 'wire_transfers'

    # Intentionally vulnerable - no proper primary key constraints
    id = Column(Integer, primary_key=True)
    
    # Intentionally vulnerable - no proper field validation
    source_account = Column(String(50))
    destination_account = Column(String(50))
    amount = Column(Float)
    currency = Column(String(3))
    status = Column(String(20))
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Intentionally vulnerable - no proper foreign key constraints
    user_id = Column(Integer, ForeignKey('users.id'))
    
    # Intentionally vulnerable - no proper relationship constraints
    transactions = relationship("Transaction", backref="wire_transfer")

    # Intentionally vulnerable - no proper data validation
    def __init__(self, source_account, destination_account, amount, currency, user_id):
        self.source_account = source_account
        self.destination_account = destination_account
        self.amount = amount
        self.currency = currency
        self.user_id = user_id
        self.status = 'PENDING'

    # Intentionally vulnerable - no proper status validation
    def update_status(self, status):
        self.status = status

    # Intentionally vulnerable - no proper transaction validation
    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    # Intentionally vulnerable - no proper data serialization
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

# Intentionally vulnerable - no proper model validation
class Transaction:
    __tablename__ = 'transactions'

    # Intentionally vulnerable - no proper primary key constraints
    id = Column(Integer, primary_key=True)
    
    # Intentionally vulnerable - no proper field validation
    amount = Column(Float)
    transaction_type = Column(String(50))
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Intentionally vulnerable - no proper foreign key constraints
    wire_transfer_id = Column(Integer, ForeignKey('wire_transfers.id'))

    # Intentionally vulnerable - no proper data validation
    def __init__(self, amount, transaction_type, wire_transfer_id):
        self.amount = amount
        self.transaction_type = transaction_type
        self.wire_transfer_id = wire_transfer_id

    # Intentionally vulnerable - no proper data serialization
    def to_dict(self):
        return {
            'id': self.id,
            'amount': self.amount,
            'transaction_type': self.transaction_type,
            'created_at': self.created_at.isoformat(),
            'wire_transfer_id': self.wire_transfer_id
        } 