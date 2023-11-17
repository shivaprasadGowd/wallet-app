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
    
    if self.text_box_3.text != self.text_box_7.text:
      alert("password doesn't match")
      self.text_box_3.text =''
      self.text_box_3.focus()
      self.text_box_7.text =''
      self.text_box_7.focus()
      open_form('SIGNUP')
      
    elif self.text_box_3.text == self.text_box_7.text:
      anvil.server.call(
        'add_info', 
        self.text_box_1.text, 
        self.text_box_2.text, 
        self.text_box_3.text,
        self.text_box_4.text,
        self.text_box_5.text,
        self.text_box_6.text,
      )
      alert (self.text_box_1.text + ' added')
      open_form('LOGIN')

  def link_1_click(self, **event_args):
    open_form()


