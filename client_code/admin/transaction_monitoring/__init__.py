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
        self.repeating_panel_1.items = app_tables.transactions.search()


    

    def button_1_click(self, **event_args):
        # Get the user entered in the textbox
        entered_user = self.textbox_search.text

        # Filter transactions based on the entered user
        filtered_transactions = app_tables.transactions.search(user=entered_user)

        # Update the repeating panel with the filtered transactions
        self.repeating_panel_1.items = filtered_transactions
      
