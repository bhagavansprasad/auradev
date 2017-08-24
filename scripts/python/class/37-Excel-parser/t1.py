import openpyxl
import dump_cell

book = openpyxl.load_workbook('revenue.xlsx')

'''
print dir(book)
for word in dir(book):
    print "\tprint (%s%s :%s%s%s, cell.%s)" % ('"', word, "%", "s", '"', word)
'''



wsheet = book.get_sheet_by_name(str("sales"))

cell = wsheet[1][0]

dump_cell.dump_cell_properties(wsheet[1][0])



''' 
for x in range(1, user_data.max_row):
    flag = 1
    for i in range (0, 5):
        if (user_data[x][i].value != None):
            print (str(user_data[x][i].value)),
            flag = 0

    print ""
    if (flag == 1):
       break;

''' 
