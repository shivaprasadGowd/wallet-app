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
        self.load_all_users()

    # def load_all_users(self):
    #     # Load all users into the repeating panel
    #     self.repeating_panel_1.items = app_tables.transactions.search()

    # def button_1_click(self, **event_args):
    #     """This method is called when the search button is clicked"""
    #     # Get the search term from the TextBox
    #     search_term = self.textbox_search.text

    #     # Perform a search in the transactions table
    #     search_result = app_tables.transactions.search(
    #         q.contains('user', search_term) |  # Replace 'column_name' with the actual column name to search
    #         # Add more conditions using | (bitwise OR) if needed )

    #     # Update the repeating panel with the search result
    #     self.repeating_panel_1.items = search_result

    # def reset_search_button_click(self, **event_args):
    #     """This method is called when the reset search button is clicked"""
    #     # Clear the TextBox and reload all users into the repeating panel
    #     self.textbox_search.text = ""
    #     self.load_all_users()

    # def repeating_panel_1_item_click(self, **event_args):
    #     """This method is called when an item in the repeating panel is clicked"""
    #     # Get the selected user from the repeating panel
    #     selected_user = event_args['item']

    #     # Check if a user is selected
    #     if selected_user is not None:
    #         # Get the user's information (replace 'column_name' with the actual column name)
    #         user_info = selected_user['user']

    #         # Update the TextBox or Label in the repeating panel with the selected user's information
    #         selected_user['textbox_in_item_template'].text = user_info
    #     else:
    #         # If no user is selected, handle it accordingly
    #         pass  # You may want to display a message or perform other actions
