import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
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
  
import anvil.server

@anvil.server.callable
def get_money_values():
    # Access the "accounts" Data Table
    accounts_table = app_tables.accounts

    # Fetch all rows from the "money" column
    money_values = [row['money'] for row in accounts_table.search()]

    return money_values