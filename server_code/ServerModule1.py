import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from anvil import tables, app

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
def add_info(email,username, password,pan,address,phone,aadhar):
  app_tables.users.add_row(
    email=email,
    username=username, 
    password=password,
    pan=pan,
    address=address,
    phone= phone,
    aadhar=aadhar,
    usertype='customer',
    confirmed=True
  )


@anvil.server.callable
def check_account_for_user(casa):
    try:
        # Check if casa is not None before querying the table
        if casa is not None:
            user = app_tables.users.get(casa=casa)
            return user is not None
        else:
            # Handle the case where casa is None
            print("Error: Casa account is None")
            return False
    except anvil.tables.TableError as e:
        # Handle other table errors, if necessary
        print(f"Error: {e}")
        return False
