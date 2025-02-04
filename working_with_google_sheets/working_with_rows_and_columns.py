import statistics
import time
import gspread

gc = gspread.service_account('secret.json')

spreadsheet = gc.open('Weather_data')

# Get worksheet by index
worksheet_one = spreadsheet.get_worksheet(0)

# Get worksheet by name
worksheet_two = spreadsheet.worksheet('2014')

# Access rows by cells
single_row = worksheet_two.get_all_values('A5:E5')
# print(single_row)

# Get row by index value
# single_row = worksheet_two.row_values(2)
# print(single_row)

# Access multiple rows
multiple_rows = worksheet_two.get_all_values('A5:E7')
# print(multiple_rows)

# Get column by index value
single_column = worksheet_two.col_values(2)
# print(single_column)

# Update column
# existing_column = worksheet_one.get_values('E2:E25')
# print(existing_column)
# new_column = [[round((float(cell[0]) * 9/5 + 32), 1)] for cell in existing_column]
# worksheet_one.update(new_column, 'E2:E25')

# Add new column
# worksheet_one.update([['Fahrenheit']] + new_column, 'G1:G25')

#Calculate mean of column
# existing_column = worksheet_one.get_values('G2:G25')
# existing_column = [float(value[0]) for value in existing_column]
# mean_of_column = [[round(statistics.mean(existing_column), 1)]]
# print(mean_of_column)
# worksheet_one.update(mean_of_column, 'G26')

# Listen for change and update cell in other worksheet
# worksheet_three = spreadsheet.worksheet('WATCH')
# while True:
#     value_one = worksheet_one.acell('G26').value
#     print(value_one)
#     time.sleep(2)
#     value_two = worksheet_one.acell('G26').value
#     print(value_two)
#     if value_one != value_two:
#         print('Changed')
#         worksheet_three.update([['CHANGED']], 'A2')