from ._anvil_designer import admin_viewTemplate
from anvil import alert, open_form
from anvil.tables import app_tables
import re

class admin_view(admin_viewTemplate):
    def __init__(self, user_data=None, **properties):
        self.init_components(**properties)
        self.edit_mode = False  # Set the initial mode to view
        if user_data:
            # Any code you write here will run before the form opens.
            self.populate_textboxes(user_data)
            self.toggle_edit_mode()  # Initial mode setup

    def button_2_click(self, **event_args):
        username = self.text_box_1.text
        user_to_delete = app_tables.users.get(username=username)

        if user_to_delete is not None:
            user_to_delete.delete()
            alert("User deleted successfully.", title="Success")

            # Clear textboxes after deletion
            self.clear_textboxes()

            # Raise an event to notify the parent form (admin form) about the deletion
            open_form('admin', user_data=user_to_delete)

    def clear_textboxes(self):
        self.text_box_1.text = ''
        self.text_box_2.text = ''
        self.text_box_3.text = ''
        self.text_box_4.text = ''
        self.text_box_5.text = ''
        self.text_box_6.text = ''
        self.text_box_7.text = ''

    def populate_textboxes(self, user_data):
        self.text_box_1.text = user_data['username']
        self.text_box_2.text = user_data['email']
        self.text_box_3.text = user_data['password']
        self.text_box_4.text = user_data['phone']
        self.text_box_5.text = user_data['aadhar']
        self.text_box_6.text = user_data['pan']
        self.text_box_7.text = user_data['address']

    def toggle_edit_mode(self):
        # Toggle between view and edit modes
        self.edit_mode = not self.edit_mode
        self.text_box_1.enabled = self.edit_mode
        self.text_box_2.enabled = self.edit_mode
        self.text_box_3.enabled = self.edit_mode
        self.text_box_4.enabled = self.edit_mode
        self.text_box_5.enabled = False  # Aadhar (not editable during edit mode)
        self.text_box_6.enabled = False  # Pan (not editable during edit mode)
        self.text_box_7.enabled = self.edit_mode

        # Change button_1 text based on the mode
        self.button_1.text = 'Save Changes' if self.edit_mode else 'Edit'

    def is_valid_phone(self, phone):
        # Check if the phone number is not empty and has exactly 10 digits
        return bool(phone and re.match(r'^\d{10}$', str(phone)))

    def button_1_click(self, **event_args):
        if self.edit_mode:
            # Validate phone number
            if not self.is_valid_phone(self.text_box_4.text):
                alert("Please enter a valid 10-digit phone number.", title="Error")
                return

            # Save changes to the database
            username = self.text_box_1.text
            user_to_update = app_tables.users.get(username=username)

            if user_to_update is not None:
                user_to_update.update(
                    email=self.text_box_2.text,
                    password=self.text_box_3.text,
                    phone=self.text_box_4.text,
                    aadhar=self.text_box_5.text,
                    pan=self.text_box_6.text,
                    address=self.text_box_7.text
                )

                alert("Changes saved successfully.", title="Success")

                # Toggle back to view mode after saving changes
                self.toggle_edit_mode()
        else:
            # Toggle to edit mode
            self.toggle_edit_mode()

    def button_3_click(self, **event_args):
      open_form('admin.show_users')

