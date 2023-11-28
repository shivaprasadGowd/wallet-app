import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from anvil import tables, app
import time
import random

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
    unique_id = generate_unique_id()

    # Add the user information to the users table
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
        id=unique_id
    )

    # Link the user to an account right after signing up
    link_accounts_to_users(account_id='', user_id=user_row['id'])

    return user_row

@anvil.server.callable
def generate_unique_id():
    # Get current timestamp (in seconds)
    timestamp = int(time.time())

    # Generate a random 4-digit number
    random_number = random.randint(1000, 9999)

    # Combine timestamp and random number to create a unique ID
    unique_id = f"{timestamp}-{random_number}"

    return unique_id


@anvil.server.callable
def link_accounts_to_users(account_id, user_id):
    try:
        # Search for an existing account row with the provided account_id
        account_row = app_tables.accounts.get(id=account_id)

        # If the account row doesn't exist, create a new one
        if not account_row:
            account_row = app_tables.accounts.add_row(id=account_id)

        # Update the id column in the accounts table
        account_row['id'] = user_id
        account_row.save()
        
    except Exception as e:
        print(f"Error linking accounts: {e}")


@anvil.server.callable
def link_user_to_transactions(id):
    try:
        # Search for an existing row in the transactions table with the provided user_id
        transaction_row = app_tables.transactions.get(user=id)

        # If the transaction row doesn't exist, create a new one
        if not transaction_row:
            transaction_row = app_tables.transactions.add_row(user=id)

            # Set any initial values for other columns in the transactions table if needed
            transaction_row['initial_balance'] = 0  # Replace with your logic

            # Save the transaction row
            transaction_row.save()

        return transaction_row

    except Exception as e:
        print(f"Error linking user to transactions: {e}")
        return None

@anvil.server.callable
def check_account_for_user(casa):
    try:
        # Check if casa is not None before querying the table
        if casa is not None:
            user = app_tables.users.get(casa=casa)
            return user is not None
        else:
            print("Error: Casa account is None")
            return False
    except anvil.tables.TableError as e:
        # Handle other table errors, if necessary
        print(f"Error: {e}")
        return False

@anvil.server.callable
def check_account_for_user_digital(digital):
    try:
        # Check if casa is not None before querying the table
        if digital is not None:
            user = app_tables.users.get(digital=digital)
            return user is not None
        else:
            # Handle the case where casa is None
            print("Error: digital account is None")
            return False
    except anvil.tables.TableError as e:
        # Handle other table errors, if necessary
        print(f"Error: {e}")
        return False
