import glob
import xlwt

book = xlwt.Workbook()
ws = book.add_sheet('First Sheet')  # Add a sheet
data_dict = {}

for file in glob.glob("*.txt"):     # reading the .txt files one by one from the current directory(Exercise2)
    f = open(file, 'r+')
    data = f.readlines()            # read all lines at once

    for i in range(len(data)):
        row = data[i].split()
        data_dict.setdefault(row[0], [])
        data_dict[row[0]].append(row[1])
    f.close()

column = 0
for key in data_dict:
    ws.write(0, column,key)
    for i in range(len(data_dict[key])):
        ws.write(i+1, column, data_dict[key][i])
    column = column + 1

book.save('Output2_1' + '.xls')
