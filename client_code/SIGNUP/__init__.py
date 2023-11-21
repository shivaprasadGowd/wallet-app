from ._anvil_designer import SIGNUPTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import re

class SIGNUP(SIGNUPTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args): 
    count=0
    if self.text_box_3.text != self.text_box_7.text:
      alert("password doesn't match")
      self.text_box_3.text =''
      self.text_box_3.focus()
      self.text_box_7.text =''
      self.text_box_7.focus()
    elif self.text_box_3.text == self.text_box_7.text:
      converted_text = self.text_box_4.text 
      if self.is_pan_card_detail(converted_text):
        alert("Valid PAN card detail")
        count=count+1
      else:
        alert("Invalid PAN card detail")
      phone_number = self.text_box_6.text
  
      # if self.validate_phone_number(phone_number):
      #   count=count+1
      #   alert("Valid phone number:", phone_number)
      #   # Perform actions for a valid phone number
      # else:
      #   alert("Invalid phone number:", phone_number)  
      
      # phone_number = self.text_box_6.text
      # if len(str(phone_number)) == 10:
      #   count=count+1
      # else:
      #   alert("Error: Please enter a valid 10-digit phone number.")
      aadharr= self.text_box_8.text
      if len(str(aadharr)) == 12:
        count=count+1
      else:
        alert("Error: Please enter a valid 12-digit Aadhar number")
        
    if count==2:
      anvil.server.call(
        'add_info', 
        self.text_box_1.text, 
        self.text_box_2.text, 
        self.text_box_3.text,
        self.text_box_4.text,
        self.text_box_5.text,
        self.text_box_6.text,
        self.text_box_8.text
      )
      alert (self.text_box_1.text + ' added')
      open_form('LOGIN')

  def link_1_click(self, **event_args):
    open_form('Form1')

  def text_box_4_change(self, **event_args):
    current_text = self.text_box_4.text
    converted_text = current_text.upper()
    self.text_box_4.text = converted_text
    
    
   
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

  def validate_button_click(self, **event_args):
    # Get the phone number from the TextBox (self.text_box_6.text)
    phone_number = self.text_box_6.text.strip()  # Remove leading/trailing whitespace
    if sevalidate_phone_number(phone_number):
        alert("Valid phone number:", phone_number)
        # Perform actions for a valid phone number
    else:
        alert("Invalid phone number:", phone_number)
  

  def validate_phone_number(self, phone_number):
    # Define a regex pattern for the phone number format
    pattern = r'^(0|91)[6-9]\d{9}$'

    # Check if the provided phone number matches the pattern
    if re.match(pattern, str(phone_number)):
        return True  # Valid phone number
    else:
        return False  # Invalid phone number
    
 
 
      


