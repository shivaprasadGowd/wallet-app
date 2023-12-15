from ._anvil_designer import user_supportTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class user_support(user_supportTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens
table_data = app_tables.table_1.search()

# Bind the data to the repeating panel
self.repeating_panel_1.items = table_data
