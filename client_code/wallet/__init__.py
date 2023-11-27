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
        account_exists = anvil.server.call('check_account_for_user', self.user['casa'])

        if account_exists:
            my_message = f"{self.user['username']} has a Casa account!"
            self.label_2.text = my_message
            self.button_2.visible = True
            self.button_2.text = "Make Casa Account"
        else:
            my_message = f"{self.user['username']} does not have a Casa account. You can create one here!"
            self.label_2.text = my_message
            self.button_2.visible = True
            self.button_2.text = "Make Casa Account"

    def button_2_click(self, **event_args):
        if self.button_2.text == "Make Casa Account":
            print("Making Casa Account...")
            if self.user['casa'] is None:
                casa_account = self.create_casa_account()
                self.button_2.visible = None
                self.label_2.text = "CASA account created and ditigal wallet linked"
            else:
                pass
        elif self.button_2.text == "Make Digital Wallet":
            # Add any additional logic or actions related to the digital wallet here
            pass

    def create_casa_account(self):
        try:
            # Generate a random 10-digit Casa account number without negative values
            casa_number = random.randint(0, 10**10 - 1)

            # Check if the generated number is already in use
            while app_tables.users.get(casa=casa_number):
                casa_number = random.randint(0, 10**10 - 1)

            # Save the Casa account number and create a unique digital wallet
            self.user['casa'] = casa_number
            digital_wallet = f"Digital Wallet for Casa Account {casa_number}"
            self.user['digital_wallet'] = digital_wallet
            self.user.save()

            return casa_number
        except Exception as e:
            return None
