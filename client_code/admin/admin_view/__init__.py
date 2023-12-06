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
        self.edit_mode = False  
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

    def toggle_edit_mode_components(self):
        # Show/hide text boxes based on edit mode
        for i in range(1, 5):
            textbox = getattr(self, f'text_box_{i}')
            textbox.visible = self.edit_mode

        self.button_1.text = "Edit Profile" if not self.edit_mode else "Save Changes"

    


    def button_1_click(self, **event_args):
        if not self.edit_mode:
            # Toggle to edit mode
            self.edit_mode = True
            self.toggle_edit_mode_components()
        else:
            user_data = app_tables.users.get(username=self.user['username'])
            count=0
            phone_number= self.text_box_4.text
            if self.validate_phone_number(phone_number):
                  count=count+1
           
                   
            if user_data is not None and count==3:
              user_data['username'] = self.text_box_1.text
              user_data['email'] = self.text_box_2.text
              user_data['phone'] = self.text_box_4.text
              user_data['password'] = self.text_box_3.text
              user_data['address'] = self.text_box_7.text
              
                
              alert("User details updated successfully.", title="Success")
            else:
              alert("Please check the entered details to proceed")

            # Toggle back to view mode
            self.edit_mode = False
            self.button_1.text = "Edit Profile" if not self.edit_mode else "Save Changes"
      
    def validate_phone_number(self, phone_number):
      pattern = r'^[6-9]\d{9}$'
      if re.match(pattern, str(phone_number)):
        return True  
      else:
        return False    # Remove leading/trailing whitespace


    def text_box_4_pressed_enter(self, **event_args):
      phone_number = self.text_box_4.text.strip()

           