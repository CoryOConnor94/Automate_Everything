import gspread
import re

gc = gspread.service_account('secret.json')

spreadsheet = gc.open('Weather_data')

# Get worksheet by index
worksheet_one = spreadsheet.get_worksheet(0)

# Get worksheet by name
worksheet_two = spreadsheet.worksheet('2014')

# Get cell using index
cell_one = worksheet_one.get_values('D5')[0][0]
# print(cell_one)

# Get cell using acell
cell_two = worksheet_one.acell('D8').value
# print(cell_two)

# Search for cell, returned as object
cell_three = worksheet_one.find('-10')
# Get cell objects coordinates
# print(cell_three.row, cell_three.col)

# Search for multiple cells by value, returned as list of objects
cells = worksheet_one.findall('-9')
# print(cells)

# Get coordinates of multiple cells
# for cell in cells:
#     print(cell.row, cell.col)

# Find cells using regex
reg = re.compile(r'99')
cells = worksheet_one.findall(reg)
# print(cells)
print(worksheet_one.get('E5'))  # Should return the current value of cell E5

# Update cell, new value must be passed as list of lists
worksheet_one.update([[75]], 'E5')

# Update cell using row and column
worksheet_one.update_cell(5, 5, -39)