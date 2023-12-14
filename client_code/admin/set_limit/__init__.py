from ._anvil_designer import set_limitTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class set_limit(set_limitTemplate):
  def __init__(self, user_data=None, **properties):
        # Initialize the base class
        self.init_components(**properties)
        
        # Access the user_data passed from the calling form
        self.user_data = user_data
        
        # Now you can access the username or any other user data
    
        
        
        

  def outlined_button_1_click(self, **event_args):
    username = self.user_data['username']
    setter = anvil.server.call('user_detail', username, self.text_box_1.text)

