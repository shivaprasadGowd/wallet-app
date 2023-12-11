from ._anvil_designer import transaction_historyTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class transaction_history(transaction_historyTemplate):
  def __init__(self, user=None, **properties):
    self.user = user
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    self.label_1.text = f"Welcome to Green Gate Financial, {user['username']}"
    user_account_numbers = anvil.server.call('get_user_account_numbers', self.user['username'])
    self.dropdown_account_numbers.items = user_account_numbers

    # Any code you write here will run before the form opens.

  def link_8_click(self, **event_args):
      open_form('deposit',user= self.user)
  
  def link_10_click(self, **event_args):
      open_form('withdraw',user= self.user)

  def link_1_click(self, **event_args):
      open_form('customer', user= self.user)
