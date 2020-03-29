#calculate mean duration of vowels in spreadsheet

import openpyxl

wb = openpyxl.load_workbook('sample.xlsx', read_only = True)

sheet = wb['Sheet1']

sum = 0
for i in range(2,6):
    name = "B"+ str(i)
    sum = sum + sheet[name].value
print(sum)

mean_dur = sum/4
print(mean_dur)
