import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from anvil import tables, app
import time
import random
import uuid


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

    # Link the user to an account right after signing up
    link_accounts_to_users(account_id='', user_id=user_row['id'])
    link_accounts_to_transactions(account_id='', user_id=user_row['id'])
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
def link_accounts_to_transactions(account_id, user_id):
    try:
        # Search for an existing account row with the provided account_id
        account_row = app_tables.transactions.get(id=account_id)

        # If the account row doesn't exist, create a new one
        if not account_row:
            account_row = app_tables.transactions.add_row(id=account_id)

        # Update the id column in the accounts table
        account_row['id'] = user_id
        account_row.save()
        
    except Exception as e:
        print(f"Error linking accounts: {e}")


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


@anvil.server.callable
def link_user_to_casa(user_id, casa_number):
    try:
        # Search for an existing row in the accounts table with the provided user_id and casa_number
        casa_row = app_tables.accounts.get(user=user_id, casa=casa_number)

        # If the casa row doesn't exist, create a new one
        if not casa_row:
            casa_row = app_tables.accounts.add_row(user=user_id, casa=casa_number)

        # Save the casa row
        casa_row.save()

        return casa_row

    except Exception as e:
        print(f"Error linking user to casa: {e}")
        return None

@anvil.server.callable
def map_casa_to_digital_wallet(user_id, casa_number):

    app_tables.transactions.add_column('user', tables.LinkType())
    try:
        # Search for an existing digital wallet row with the provided user_id
        digital_row = app_tables.transactions.get(user=user_id)

        # If the digital wallet row doesn't exist, create a new one
        if not digital_row:
            # Generate a unique e_wallet based on the user_id
            unique_e_wallet = f"UniqueDigitalWallet-{user_id}"

            # Add a new row to the transactions table
            digital_row = app_tables.transactions.add_row(user=user_id, digital=unique_e_wallet)

            # Map the Casa account to the digital wallet
            digital_row['casa'] = casa_number

            # Save the digital row
            digital_row.save()

            return unique_e_wallet  # Return the generated e_wallet

    except Exception as e:
        print(f"Error mapping casa to digital wallet: {e}")
    
    return None
@anvil.server.callable
def generate_unique_id1(user_id):
    # Check if the user already has a unique ID generated
    user_row = app_tables.user_unique_ids.get(user=user_id)

    if user_row is not None:
        # If the user already has a unique ID, return that ID
        return user_row['unique_id']
    else:
        # Generate a random 4-digit number
        random_number = random.randint(1000, 9999)

        # Generate another unique ID using UUID (Universal Unique Identifier)
        unique_id = str(uuid.uuid4())

        # Combine the random number and the additional unique ID to create a unique ID
        combined_id = f"{random_number}-{unique_id}"

        # Save the generated unique ID for the user in the database
        app_tables.user_unique_ids.add_row(user=user_id, unique_id=combined_id)

        return combined_id




