from ._anvil_designer import admin_viewTemplate
from anvil import *
import anvil.tables as tables
from anvil.tables import app_tables
from anvil import alert
from anvil import alert, open_form
import re

class admin_view(admin_viewTemplate):
    def __init__(self, user_data=None, **properties):
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
        username = self.text_box_1.text
        user_to_delete = app_tables.users.get(username=username)

        if user_to_delete is not None:
            user_to_delete.delete()
            alert("User deleted successfully.", title="Success")
            
            # Clear textboxes after deletion
            self.clear_textboxes()
            
            # Raise an event to notify the parent form (admin form) about the deletion
            open_form('admin', user_data=user_to_delete)
       

    def clear_textboxes(self):
        self.text_box_1.text = ''
        self.text_box_2.text = ''
        self.text_box_3.text = ''
        self.text_box_4.text = ''
        self.text_box_5.text = ''
        self.text_box_6.text = ''
        self.text_box_7.text = ''

  
    def button_1_click(self, **event_args):
       pass
           