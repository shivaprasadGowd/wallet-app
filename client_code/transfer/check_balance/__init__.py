from ._anvil_designer import check_balanceTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class check_balance(check_balanceTemplate):
  def __init__(self, user=None, **properties):
    self.user = user
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    self.label_1.text = f"Welcome to Green Gate Financial, {user['username']}"
    user_account_numbers = anvil.server.call('get_user_account_numbers', self.user['username'])
    self.dropdown_account_numbers.items = user_account_numbers

    # Any code you write here will run before the form opens.
