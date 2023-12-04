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


    # def button_1_click(self, **event_args):
    #   current_datetime = datetime.now()
    #   count = 0

    #   if app_tables.accounts.search(casa=self.text_box_2.text):
    #     count += 1
    #   else:
    #     self.label_2.text = "Account does not exist"

    # # Check if self.user is not None before accessing attributes
    #   if self.user is not None:
    #     wallet3 = anvil.server.call('generate_unique_id', self.user['username'], self.user['phone'])

    #     if wallet3 is None:
    #         self.label_2.text = "Error: Wallet is empty"
    #         return  # Exit the function or handle the error appropriately

    #     money3 = anvil.server.call('money', self.drop_down_1.selected_value, self.text_box_3.text)

    #     if count == 1:
    #         new_account = app_tables.transactions.add_row(
    #             user=self.user['username'],
    #             account=self.text_box_2.text,
    #             e_wallet=wallet3,
    #             money=money3,
    #             date=current_datetime
    #         )
    #     count = 1
    #     money3 = anvil.server.call('money', self.drop_down_1.selected_value, self.text_box_3.text)
    #     if app_tables.accounts.search(casa=self.text_box_2.text):count += 1
         
        
          
    #   else:
    #     self.label_2.text = "Error: User information is not available"

    # def button_1_click(self, **event_args):
    #   current_datetime = datetime.now()

    #   if self.user is not None:
    #     wallet3 = anvil.server.call('generate_unique_id', self.user['username'], self.user['phone'])

    #     if wallet3 is None:
    #         self.label_2.text = "Error: Wallet is empty"
    #         return  

    #     # Get the numeric amount entered in self.text_box_3.text
    #     money3_numeric = ''.join(filter(str.isdigit, str(self.text_box_3.text)))
    #     money_value = float(money3_numeric) if money3_numeric else 0.0

    #     selected_symbol = self.drop_down_1.selected_value

    #     # Get the entered account number as a string
    #     entered_account_number = str(self.text_box_2.text).strip()  # Ensure it's a string before stripping

    #     # Check if the entered account number is at least 10 digits long and consists of only digits
    #     if len(entered_account_number) < 10 or not entered_account_number.isdigit():
    #         self.label_2.text = "Error: Invalid account number. Please enter at least 10 digits."
    #         return  # Exit the function if the account number is invalid

    #     # Update the appropriate currency column in the user account with the symbol and numeric value
    #     user_accounts = app_tables.accounts.search(
    #         user=self.user['username'],
    #         casa=int(entered_account_number)  # Convert to int if required by your data structure
    #     )

    #     if user_accounts and len(user_accounts) > 0:
    #         user_account = user_accounts[0]

    #         # Update the corresponding currency column based on the selected symbol
    #         if selected_symbol == '€':
    #             user_account['money_euro'] = str(money_value
    #         elif selected_symbol == '$':
    #             user_account['money_usd'] = money_value
    #         elif selected_symbol == '₣':
    #             user_account['money_swiss'] = money_value
    #         elif selected_symbol == '₹':
    #             user_account['money_inr'] = money_value
    #         else:
    #             self.label_2.text = "Error: Invalid currency symbol selected."
    #             return  # Exit the function if an invalid symbol is selected

    #         user_account.update()

    #         # Add a transaction record for the updated account
    #         new_transaction = app_tables.transactions.add_row(
    #             user=self.user['username'],
    #             account=int(entered_account_number),  
    #             e_wallet=wallet3,
    #             money=f"{selected_symbol}-{money_value}", 
    #             date=current_datetime
    #         )

    #         self.label_2.text = "Money added successfully to the account"
    #     else:
    #         self.label_2.text = "Error: No matching accounts found for the user or invalid account number."
    #   else:
    #     self.label_2.text = "Error: User information is not available"

   def button_1_click(self, **event_args):
      current_datetime = datetime.now()

      if self.user is not None:
        wallet3 = anvil.server.call('generate_unique_id', self.user['username'], self.user['phone'])

        if wallet3 is None:
            self.label_2.text = "Error: Wallet is empty"
            return

        # Get the numeric amount entered in self.text_box_3.text
        money3_numeric = ''.join(filter(str.isdigit, str(self.text_box_3.text)))
        money_value = float(money3_numeric) if money3_numeric else 0.0

        selected_symbol = self.drop_down_1.selected_value

        # Get the entered account number as a string
        entered_account_number = str(self.text_box_2.text).strip()  # Ensure it's a string before stripping

        # Check if the entered account number is at least 10 digits long and consists of only digits
        if len(entered_account_number) < 10 or not entered_account_number.isdigit():
            self.label_2.text = "Error: Invalid account number. Please enter at least 10 digits."
            return  # Exit the function if the account number is invalid

        # Update the appropriate currency column in the user account with the symbol and numeric value
        user_accounts = app_tables.accounts.search(
            user=self.user['username'],
            casa=int(entered_account_number)  # Replace 'casa' with the appropriate column name
        )

        if user_accounts and len(user_accounts) > 0:
            user_account = user_accounts[0]

            # Update the corresponding currency column based on the selected symbol
            if selected_symbol == '€':
                user_account['money_euro'] = str((float(user_account['money_euro'] or 0)) + money_value)
            elif selected_symbol == '$':
                user_account['money_usd'] = str((float(user_account['money_usd'] or 0)) + money_value)
            elif selected_symbol == '₣':
                user_account['money_swis'] = str((float(user_account['money_swis'] or 0)) + money_value)
            elif selected_symbol == '₹':
                user_account['money_inr'] = str((float(user_account['money_inr'] or 0)) + money_value)
            else:
                self.label_2.text = "Error: Invalid currency symbol selected."
                return  # Exit the function if an invalid symbol is selected

            user_account.update()

            # Add a transaction record for the updated account
            new_transaction = app_tables.transactions.add_row(
                user=self.user['username'],
                account=int(entered_account_number),
                e_wallet=wallet3,
                money=f"{selected_symbol}-{money_value}",
                date=current_datetime
            )

            self.label_2.text = "Money added successfully to the account"
        else:
            self.label_2.text = "Error: No matching accounts found for the user or invalid account number."
      else:
        self.label_2.text = "Error: User information is not available"



  
