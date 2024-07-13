import json
from sqlalchemy import create_engine, Column, String, Float, Date, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()

class Invoice(Base):
    __tablename__ = 'invoices'
    id = Column(Integer, primary_key=True)
    invoice_number = Column(String)
    date = Column(Date)
    total_amount = Column(Float)
    vendor_name = Column(String)

# Connect to the database
engine = create_engine('sqlite:///invoices.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def save_invoice_to_db(invoice_data):

    invoice = Invoice(
        invoice_number=invoice_data['invoice_number'],
        date=datetime.strptime(invoice_data['date'], '%Y-%m-%d').date(),
        total_amount=invoice_data['amount'],
        vendor_name=invoice_data['issuer']
    )
    session.add(invoice)
    session.commit()

def read_invoice_from_json(filepath):
    with open(filepath, 'r') as f:
        invoice_data = json.load(f)
    return invoice_data

# Take JSON file path as input
# filepath = input("Enter the path to the JSON file: ")
filepath = "/path/to/invoice/json/invoice.json"

# Read the JSON file and create invoice_data
invoice_data = read_invoice_from_json(filepath)

# Save the invoice data to the database
save_invoice_to_db(invoice_data[0])
