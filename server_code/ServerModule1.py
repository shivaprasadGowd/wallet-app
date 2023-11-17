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
def add_info(username, password, usertype,pan,address):
  app_tables.users.add_row(
    username=username, 
    password=password,
    usertype=usertype,
    pan=pan,
    address=address,
  )
