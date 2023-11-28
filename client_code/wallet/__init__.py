from ._anvil_designer import walletTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil import alert, get_open_form
import random

class wallet(walletTemplate):
    def __init__(self, user=None, **properties):
        self.init_components(**properties)
        self.user = user
        self.label_1.text = f"Welcome to Green Gate Financial, {user['username']}"
        anvil.server.call('link_accounts_to_users', account_id='', user_id=self.user['id'])
        self.button_2.visible = False
        self.bank_details_visible = False
        self.label_bank_details_error = Label(text="", role="alert")
        self.label_bank_name.visible = False
        self.textbox_bank_name.visible = False
        self.label_account_number.visible = False
        self.textbox_account_number.visible = False
        self.label_routing_number.visible = False
        self.textbox_routing_number.visible = False
        self.label_bank_details_error.visible = False
        self.button_save_bank_details.visible = False

    def button_1_click(self, **event_args):
        # Get the user-entered Casa account number from the textbox
        casa_number = self.textbox_account_number.text

        # Validate if the entered Casa account number is valid (you can add more validation as needed)
        if casa_number and casa_number.isdigit():
            casa_number = int(casa_number)

            # Check if the entered Casa account number is already in use
            if not app_tables.accounts.search(q.equal('casa', casa_number)):
                # Save the Casa account number to the user
                app_tables.accounts.add_row(user=self.user, casa=casa_number)

                # Map the e-wallet to the casa account
                e_wallet = anvil.server.call('map_e_wallet_to_casa', self.user['id'], casa_number)

                self.label_2.text = f"Casa account {casa_number} created successfully."
                self.button_2.visible = True
                self.button_2.text = "Make Digital Wallet"
            else:
                self.label_2.text = "Casa account number already in use. Please choose a different one."
        else:
            self.label_2.text = "Please enter a valid Casa account number."

    def button_add_bank_details_click_click(self, **event_args):
       # Toggle the visibility of bank details labels and textboxes
        self.bank_details_visible = not self.bank_details_visible
        self.label_bank_name.visible = self.bank_details_visible
        self.textbox_bank_name.visible = self.bank_details_visible
        self.label_account_number.visible = self.bank_details_visible
        self.textbox_account_number.visible = self.bank_details_visible
        self.label_routing_number.visible = self.bank_details_visible
        self.textbox_routing_number.visible = self.bank_details_visible
        self.button_save_bank_details.visible = self.bank_details_visible
        self.label_bank_details_error.text = ""
       
    def button_save_bank_details_click(self, **event_args):
        # Get the entered bank details from textboxes
        bank_name = self.textbox_bank_name.text
        account_number = self.textbox_account_number.text
        routing_number = self.textbox_routing_number.text

        # Validate the bank details (you can add more validation as needed)
        if bank_name and account_number and routing_number:
            # Save the bank details to the 'accounts' table
            new_account = app_tables.accounts.add_row(
              id=str(id), 
              casa=int(account_number), 
              e_wallet= f"UniqueEwallet-{account_number}", 
              bank_name=bank_name, 
              routing_number=routing_number
            )


            self.label_bank_details_error.text = "Bank details saved successfully."
        else:
            self.label_bank_details_error.text = "Please fill in all bank details."

    def link_user_to_casa(self, user_id, casa_number):
        # Call the server function to link the user to a Casa account
        casa_row = anvil.server.call('link_user_to_casa', user_id=user_id, casa_number=casa_number)

        if casa_row:
            self.label_2.text = "User linked to Casa account successfully."

    def map_casa_to_digital_wallet(self, user_id, casa_number):
        # Call the server function to map the Casa account to a digital wallet
        digital_row = anvil.server.call('map_casa_to_digital_wallet', user_id=user_id, casa_number=casa_number)

        if digital_row:
            self.label_2.text = "Casa account mapped to digital wallet successfully."
            self.button_2.visible = True
            self.button_2.text = "Make Digital Wallet"
        else:
            self.label_2.text = "Error mapping Casa account to digital wallet."

    



            

  