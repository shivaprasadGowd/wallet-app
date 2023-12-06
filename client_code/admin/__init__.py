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
    if user is not None:
            self.label_1.text = f"Welcome to Green Gate Financial, {user['username']}"
            self.repeating_panel_1.visible = False
            self.text_box_1.visible = False
            self.button_2.visible = False
            self.label_2.visible = False
            self.label_3.visible = False
            self.label_4.visible = False
    else:
        self.label_1.text = "Welcome to Green Gate Financial (User data not available)"
    

  
  def link_1_click(self, **event_args):
    open_form('Home')

  def button_1_click(self, **event_args):
    self.repeating_panel_1.visible = not self.repeating_panel_1.visible
    self.text_box_1.visible = not self.text_box_1.visible
    self.button_2.visible = not self.button_2.visible
    self.label_2.visible = not self.label_2.visible
    self.label_3.visible = not self.label_3.visible
    self.label_4.visible = not self.label_4.visible

    customer_type_filter = []

    for user in app_tables.users.search():
        if user['usertype'] == 'customer':
            customer_type_filter.append(user)

    self.repeating_panel_1.items = customer_type_filter

 


 