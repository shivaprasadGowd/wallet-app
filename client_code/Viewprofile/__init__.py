from ._anvil_designer import ViewprofileTemplate
from anvil import *
import anvil.server

class Viewprofile(ViewprofileTemplate):
  def __init__(self, user=None, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    if user:
        self.label_8.text = f"Welcome, {user['username']}!"

    # Any code you write here will run before the form opens.

  def link_1_click(self, **event_args):
    open_form('Form1')

  def button_1_click(self, **event_args):
      self.repeating_panel_1.items = app_tables.users.search(phone=int(self.text_box_1.text))
