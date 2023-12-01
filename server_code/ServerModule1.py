import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from datetime import datetime
import anvil.server
from anvil import tables, app
import time
import random
import uuid
# server_module.py

# Function to validate login credentials
@anvil.server.callable
def validate_login(username, password):
    # Query the 'users' table
    user = tables.app_tables.users.get(username=username, password=password)

    if user:
        return user['usertype']
    else:
        return None



@anvil.server.callable
def add_info(email, username, password, pan, address, phone, aadhar):
    user_row = app_tables.users.add_row(
        email=email,
        username=username,
        password=password,
        pan=pan,
        address=address,
        phone=phone,
        aadhar=aadhar,
        usertype='customer',
        confirmed=True,
    )
    return user_row

@anvil.server.callable
def generate_unique_id(username, phone):

    # Combine timestamp and random number to create a unique ID
    unique_id = f"{username}-{phone}"

    return unique_id

@anvil.server.callable
def depo(name,account,e_wallet,money):
  current_datetime = datetime.now()
  user_row = app_tables.transactions.add_row(
    user=name,
    account=account,
    e_wallet=e_wallet,
    money=money,
    date=current_datetime
  )
  return user_row

@anvil.server.callable
def money(type,amount):
  unique=f"{type}-{amount}"
  return unique
  


@anvil.server.callable
def transfer_money(user, amount, currency):
    # Extract numeric part and currency type from the 'amount' string
    amount_numeric, source_currency = extract_numeric_and_currency(amount)

    # Get the exchange rate for the selected currency
    exchange_rate = get_exchange_rate(source_currency)

    # Fetch the current money value from the database
    user_row = app_tables.accounts.get(user=user)
    current_money_str = user_row['money']

    # Convert the amount to rupees based on the selected currency
    amount_in_rupees = convert_to_rupees(amount_numeric, exchange_rate)

    # Update the 'e_money' column by adding the converted amount
    user_row['e_money'] = str(float(user_row['e_money']) + amount_in_rupees)

    # Save the changes to the row
    user_row.update()

def extract_numeric_and_currency(amount_str):
    # Extract numeric part and currency type from the string
    numeric_part = ''.join(char for char in amount_str if char.isdigit() or char == '.')
    currency_type = ''.join(char for char in amount_str if char.isalpha())
    return float(numeric_part) if '.' in numeric_part else int(numeric_part), currency_type

def get_exchange_rate(currency):
    # Implement logic to fetch exchange rate based on the selected currency
    # For simplicity, you can have predefined rates or fetch them from an external API
    exchange_rates = {'dollar': 73.5, 'euro': 87.2, 'rupees': 1.0}
    return exchange_rates.get(currency, 1.0)

def convert_to_rupees(amount, exchange_rate):
    return amount * exchange_rate

