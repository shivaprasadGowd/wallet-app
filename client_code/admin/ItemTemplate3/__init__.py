from ._anvil_designer import ItemTemplate3Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil import alert, open_form
import re

class ItemTemplate3(ItemTemplate3Template):
  def __init__(self, user=None, **properties):
    # Set Form properties and Data Bindings.
      self.init_components(**properties)
      self.user = user 
      self.edit_mode = False
      
    
 
  def toggle_edit_mode_components(self):
        # Show/hide text boxes based on edit mode
        for i in range(1, 9):
            textbox = getattr(self, f'text_box_{i}')
            textbox.visible = self.edit_mode
          
        self.button_1.text = "Edit Profile" if not self.edit_mode else "Save Changes" 
    
  def display_user_profile(self, user):
        # Fetch and display data for the logged-in user
        # You can customize this based on your table structure
        user_data = app_tables.users.get(username=user['username'])
        self.text_box_1.text = f"{user_data['email']}"
        self.text_box_4.text = f"{user_data['phone']}"
        self.text_box_5.text = f"{user_data['pan']}"
        self.text_box_6.text = f"{user_data['aadhar']}"
    
  def button_1_click(self, **event_args):
    if not self.edit_mode:
        self.edit_mode = True
        self.toggle_edit_mode_components()
    else:
        if self.user is not None and 'username' in self.user:
            user_data = app_tables.users.get(username=self.user['username'])
            count = 0

            phone_number = self.text_box_4.text
            if self.validate_phone_number(phone_number):
                count += 1
            aadhar_card = self.text_box_5.text
            if len(str(aadhar_card)) == 12:
                count += 1 
            converted_text = self.text_box_6.text 
            if self.is_pan_card_detail(converted_text):
                count += 1

            if user_data is not None and count == 3:
                user_data['email'] = self.text_box_1.text
                user_data['phone'] = self.text_box_4.text
                user_data['aadhar'] = self.text_box_5.text
                user_data['pan'] = self.text_box_6.text

                alert("User details updated successfully.", title="Success")
            else:
                alert("User data not found or invalid details. Please check and try again.")

            # Toggle back to view mode
            self.edit_mode = False
            self.display_user_profile(self.user)
            self.button_1.text = "Edit Profile" if not self.edit_mode else "Save Changes"
  
  def validate_phone_number(self, phone_number):
      pattern = r'^[6-9]\d{9}$'
      if re.match(pattern, str(phone_number)):
          return True  
      else:
          return False    # Remove leading/trailing whitespace
        
  def is_pan_card_detail(self, text):
        if (
            len(text) == 10 and
            text[:5].isalpha() and
            text[5:9].isdigit() and
            text[9].isalpha()
        ):
          return True
        else:
          return False

  def text_box_6_change(self, **event_args):
      current_text = self.text_box_6.text
      converted_text = current_text.upper()
      self.text_box_6.text = converted_text

  def text_box_4_pressed_enter(self, **event_args):
      phone_number = self.text_box_4.text.strip()

  def button_2_click(self, **event_args):
    # Confirm deletion with user
    confirmation = confirm("Are you sure you want to delete this user?", title="Delete Confirmation")

    if confirmation:
        item = self.item
        item.delete()

        # Clear textboxes after deletion
        self.clear_textboxes()
    else:
        alert("User data not found. Deletion failed.", title="Error")

  def clear_textboxes(self):
    # Reset the values of textboxes
    for i in range(1, 9):
        textbox = getattr(self, f'text_box_{i}')
        textbox.text = ''



    
    
