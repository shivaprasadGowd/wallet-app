from ._anvil_designer import transferTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class transfer(transferTemplate):
    def __init__(self, user=None, **properties):
        self.user = user
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

    def button_1_click(self, **event_args):
        # Get the current user or any other way to identify the user
        # Replace with the actual method to get the user

        amount = float(self.txt_amount.text)
        currency = self.dd_currency.selected_value

        # Call the server function to transfer money
        anvil.server.call('transfer_money', self.user, amount, currency)

        # Optionally, update any UI elements or show a success message
        self.label_status.text = f'Transferred {amount} {currency} successfully.'
