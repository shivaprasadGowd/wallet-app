from ._anvil_designer import auto_top_upTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from datetime import datetime

class auto_top_up(auto_top_upTemplate):
  def __init__(self, user=None, **properties):
    self.user = user
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    self.label_1.text = f"Welcome to Green Gate Financial, {user['username']}"
    user_account_numbers = anvil.server.call('get_user_account_numbers', self.user['username'])
    self.dropdown_account_numbers.items = user_account_numbers
    self.display()

    # Any code you write here will run before the form opens.

  def display(self, **event_args):
    acc=self.dropdown_account_numbers.selected_value
    user_for_emoney = self.user['username']
    fore_money = anvil.server.call('get_accounts_emoney',acc)
    acc_validate = anvil.server.call('validate_acc_no_to_display_in_transfer',acc)
    self.label_6.text = "$" + str(acc_validate['money_usd'])
    self.label_10.text = "₹ " + str(acc_validate['money_inr'])
    self.label_11.text = "€ " + str(acc_validate['money_euro'])
    self.label_12.text = "₣ " + str(acc_validate['money_swis'])
    e_money_value = str(fore_money['e_money'])
    eb= self.drop_down_2.selected_value
    if e_money_value and e_money_value != 'None' and e_money_value.replace('.', '', 1).isdigit() and eb == '$':
      try:
        e_money_value = float(e_money_value)
        dollar_to_rupee = e_money_value / 80.0  # Set a default value, adjust as needed
        self.label_14.text = str(dollar_to_rupee)
      except ValueError:
        pass
      else:
        pass
    if eb == 'Є':
      try:
        e_money_value = float(e_money_value)
        euro_to_rupee = e_money_value / 90.0
        self.label_14.text = str(euro_to_rupee)  # Convert result to string before assigning to label
      except ValueError:
        pass
    if eb == '₣':
      try:
        e_money_value = float(e_money_value)
        swis_to_rupee = (e_money_value)/95.0
        self.label_14.text = str(swis_to_rupee)
      except ValueError:
        pass
    if eb == '₹':
      self.label_14.text = (e_money_value)

  def drop_down_2_change(self, **event_args):
    acc=self.dropdown_account_numbers.selected_value
    fore_money = anvil.server.call('get_accounts_emoney',acc)
    e_money_value = float(fore_money['e_money'])
    eb= self.drop_down_2.selected_value
    if eb == '$':
      dollar_to_rupee = (e_money_value)/80.0
      self.label_14.text = dollar_to_rupee
    if eb == 'Є':
      euro_to_rupee = (e_money_value)/90.0
      self.label_14.text = euro_to_rupee
    if eb == '₣':
      swis_to_rupee = (e_money_value)/95.0
      self.label_14.text = swis_to_rupee
    if eb == '₹':
      self.label_14.text = (e_money_value)

  def dropdown_account_numbers_change(self, **event_args):
    self.display()

  def link_8_click(self, **event_args):
    open_form('deposit',user= self.user)

  def link_10_click(self, **event_args):
    open_form('withdraw',user= self.user)

  def link_1_click(self, **event_args):
    open_form('customer', user= self.user)

  def link_9_click(self, **event_args):
    open_form('transfer',user= self.user)
