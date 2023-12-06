from ._anvil_designer import show_usersTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class show_users(show_usersTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)

        # Set the visibility of the button to False
        self.button_1.visible = False

        # Filter users and set items in the repeating panel
        customer_type_filter = [user for user in app_tables.users.search() if user['usertype'] == 'customer']
        self.repeating_panel_1.items = customer_type_filter

    def button_1_click(self, **event_args):
        self.repeating_panel_1.visible = not self.repeating_panel_1.visible
