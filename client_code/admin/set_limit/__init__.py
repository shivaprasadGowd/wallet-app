from ._anvil_designer import set_limitTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class set_limit(set_limitTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
        self.init_components(**properties)
        self.text_box_8.visible = False
        self.text_box_10.visible = False
        self.text_box_9.visible = False
        self.text_box_11.visible = False
        self.text_box_12.visible = False

        self.label_9.visible = False
        self.label_10.visible = False
        self.label_11.visible = False
        self.label_12.visible = False
        self.label_13.visible = False
      
        


        # Initialize the dropdown with account numbers
        self.populate_account_dropdown(user_data)

        if user_data:
            # Any code you write here will run before the form opens.
            self.populate_textboxes(user_data)
            self.toggle_edit_mode()
