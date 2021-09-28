import glob
import xlwt

book = xlwt.Workbook()
ws = book.add_sheet('First Sheet')  # Add a sheet
rows = 0


# writing the headings to excel
f = open('ExerciseInput1.txt', 'r+')
data = f.readlines()                # read all lines at once
for i in range(len(data)):
    row = data[i].split()           # split each line as a list
    ws.write(rows, i, row[0])          # write the heading to excel
book.save('Output2' + '.xls')       # save the sheet to excel book
f.close()


# getting the value of each tag and storing it to excel sheet

for file in glob.glob("*.txt"):     # reading the .txt files one by one from the current directory(Exercise2)
    rows = rows+1
    f = open(file, 'r+')
    data = f.readlines()            # read all lines at once

    for i in range(len(data)):
        row = data[i].split()
        ws.write(rows, i, row[1])

    book.save('Output2' + '.xls')
    f.close()