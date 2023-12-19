from ._anvil_designer import audit_trailTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from datetime import datetime

class audit_trail(audit_trailTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.user = user
    self.repeating_panel_1.items = app_tables.actions.search()

            

  def button_1_click(self, **event_args):
        entered_user = self.text_box_1.text
        filtered_actions = app_tables.actions.search(username=entered_user)
        self.repeating_panel_1.items = filtered_actions


