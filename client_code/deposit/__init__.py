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
        self.label_1.text = f"Welcome to Green Gate Financial, {user['username']}"
        print(f"User parameter in deposit form: {user}")
        self.user = user
        self.init_components(**properties)

    # def button_1_click(self, **event_args):
    #   current_datetime = datetime.now()

    #   if self.user is not None:
    #     wallet3 = anvil.server.call('generate_unique_id', self.user['username'], self.user['phone'])

    #     if wallet3 is None:
    #         self.label_2.text = "Error: Wallet is empty"
    #         return

        
    #     money3_numeric = ''.join(filter(str.isdigit, str(self.text_box_3.text)))
    #     money_value = float(money3_numeric) if money3_numeric else 0.0

    #     selected_symbol = self.drop_down_1.selected_value

       
    #     entered_account_number = str(self.text_box_2.text).strip() 

        
    #     if len(entered_account_number) < 10 or not entered_account_number.isdigit():
    #         self.label_2.text = "Error: Invalid account number. Please enter at least 10 digits."
    #         return 

        
    #     user_accounts = app_tables.accounts.search(
    #         user=self.user['username'],
    #         casa=int(entered_account_number)  
    #     )

    #     if user_accounts and len(user_accounts) > 0:
    #         user_account = user_accounts[0]

            
    #         if selected_symbol == '€':
    #             user_account['money_euro'] = str((float(user_account['money_euro'] or 0)) + money_value)
    #         elif selected_symbol == '$':
    #             user_account['money_usd'] = str((float(user_account['money_usd'] or 0)) + money_value)
    #         elif selected_symbol == '₣':
    #             user_account['money_swis'] = str((float(user_account['money_swis'] or 0)) + money_value)
    #         elif selected_symbol == '₹':
    #             user_account['money_inr'] = str((float(user_account['money_inr'] or 0)) + money_value)
    #         else:
    #             self.label_2.text = "Error: Invalid currency symbol selected."
    #             return  

    #         user_account.update()

            
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

    # def link_click(self, **event_args):
    #   open_form('customer', user= self.user)


    def button_1_click(self, **event_args):
      current_datetime = datetime.now()

      if self.user is not None:
        wallet3 = anvil.server.call('generate_unique_id', self.user['username'], self.user['phone'])

        if wallet3 is None:
            self.label_2.text = "Error: Wallet is empty"
            return

        money3_numeric = ''.join(filter(str.isdigit, str(self.text_box_3.text)))
        money_value = float(money3_numeric) if money3_numeric else 0.0

        selected_symbol = self.drop_down_1.selected_value

        entered_account_number = str(self.text_box_2.text).strip()

        if len(entered_account_number) < 10 or not entered_account_number.isdigit():
            self.label_2.text = "Error: Invalid account number. Please enter at least 10 digits."
            return

        user_currencies = app_tables.currencies.search(
            user=self.user['username'],
            account=int(entered_account_number)
        )

        if user_currencies and len(user_currencies) > 0:
            user_currency = user_currencies[0]

            if selected_symbol == '€':
                user_currency['money_euro'] = str((float(user_currency['money_euro'] or 0)) + money_value)
            elif selected_symbol == '$':
                user_currency['money_usd'] = str((float(user_currency['money_usd'] or 0)) + money_value)
            elif selected_symbol == '₣':
                user_currency['money_swis'] = str((float(user_currency['money_swis'] or 0)) + money_value)
            elif selected_symbol == '₹':
                user_currency['money_inr'] = str((float(user_currency['money_inr'] or 0)) + money_value)
            else:
                self.label_2.text = "Error: Invalid currency symbol selected."
                return

            user_currency.update()

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

    def link_click(self, **event_args):
      open_form('customer', user=self.user)


      
  
