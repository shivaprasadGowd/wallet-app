from ._anvil_designer import transferTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class transfer(transferTemplate):
    def __init__(self, user=None, **properties):
        self.user = user
        self.init_components(**properties)
        self.display_balance() 

    def link_1_click(self, **event_args):
      open_form('customer', user= self)

    def display_balance(self, user_casa):
        user_row = app_tables.accounts.get(casa=user_casa)
        self.label_6.text = f"USD Balance: {user_row['money_usd']}"
        self.label_10.text = f"Euro Balance: {user_row['money_euro']}"
        self.label_11.text = f"INR Balance: {user_row['money_inr']}"
        self.label_12.text = f"Swiss Franc Balance: {user_row['money_swiss']}"
