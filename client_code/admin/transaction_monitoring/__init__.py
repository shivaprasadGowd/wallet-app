from ._anvil_designer import transaction_monitoringTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class transaction_monitoring(transaction_monitoringTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        self.load_transactions()

    def load_transactions(self):
        """Load transactions into the repeating panel."""
        self.repeating_panel_1.items = app_tables.transactions.search()

    def add_user_transaction(self, username):
        """Add user's transactions to the repeating panel."""
        user_transactions = app_tables.transactions.search(username=username)
        self.repeating_panel_1.items = user_transactions

    def button_1_click(self, **event_args):
        """This method is called when the button is clicked."""
        # Get the username from the textbox
        username = self.text_box_1.text

        # Add user's transactions to the repeating panel
        self.add_user_transaction(username)
