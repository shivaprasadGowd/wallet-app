from ._anvil_designer import customerTemplate
from anvil import open_form

class customer(customerTemplate):
    def __init__(self, user=None, **properties):
        self.init_components(**properties)
        self.user = user  # Set the user attribute

        if user:
            # Use the information from the logged-in user
            self.label_1.text = f"Welcome to Green Gate Financial, {user['username']}"

    def button_1_click(self, **event_args):
        # Open the Viewprofile form and pass the user information
        open_form('Viewprofile', user=self.user)
