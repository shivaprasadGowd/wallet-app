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


  def link_8_click(self, **event_args):
    open_form('deposit',user= self.user)

  def link_10_click(self, **event_args):
    open_form('withdraw',user= self.user)

  def link_1_click(self, **event_args):
    open_form('customer', user= self.user)

  def link_9_click(self, **event_args):
    open_form('transfer',user= self.user)

  def button_1_click(self, **event_args):
    self.button_1.visible = False
    self.button_2.visible = True
