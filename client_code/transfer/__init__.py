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
        self.label_1.text = f"Welcome to Green Gate Financial, {user['username']}"
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
      user_currency = anvil.server.call('get_account_data', self.user['username'])
      conversion_rate_usd_to_inr = 80.0
      conversion_rate_swis_to_inr = 95.0
      conversion_rate_euro_to_inr = 90.0
      

      if selected_symbol == 'Є':
        if float(user_currency['money_euro']) > money_value:
            user_currency['money_euro'] = str(float(user_currency['money_euro']) - money_value)
            money_inr_equivalent = money_value * conversion_rate_euro_to_inr
            user_currency['e_money'] = str(float(user_currency['e_money'] or 0) + money_inr_equivalent)
        else:
            self.label_4.text = "Insufficient funds"
      elif selected_symbol == '$':
        if float(user_currency['money_usd']) > money_value:
            user_currency['money_usd'] = str(float(user_currency['money_usd']) - money_value)
            money_inr_equivalent = money_value * conversion_rate_usd_to_inr
            user_currency['e_money'] = str(float(user_currency['e_money'] or 0) + money_inr_equivalent)
        else:
            self.label_4.text = "Insufficient funds"
      elif selected_symbol == '₣':
        if float(user_currency['money_swis']) > money_value:
            user_currency['money_swis'] = str(float(user_currency['money_swis']) - money_value)
            money_inr_equivalent = money_value * conversion_rate_swis_to_inr
            user_currency['e_money'] = str(float(user_currency['e_money'] or 0) + money_inr_equivalent)
        else:
            self.label_4.text = "Insufficient funds"
      elif selected_symbol == '₹':
        if float(user_currency['money_inr']) > money_value:
            user_currency['money_inr'] = str(float(user_currency['money_inr']) - money_value)
            money_inr_equivalent = money_value * 1
            user_currency['e_money'] = str(float(user_currency['e_money'] or 0) + money_inr_equivalent)
        else:
            self.label_4.text = "Insufficient funds"
      else:
        self.label_4.text = "Error: Invalid currency symbol selected."
        return
      
      new_transaction = app_tables.transactions.add_row(
                user=self.user['username'],
                account=int(entered_account_number,
                e_wallet=wallet3,
                money=f"{selected_symbol}-{money_value}",
                date=current_datetime
            )
      
      open_form('transfer',user=self.user)

    def display(self, **event_args):
        user_currency = anvil.server.call('get_account_data', self.user['username'])
        account_data = anvil.server.call('get_account_data',self.user['username'])
        self.label_6.text = "$" + str(account_data['money_usd'])
        self.label_10.text = "₹ " + str(account_data['money_inr'])
        self.label_11.text = "€ " + str(account_data['money_euro'])
        self.label_12.text = "₣ " + str(account_data['money_swis'])
        eb= self.drop_down_2.selected_value
        if eb == '$':
          dollar_to_rupee = float(user_currency['e_money'])/80
          self.label_14.text = dollar_to_rupee
        if eb == 'Є':
          euro_to_rupee = float(user_currency['e_money'])/90
          self.label_14.text = euro_to_rupee
        if eb == '₣':
          swis_to_rupee = float(user_currency['e_money'])/95
          self.label_14.text = swis_to_rupee

        if eb == '₹':
          self.label_14.text = user_currency['e_money']

    def drop_down_2_change(self, **event_args):
      user_currency = anvil.server.call('get_account_data', self.user['username'])
      eb= self.drop_down_2.selected_value
      if eb == '$':
          dollar_to_rupee = float(user_currency['e_money'])/80
          self.label_14.text = dollar_to_rupee
      if eb == 'Є':
          euro_to_rupee = float(user_currency['e_money'])/90
          self.label_14.text = euro_to_rupee
      if eb == '₣':
          swis_to_rupee = float(user_currency['e_money'])/95
          self.label_14.text = swis_to_rupee

      if eb == '₹':
          self.label_14.text = user_currency['e_money']
        
        