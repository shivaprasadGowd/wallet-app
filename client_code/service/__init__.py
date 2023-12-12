from ._anvil_designer import serviceTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class service(serviceTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)

  


  

  def link_1_click(self, **event_args):
    open_form('Home')

  def button_2_click(self, **event_args):
    open_form('SIGNUP')
