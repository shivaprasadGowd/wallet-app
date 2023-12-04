from ._anvil_designer import transferTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from datetime import datetime


class transfer(transferTemplate):
    def __init__(self, user=None, **properties):
        self.user = user
        self.init_components(**properties)
        self.display()
        
        
    def link_1_click(self, **event_args):
      open_form('customer', user= self.user)

    def button_1_click(self, **event_args):
      current_datetime = datetime.now()
      if self.user is not None:
        wallet3 = anvil.server.call('generate_unique_id', self.user['username'], self.user['phone'])

        if wallet3 is None:
            self.label_4.text = "Error: Wallet is empty"
            return
      selected_symbol = self.drop_down_1.selected_value
      money_value = float(self.text_box_4.text)
      entered_account_number = anvil.server.call('account_no',self.user['username'])
      user_account = anvil.server.call('get_account_data', self.user['username'])

      if selected_symbol == 'Є':
        if float(user_account['money_euro']) > money_value:
            user_account['money_euro'] = str(float(user_account['money_euro']) - money_value)
        else:
            self.label_4.text = "Insufficient funds"
      elif selected_symbol == '$':
        if float(user_account['money_usd']) > money_value:
            user_account['money_usd'] = str(float(user_account['money_usd']) - money_value)
        else:
            self.label_4.text = "Insufficient funds"
      elif selected_symbol == '₣':
        if float(user_account['money_swis']) > money_value:
            user_account['money_swis'] = str(float(user_account['money_swis']) - money_value)
        else:
            self.label_4.text = "Insufficient funds"
      elif selected_symbol == '₹':
        if float(user_account['money_inr']) > money_value:
            user_account['money_inr'] = str(float(user_account['money_inr']) - money_value)
        else:
            self.label_4.text = "Insufficient funds"
      else:
        self.label_4.text = "Error: Invalid currency symbol selected."
        return
      open_form('transfer',user=self.user)
      new_transaction = app_tables.transactions.add_row(
                user=self.user['username'],
                account=entered_account_number['casa'],
                e_wallet=wallet3,
                money=f"{selected_symbol}-{money_value}",
                date=current_datetime
            )


    def display(self, **event_args):
        account_data = anvil.server.call('get_account_data',self.user['username'])
        self.label_6.text = "$" + str(account_data['money_usd'])
        self.label_10.text = "₹ " + str(account_data['money_inr'])
        self.label_11.text = "€ " + str(account_data['money_euro'])
        self.label_12.text = "₣ " + str(account_data['money_swis'])