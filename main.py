from fastapi import FastAPI
from pydantic import BaseModel
import csv
import random

app = FastAPI()

# Define the Customer model
class Customer(BaseModel):
    customer_id: int
    first_name: str
    last_name: str
    happiness: int

# Read customers from CSV file
customers = []
with open('names.csv', mode='r', encoding='utf-8-sig') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        customers.append(row)

@app.get("/customerFeedback", response_model=list[Customer])
async def get_customers():
    # Select 10 random customers
    selected_customers = random.sample(customers, 10)
    
    # Add a random happiness score to each selected customer
    for customer in selected_customers:
        customer['happiness'] = random.randint(0, 100)

    # Convert customer dictionaries to Customer model objects
    customer_objects = [Customer(**customer) for customer in selected_customers]
    
    return customer_objects
