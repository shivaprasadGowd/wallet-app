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
        self.button_2.visible = False

    def button_1_click(self, **event_args):
        # Check if the user has a Casa account
        account_exists = anvil.server.call('check_account_for_user', self.user['casa'])

        if account_exists:
            my_message = f"{self.user['username']} has a Casa account!"
            self.label_2.text = my_message
            # If the user has a Casa account, make Button_2 visible
            self.button_2.visible = True
            self.button_2.text="Make Digital Wallet"
        else:
            my_message = f"{self.user['username']} does not have a Casa account. You can create one here!"
            self.label_2.text = my_message
            self.button_2.visible = True
            self.button_2.text="Make Casa Account"
            # If the user doesn't have a Casa account, keep Button_2 invisible

    def button_2_click(self, **event_args):
        print("Button 2 clicked")
        if self.button_2.text == "Make Digital Wallet":
        # Logic to create a unique digital wallet
           digital_wallet = self.create_digital_wallet()
           print(f"Digital wallet created: {digital_wallet}")
        elif self.button_2.text == "Make Casa Account":
          print("Making Casa Account...")
        # Check if the user has a Casa account (self.user['casa'] is not None)
        if self.user['casa'] is None:
            # Logic to create a Casa account
            casa_account = self.create_casa_account()
            print(f"Casa account created: {casa_account}")
        else:
            pass
            # Handle the case where casa account is None (optional)
            #here casa account is None (optional)

    def create_casa_account(self):
     try:
        print("Creating Casa account...")
        print(f"Current user: {self.user}")
        print(f"Current 'casa' value: {self.user['casa']}")

        casa_number = random.randint(10**9, 10**10 - 1)

        # Update the user's 'casa' field with the generated number
        self.user['casa'] = casa_number
        self.user.save()  # Save the changes to the database

        # Return the generated Casa account number
        return casa_number
     except Exception as e:
        print(f"Error creating Casa account: {e}")
        return None


    def create_digital_wallet(self):
        # Implement the logic to create a unique digital wallet
        # You can use the user information, generate a wallet ID, etc.
        # Replace the following line with your actual implementation
        return f"Unique Digital Wallet for {self.user['username']}"

    