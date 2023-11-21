from ._anvil_designer import customerTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class customer(customerTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def link_1_click(self, **event_args):
    open_form('Form1')

  def button_1_click(self, **event_args):
    if 
    self.repeating_panel_1.items = app_tables.users.search(phone=int(self.text_box_1.text))
