import openpyxl

wb = openpyxl.load_workbook('sample.xlsx', read_only = True)

sheet = wb['Sheet1']

for row in sheet.rows:
    for cell in row:
        print(cell.value)

