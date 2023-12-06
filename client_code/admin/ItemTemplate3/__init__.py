from ._anvil_designer import ItemTemplate3Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class ItemTemplate3(ItemTemplate3Template):
    def __init__(self, **properties):
        self.init_components(**properties)
       
       
    def button_1_click(self, **event_args):
        # Pass the username to the server function to fetch user_data
       
        open_form('admin.admin_view')
      
       

   

   

  



    
    
