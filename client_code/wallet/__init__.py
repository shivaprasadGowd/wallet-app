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
        self.button_2.visible = False

    def button_1_click(self, **event_args):
        account_exists = anvil.server.call('check_account_for_user', self.user['casa'])
        aa=anvil.server.call('check_account_for_user_digital',self.user['digital'])
        if aa:
          message = f"{self.user['username']} has an existing E-Wallet"
          self.label_2.text= message
        else:
          if account_exists:
            my_message = f"{self.user['username']} has a Casa account!"
            self.label_2.text = my_message
            self.button_2.visible = True
            self.button_2.text = "Make Digital Wallet"
          else:
            my_message = f"{self.user['username']} does not have a Casa account. You can create one here!"
            self.label_2.text = my_message
            self.button_2.visible = True
            self.button_2.text = "Make Casa Account"

    def button_2_click(self, **event_args):
        if self.button_2.text == "Make Casa Account":
            if self.user['casa'] is None:
                casa_account = self.create_casa_account()
                self.button_2.text = "Make Digital Wallet"
                self.label_2.text = "CASA account Created"
            else:
                pass
        elif self.button_2.text == "Make Digital Wallet":
            digital_wallet = self.create_digital_wallet()
            self.button_2.visible= None
            self.label_2.text= "Digital Wallet Created and Linked with CASA Account"
            

    def create_casa_account(self):
      try:
        # Generate a random 10-digit Casa account number without negative values
        casa_number = random.randint(0, 10**10 - 1)

        # Check if the generated number is already in use in the 'users' table
        while app_tables.users.get(casa=casa_number):
            casa_number = random.randint(0, 10**10 - 1)

        # Save the Casa account number to the user
        self.user['casa'] = casa_number
        self.user.save()

        print(f"Casa account created successfully: {casa_number}")

        return casa_number
      except Exception as e:
        print(f"Error creating Casa account: {e}")
        return None



    def create_digital_wallet(self):
        if self.user['casa'] is not None:
            # Use the Casa account number to create a unique digital wallet
            digital_wallet = self.user['casa']
            # Save the digital wallet to the 'digital' table or use it as needed
            self.user['digital']= digital_wallet
            return digital_wallet
        else:
            return "Casa account not available. Please create one first."
