from ._anvil_designer import LOGINTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class LOGIN(LOGINTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)

    def button_1_click(self, **event_args):
        # Get the login input (username, phone number, or email)
        login_input = self.text_box_1.text.strip()

        # Get the password
        password = self.text_box_2.text.strip()

        # Get the user based on login input
        user = self.get_user(login_input)

        # Check if user exists and password matches
        if user is not None and user['password'] == password:
            user_type = user['usertype']

            if user_type == 'admin':
                open_form('admin', user=user)
            if user_type == 'customer':
                open_form('customer', user=user)
        else:
            self.label_9.text= "Invalid login credentials"
            self.text_box_1.text=''
            self.text_box_1.focus()
            self.text_box_2.text=''
            self.text_box_2.focus()


    def get_user(self, login_input):
    # Check if the login input is a valid username
      user_by_username = app_tables.users.get(username=login_input)
      if user_by_username:
        return user_by_username
        
      user_by_email = app_tables.users.get(email=login_input)
      if user_by_email:
        return user_by_email 

        
      user_by_phone = app_tables.users.get(phone=int(login_input))
      if user_by_phone:
        return user_by_phone
      else:
        return None

    def link_1_click(self, **event_args):
      open_form('Home')

    def button_2_click(self, **event_args):
      open_form('SIGNUP')

