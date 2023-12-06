from ._anvil_designer import admin_viewTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class admin_view(admin_viewTemplate):
  def __init__(self, user_data, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.text_box_1.text = user_data.get('username', '')
    self.text_box_2.text = user_data.get('email', '')
    self.text_box_4.text = user_data.get('phone', '')
    self.label_7.text = user_data.get('aadhar', '')
    self.label_8.text = user_data.get('pan', '')
    self.textbox_3.text = user_data.get('password', '')