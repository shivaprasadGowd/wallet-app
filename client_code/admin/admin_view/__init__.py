from ._anvil_designer import admin_viewTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil import alert, open_form
import re

class admin_view(admin_viewTemplate):
    def __init__(self, user_data=None, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        if user_data:
            # Any code you write here will run before the form opens.
            self.text_box_1.text = user_data['username']
            self.text_box_2.text = user_data['email']
            self.text_box_3.text = user_data['password']
            self.text_box_4.text = user_data['phone']
            self.text_box_5.text = user_data['aadhar']
            self.text_box_6.text = user_data['pan']
            self.text_box_7.text = user_data['address']
  
    def button_2_click(self, **event_args):
        # Get the username from the text box
        username = self.text_box_1.text
  
        # Try to get the user from the users table
        user_to_delete = app_tables.users.get(username=username)
        
        if user_to_delete is not None:
            # Delete the user
            user_to_delete.delete()
            alert("User deleted successfully.", title="Success")
            
            # Clear textboxes after deletion
            self.clear_textboxes()
            open_form('admin', user=self.user_data)
            
            # Optionally, you can close the form after deletion
          
        else:
            alert("User not found. Deletion failed.", title="Error")
    
    def clear_textboxes(self):
        # Clear the text property of each textbox
        self.text_box_1.text = ''
        self.text_box_2.text = ''
        self.text_box_3.text = ''
        self.text_box_4.text = ''
        self.text_box_5.text = ''
        self.text_box_6.text = ''
        self.text_box_7.text = ''
