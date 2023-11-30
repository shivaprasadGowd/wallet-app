from ._anvil_designer import depositTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from datetime import datetime


class deposit(depositTemplate):
    def __init__(self, user=None, **properties):
        # Set Form properties and Data Bindings.
        print(f"User parameter in deposit form: {user}")
        self.user = user
        self.init_components(**properties)

        # Any code you write here will run before the form opens.


    def button_1_click(self, **event_args):
      current_datetime = datetime.now()
      count = 0

      if app_tables.accounts.search(casa=self.text_box_2.text):
        count += 1
      else:
        self.label_2.text = "Account does not exist"

    # Check if self.user is not None before accessing attributes
      if self.user is not None:
        wallet3 = anvil.server.call('generate_unique_id', self.user['username'], self.user['phone'])

        if wallet3 is None:
            self.label_2.text = "Error: Wallet is empty"
            return  # Exit the function or handle the error appropriately

        money3 = anvil.server.call('money', self.drop_down_1.selected_value, self.text_box_3.text)

        if count == 1:
            new_account = app_tables.transactions.add_row(
                user=self.user['username'],
                account=self.text_box_2.text,
                e_wallet=wallet3,
                money=money3,
                date=current_datetime
            )
      else:
        self.label_2.text = "Error: User information is not available"



  
