import gspread

gc = gspread.service_account('secret.json')

spreadsheet = gc.open('Weather_data')

# Get worksheet by index
worksheet_one = spreadsheet.get_worksheet(0)

# Get worksheet by name
worksheet_two = spreadsheet.worksheet('2014')

# data_2013 = worksheet_one.get_all_records()
# print(data_2013)

data_2014 = worksheet_two.get_all_records()
# print(data_2014)

