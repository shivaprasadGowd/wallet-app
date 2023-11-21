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
    # def get_user(self, login_input):
        # user_by_username = app_tables.users.get(username=login_input)
        # if user_by_username:
        #     return user_by_username
        
        # Check if the input is a valid phone number
        # user_by_phone = app_tables.users.search(
        #     q.like('phone', '%' + login_input + '%', case_sensitive=False)
        # ).get()
        # if user_by_phone:
        #     return user_by_phone

        # Check if the input is a valid email
        # user_by_email = app_tables.users.get(email=login_input)
        # if user_by_email:
        #     return user_by_email

        # return None  # No user found for the given input

    # def button_1_click(self, **event_args):
    #   login_input = self.text_box_1.text
    #   password_input = self.text_box_2.text

    # # Get the user object
    # user = self.get_user(login_input)

    # if user is not None and 'password' in user and user['password'] == password_input:
    #     alert("Login successful!")
    #     username = self.text_box_1.text
    #     password = self.text_box_2.text
    #     user_type = anvil.server.call('validate_login', username, password)

    #     if user_type:
    #         if user_type == 'admin':
    #             open_form('admin')
    #         elif user_type == 'customer':
    #             open_form('customer')
    #         elif user_type == '':
    #             open_form('customer')
    #     else:
    #         alert("Invalid username or password", title="Login Failed")
    # else:
    #     alert("Invalid username, phone number, email, or password.")
          
    def link_1_click(self, **event_args):
      open_form('Form1')

    def button_2_click(self, **event_args):
      open_form('SIGNUP')

    def button_1_click(self, **event_args):
      """This method is called when the button is clicked"""
      pass
