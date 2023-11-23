from ._anvil_designer import ViewprofileTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil import alert, open_form

class Viewprofile(ViewprofileTemplate):
    def __init__(self, user=None, **properties):
        self.init_components(**properties)
        self.user = user
        self.edit_mode = False  # Initial edit mode is set to False
        if user:
            self.label_8.text = f"Welcome to Green Gate Financial, {user['username']}"
            self.display_user_profile(user)  # Display user profile on form load

    def toggle_edit_mode_components(self):
        print(f"Edit mode: {self.edit_mode}")

        # Show/hide text boxes based on edit mode
        for i in range(1, 5):
            textbox = getattr(self, f'text_box_{i}')
            textbox.visible = not self.edit_mode

        self.button_1.text = "Edit Profile" if not self.edit_mode else "Save Changes"

    def display_user_profile(self, user):
        user_data = app_tables.users.get(username=user['username'])
        print(type(user_data))  # Check the type
        print(user_data)  # Check the result

        if user_data is not None:
            self.text_box_1.text = user_data['email'] if 'email' in user_data else ''
            self.text_box_2.text = str(user_data['phone']) if 'phone' in user_data else ''
            self.text_box_3.text = user_data['pan'] if 'pan' in user_data else ''
            self.text_box_4.text = user_data['aadhar'] if 'aadhar' in user_data else ''
            print("Text values after setting:")
            print(f"Textbox 1: {self.text_box_1.text}")
            print(f"Textbox 2: {self.text_box_2.text}")
            print(f"Textbox 3: {self.text_box_3.text}")
            print(f"Textbox 4: {self.text_box_4.text}")
        else:
            # Handle the case when user data is not found
            self.text_box_1.text = ''
            self.text_box_2.text = ''
            self.text_box_3.text = ''
            self.text_box_4.text = ''
            print("User data not found.")

    def link_1_click(self, **event_args):
        open_form('customer', user=self.user)

    def button_1_click(self, **event_args):
        if not self.edit_mode:
            # Toggle to edit mode
            self.edit_mode = True
            self.toggle_edit_mode_components()
        else:
            # Save changes and toggle back to view mode
            user_data = app_tables.users.get(username=self.user['username'])
            print(type(user_data))  # Check the type before attempting to save
            if user_data is not None:
                user_data['email'] = self.text_box_1.text
                user_data['phone'] = self.text_box_2.text
                user_data['pan'] = self.text_box_3.text
                user_data['aadhar'] = self.text_box_4.text
                alert("User details updated successfully.", title="Success")
            else:
                alert("User data not found.", title="Error")

            # Toggle back to view mode
            self.edit_mode = False
            self.toggle_edit_mode_components()
