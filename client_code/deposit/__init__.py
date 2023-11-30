from ._anvil_designer import depositTemplate
from anvil import *
import anvil.server

class deposit(depositTemplate):
  def __init__(self, user= None, **properties):
    # Set Form properties and Data Bindings.
    self.user = user
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    count=0
    if app_tables.accounts.search(casa=self.text_box_2.text):
      count= count+1
    else:
      self.label_2.text="Account does not exist"
    e_wallet= anvil.server.call('generate_unique_id',self.user['username'],self.user['phone'])
    money3= anvil.server.call('money',self.drop_down_1.text,self.text_box_3.text)
    if count ==1:
      anvil.server.call(
        'depo',
        self.user['username'],
        self.text_box_2.text,
        e_wallet,
        money3,
    )

  
