from ._anvil_designer import adminTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables



class admin(adminTemplate):
  def __init__(self, user=None, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.label_1.text = f"Welcome to Green Gate Financial, {user['username']}"
    self.repeating_panel_1.visible = False

  
  def link_1_click(self, **event_args):
    open_form('Home')

  def button_1_click(self, **event_args):
    self.repeating_panel_1.visible = not self.repeating_panel_1.visible

    customer_type_filter = []

    for user in app_tables.users.search():
        if user['usertype'] == 'customer':
            customer_type_filter.append(user)

    self.repeating_panel_1.items = customer_type_filter


 