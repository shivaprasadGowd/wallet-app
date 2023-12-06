from ._anvil_designer import admin_viewTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil import alert, open_form
import re

class admin_view(admin_viewTemplate):
  def __init__(self,user_data=None, **properties):
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
    confirmation = confirm("Are you sure you want to delete this user?", title="Delete Confirmation")

    if confirmation:
        user_data = self.item  # Assuming the item property is set when opening the form
        if user_data:
            # Assuming 'app_tables.users' is the table containing user data
            app_tables.users.get(id=user_data['id']).delete()
            
            alert("User deleted successfully.", title="Success")
            
            # Optionally, you can close the form after deletion
            self.close()
        else:
            alert("User data not found. Deletion failed.", title="Error")
    else:
        alert("Deletion canceled.", title="Canceled")
