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
  
exchange_rates = {'usd': 73.5, 'eur': 87.2, 'inr': 1.0}

@anvil.server.callable
def get_exchange_rate(currency):
    # Return the exchange rate for the specified currency
    return exchange_rates.get(currency, 1.0)  # Default to 1.0 if currency not found

@anvil.server.callable
def extract_numeric_and_currency(amount_str):
    # Initialize variables for numeric_part and currency_type
    numeric_part = ''
    currency_type = ''

    # Iterate through characters in amount_str
    for char in amount_str:
        if char.isdigit() or char == '.':
            numeric_part += char
        elif char.isalpha():
            currency_type += char

    # Convert numeric_part to float if it contains a dot, otherwise to int
    try:
        numeric_part = float(numeric_part)
    except ValueError:
        numeric_part = 0  # Default to 0 if conversion fails

    return numeric_part, currency_type

@anvil.server.callable
def transfer_money(user, amount, currency):
    # Extract numeric part and currency type from the 'amount' string
    amount_numeric, source_currency = extract_numeric_and_currency(amount)

    # Get the exchange rate for the selected currency
    exchange_rate = get_exchange_rate(source_currency)

    # Fetch the current money value from the database
    user_row = app_tables.accounts.get(user=user)
    current_money_str = user_row['money']

    # Ensure current_money_str is not None
    current_money_str = current_money_str or '0'

    # Convert the amount to rupees based on the selected currency
    amount_in_rupees = amount_numeric * exchange_rate

    # Ensure 'e_money' is not None
    user_row['e_money'] = user_row['e_money'] or 0

    # Update the 'e_money' column with the converted amount
    user_row['e_money'] += amount_in_rupees

    # Update the 'money' column by subtracting the transferred amount
    user_row['money'] = str(float(current_money_str) - amount_numeric)

    # Save the changes to the row
    user_row.update()

@anvil.server.callable
def add_money(user, amount, currency):
    # Extract numeric part and currency type from the 'amount' string
    amount_numeric, source_currency = extract_numeric_and_currency(amount)

    # Get the exchange rate for the selected currency
    exchange_rate = get_exchange_rate(source_currency)

    # Fetch the current money value from the database
    user_row = app_tables.accounts.get(user=user)

    # Ensure 'e_money' is not None
    user_row['e_money'] = user_row['e_money'] or 0

    # Convert the amount to rupees based on the selected currency
    amount_in_rupees = amount_numeric * exchange_rate

    # Update the 'e_money' column with the converted amount
    user_row['e_money'] += amount_in_rupees

    # Save the changes to the row
    user_row.update()
