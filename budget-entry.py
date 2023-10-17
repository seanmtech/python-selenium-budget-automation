import time
import os
import json
import gspread
from google.oauth2 import service_account
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pandas as pd

csvData = pd.read_csv('<user input file name>')

chrome_driver_path = "../Chrome-Driver/chromedriver.exe"
chrome_binary_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"
user_data_dir = "<redacted>"
credentials_path = '<redacted>'
credentials = service_account.Credentials.from_service_account_file(
    credentials_path,
    scopes=['https://www.googleapis.com/auth/spreadsheets']
)
# spreadsheet_id = '1IdnzqZmjRfS8WL4Y08tOCHzVuPlofSgAy6PaCc6gPOQ'
# gc = gspread.authorize(credentials)
# sheet = gc.open_by_key(spreadsheet_id).sheet1

# month_mapping = {
#     'january': {'number': 1, 'evDolMonthStr': 'Jan'},
#     'february': {'number': 2, 'evDolMonthStr': 'Feb'},
#     'march': {'number': 3, 'evDolMonthStr': 'Mar'},
#     'april': {'number': 4, 'evDolMonthStr': 'Apr'},
#     'may': {'number': 5, 'evDolMonthStr': 'May'},
#     'june': {'number': 6, 'evDolMonthStr': 'Jun'},
#     'july': {'number': 7, 'evDolMonthStr': 'Jul'},
#     'august': {'number': 8, 'evDolMonthStr': 'Aug'},
#     'september': {'number': 9, 'evDolMonthStr': 'Sep'},
#     'october': {'number': 10, 'evDolMonthStr': 'Oct'},
#     'november': {'number': 11, 'evDolMonthStr': 'Nov'},
#     'december': {'number': 12, 'evDolMonthStr': 'Dec'}
# }

# # Read all cell data from Google Sheets into a 2d array
# fullSheetData = sheet.get_all_values()

# # Open Chrome instance & navigate to Everydollar.com

    # get Chrome profile to log in to session
options = Options()
options.add_argument(f"--user-data-dir={user_data_dir}")
options.add_argument("--profile-directory=Default")

    # Create ChromeDriver instance
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 10)

    # Open Everydollar.com
driver.get("https://www.everydollar.com/app/budget")






#     # # **** MONTH SELECTOR FEATURE (enable and disable as you want) ******

#     # current month in number form
# current_month_num = time.localtime().tm_mon

#     # Define the month you want to select   (for now just hard code it and change as needed)
# user_chosen_month = "May"
# monthInput = month_mapping[user_chosen_month.lower()]['evDolMonthStr']

# month_dropdown_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "BudgetNavigation-date")))
# month_dropdown_button.click()
# time.sleep(1)

# if user_chosen_month.lower() in month_mapping:
#     monthInputNum = month_mapping[user_chosen_month.lower()]['number']

#     if monthInputNum < current_month_num:
#         # change the way we use CSS selector in everydollar (they do something wonky with 'past months')
#         print("This is a past month yay!")
#         print("this is month input: ", monthInput)
        


# print("monthInput here:", monthInput)
    # Construct the CSS selector using the target month's text
# (old) selector = f'//div[@class="MonthPicker-month"]//div[contains(text(), "{monthInput}")]'
# selector = f'//div[@class="MonthPicker-month"]//div[contains(text(), "{monthInput}")]/..'

#     # think I need to somehow pick the div ABOVE this one (aka the parent div) of the one I'm targeting with this f string
#         # my theory is this f string is "too specific" and the <div> it targets is "one layer too low" so to speak
# month_choice_button = wait.until(EC.element_to_be_clickable((By.XPATH, selector)))
# month_choice_button.click()
# time.sleep(5)

# Loop through csvData, adding each row as a new transaction on EveryDollar
for index, row in csvData.iterrows():

    amount = row['Amount']*-1
    date = row['Effective Date']
    description = row['Description']

    add_transaction_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "AddTransactionLink-module__AddTransactionLink--EjoHafiYHAtckTey")))
    add_transaction_button.click()

    amount_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@data-testid="transaction_form_amount_input"]')))
    amount_input.clear()
    amount_input.send_keys(amount)

    date_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='date']")))
    date_input.clear()
    date_input.send_keys(date)

    merchant_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='merchant']")))
    merchant_input.clear()
    merchant_input.send_keys(description)

    submit_transaction_button = wait.until(EC.presence_of_element_located((By.ID, "TransactionModal_submit")))
    submit_transaction_button.click()

    time.sleep(1)











    #COPY of old google Sheet looping approach (just to be safe)
# for row in fullSheetData:
#     add_transaction_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "AddTransactionLink-module__AddTransactionLink--EjoHafiYHAtckTey")))
#     add_transaction_button.click()

#     amount_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@data-testid="transaction_form_amount_input"]')))
#     amount_input.clear()
#     amount_input.send_keys(row[1])

#     merchant_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='merchant']")))
#     merchant_input.clear()
#     merchant_input.send_keys(row[0])

#     submit_transaction_button = wait.until(EC.presence_of_element_located((By.ID, "TransactionModal_submit")))
#     submit_transaction_button.click()

#     time.sleep(2)






