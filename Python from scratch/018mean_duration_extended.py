import openpyxl

wb = openpyxl.load_workbook('sample.xlsx', read_only = True)

sheet = wb['Sheet1']

user = input("Please give me indexes - from and to [separated by spaces]\n"
             "Remember to select ONE column (e.g. B2 and B5 - not B2 and D4)\n\t")
list_indexes = user.split(" ")

start_name = list_indexes[0]
end_name = list_indexes[1]

for el in start_name:
    if el.isdigit() == False:
        start_position = start_name.replace(el,"")
        col_name = start_name.replace(start_position,"")
for elem in end_name:
    if elem.isdigit() == False:
        final_position = end_name.replace(elem,"")

sum = 0

for i in range(int(start_position),int(final_position)+1):
    name = col_name + str(i)
    sum = sum + sheet[name].value
print(sum)

mean_dur = sum/4
print(mean_dur)