import openpyxl

book = openpyxl.load_workbook('revenue.xlsx')
user_data = book.get_sheet_by_name(str("sales"))
for x in range(1, user_data.max_row):
    flag = 1
    for i in range (0, 5):
        if (user_data[x][i].value != None):
            print (str(user_data[x][i].value)),
            flag = 0

    print ""
    if (flag == 1):
       break;

