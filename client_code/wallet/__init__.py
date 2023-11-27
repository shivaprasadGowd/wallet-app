from ._anvil_designer import walletTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil import alert, get_open_form

class wallet(walletTemplate):
    def __init__(self, user=None, **properties):
        self.init_components(**properties)
        self.user = user

    def button_1_click(self, **event_args):
        # Check if the user has a Casa account
        account_exists = anvil.server.call('check_account_for_user', self.user['casa'])

        if account_exists:
            my_message = f"{self.user['username']} has a Casa account!"
            self.label_2.text=my_message
        else:
            my_message = f"{self.user['username']} does not have a Casa account. You can create one here!"
            self.label_2.text=my_message

   

    
    
    
