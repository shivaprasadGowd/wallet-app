from ._anvil_designer import set_limitTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class set_limit(set_limitTemplate):
  def __init__(self,user_data=None, **properties):
    # Set Form properties and Data Bindings.
        self.init_components(**properties)
        self.text_box_3.visible = False
        self.text_box_4.visible = False
        self.text_box_5.visible = False
        self.text_box_6.visible = False
        self.text_box_7.visible = False

        self.label_5.visible = False
        self.label_6.visible = False
        self.label_7.visible = False
        self.label_8.visible = False
        self.label_9.visible = False

    
        


        # Initialize the dropdown with account numbers
        self.populate_account_dropdown(user_data)

        if user_data:
            # Any code you write here will run before the form opens.
            self.populate_textboxes(user_data)
            


  def populate_account_dropdown(self, user_data):
        # Get account numbers associated with the user from the 'accounts' table
        user_accounts = app_tables.accounts.search(user=user_data['username'])

        # Extract account numbers and populate the dropdown
        account_numbers = [str(account['casa']) for account in user_accounts]
        self.drop_down_1.items = account_numbers
    
  def populate_textboxes(self, user_data):
        self.label_1.text = user_data['username']
        
       
    
  def button_1_click(self, **event_args):
        # Get the selected account number from the dropdown
        selected_account_number = self.drop_down_1.selected_value

        if selected_account_number is not None:
            # Get the 'e_money' amount from the 'accounts' table
            account = app_tables.accounts.get(user=self.text_box_1.text, casa=int(selected_account_number))
            if account is not None:
                # Display 'e_money' in text_box_12
                self.text_box_7.text = str(account['e_money'])
  
                # Get the currency details from the 'currencies' table
                currency_details = app_tables.currencies.get(casa=int(selected_account_number))
  
                if currency_details is not None:
                    # Display currency details in respective textboxes and labels
                    self.text_box_3.text = str(currency_details['money_usd'])
                    self.text_box_5.text = str(currency_details['money_inr'])
                    self.text_box_4.text = str(currency_details['money_euro'])
                    self.text_box_6.text = str(currency_details['money_swis'])
  
                    # Set the visibility of text boxes and labels to True
                    self.text_box_3.visible = True
                    self.text_box_4.visible = True
                    self.text_box_5.visible = True
                    self.text_box_6.visible = True
                    self.text_box_7.visible = True

                    # Set the visibility of labels to True
                    self.label_5.visible = True
                    self.label_6.visible = True
                    self.label_7.visible = True
                    self.label_8.visible = True
                    self.label_9.visible = True

