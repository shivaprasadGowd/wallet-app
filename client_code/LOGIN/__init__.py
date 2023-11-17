from ._anvil_designer import LOGINTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class LOGIN(LOGINTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run before the form opens.

    def button_1_click(self, **event_args):
        """This method is called when the button is clicked"""
        
        username = self.text_box_1.text
        password = self.text_box_2.text

        # Call a server function to validate login credentials
        user_type = anvil.server.call('validate_login', username, password)

        if user_type:
            # Redirect based on user type
            if user_type == 'admin':
                open_form('admin')
            elif user_type == 'customer':
                open_form('customer')
        else:
            # Show an error message for invalid login
            alert("Invalid username or password", title="Login Failed")

    

    def SIGNUP_click(self, **event_args):
      """This method is called when the button is clicked"""
      open_form('SIGNUP')
