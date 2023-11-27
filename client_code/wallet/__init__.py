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
            self.button_2.text="Make Digital Wallet"
        else:
            my_message = f"{self.user['username']} does not have a Casa account. You can create one here!"
            self.label_2.text = my_message
            self.button_2.visible = True
            self.button_2.text="Make Casa Account"
          
    def button_2_click(self, **event_args):
        if self.button_2.text == "Make Digital Wallet":
           digital_wallet = self.create_digital_wallet()
        elif self.button_2.text == "Make Casa Account":
          print("Making Casa Account...")
        if self.user['casa'] is None:
            casa_account = self.create_casa_account()
        else:
            pass

    def create_casa_account(self):
     try:
        casa_number = random.randint(10**9, 10**10 - 1)

        self.user['casa'] = casa_number
        self.user.save()
        return casa_number
     except Exception as e:
        return None


    def create_digital_wallet(self):
        return f"Unique Digital Wallet for {self.user['username']}"

    