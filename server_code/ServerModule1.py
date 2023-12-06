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
    unique_id = f"{username}-{phone}"

    return unique_id
  

def convert_to_inr(amount, currency):
    conversion_rates = {
        'usd': 75.0,   # Replace with actual rates
        'euro': 85.0,  # Replace with actual rates
        'inr': 1.0,    # 1:1 conversion for INR
        'swiss': 80.0  # Replace with actual rates
        # Add more currencies as needed
    }

    return amount * conversion_rates[currency.lower()]

# Define a function to transfer money to e_wallet
@anvil.server.callable
def transfer_money(username, amount, selected_currency):
    # Get the current user's data from the accounts table
    account_row = app_tables.accounts.get(user=username)

    # Convert the entered amount to INR
    amount_inr = convert_to_inr(float(amount), selected_currency)

    # Update the e_wallet column with the transferred amount
    account_row['e_wallet'] += amount_inr

    # Update the specific currency column with the transferred amount
    currency_column = f'money_{selected_currency.lower()}'
    account_row[currency_column] -= float(amount)

    # Save the changes to the accounts table
    account_row.save()

    # Return a success message or any relevant information
    return f"Transferred {amount} {selected_currency} to e_wallet for {user_id}"

@anvil.server.callable
def get_currency_data(name):
    currency_table = app_tables.currencies.get(user=name)
    return currency_table

@anvil.server.callable
def get_account_no(name):
    accounts_tab = app_tables.accounts.get(user=name)
    return accounts_tab
#
@anvil.server.callable
def update_all_rows(user, e_wallet, e_money_value):
    # Fetch all rows with the same user and e_wallet
    matching_rows = app_tables.your_table_name.search(user=user, e_wallet=e_wallet)

    # Update 'e_money' column in all matching rows
    for row in matching_rows:
        row['e_money'] = e_money_value

    # Update other columns if needed
    # row['other_column'] = some_value

    # Save changes to the table
    app_tables.your_table_name.update(matching_rows)



