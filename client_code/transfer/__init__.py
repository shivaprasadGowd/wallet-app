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

        amount = float(self.text_box_4.text)
        currency = self.drop_down_1.selected_value

        # Extract the username from the user Row
        username = self.user['username']

        # Call the server function to transfer money
        anvil.server.call('transfer_money', username, amount, currency)

        # Optionally, update any UI elements or show a success message
        self.label_4.text = f'Transferred {amount} {currency} successfully.'

   