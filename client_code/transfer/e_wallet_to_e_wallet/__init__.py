from ._anvil_designer import e_wallet_to_e_walletTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class e_wallet_to_e_wallet(e_wallet_to_e_walletTemplate):
  def __init__(self, user=None, **properties):
    self.user = user
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    self.label_1.text = f"Welcome to Green Gate Financial, {user['username']}"
    user_account_numbers = anvil.server.call('get_user_account_numbers', self.user['username'])
    self.dropdown_account_numbers.items = user_account_numbers

    # Any code you write here will run before the form opens.
