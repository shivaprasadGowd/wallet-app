from ._anvil_designer import SIGNUPTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

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
      input_value = self.text_box_4.text
      if len(input_value) != 10:
        alert("Pan Should be of 10 characters.")
      else:
        count=count+1  
      phone_number = self.text_box_6.text
      if len(str(phone_number)) == 10:
        count=count+1
      else:
        alert("Error: Please enter a valid 10-digit phone number.")
      aadharr= self.text_box_8.text
      if len(str(aadharr)) == 12:
        count=count+1
      else:
        alert("Error: Please enter a valid 12-digit Aadhar number")
        
    if count==3:
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
    input_value = self.text_box_4.text
    if any(char.islower() for char in input_value):
      alert("Warning: The input contains lowercase letters.")
    else:
      pass

    
      


