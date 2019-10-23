import sys
import xlsxwriter
from xlrd import open_workbook


def my_workbook(*args):
    inputfile = args[0]
    outfile = args[1]
    #location = "C:\Test1.xlsx"
    book = open_workbook(inputfile)
    newbook = xlsxwriter.Workbook(outfile)
    sheet_names = book.sheet_names()
    sheet_index = [x for x in range(len(sheet_names))]
    for i in sheet_index:
        sheet = book.sheet_by_index(i)
        counts = {}
        for j in range(0, sheet.ncols):
            for col in range(sheet.ncols):
                for row in range(0, sheet.nrows):
                    val = sheet.cell_value(row, col)
                    if val not in counts:
                        counts[val] = 0
                    counts[val] += 1
        # print(counts)
        s = sum(counts.values())
        for (k, v) in counts.items():
            avg = v * 100.0 / s
            print(k, '= {:02.2f}'.format(avg))
            #av = ('{:02.2f}'.format(avg))


        ws = newbook.add_worksheet()
        row = 0
        col = 0
        for (k, v) in counts.items():
            ws.write(row, col, k)
            ws.write(row, col + 1, (v * 100.0 / s))
            row += 1

        newbook.close()


if __name__ =='__main__':
    if(len(sys.argv) == 3):
        script, inputfile, outfile = sys.argv
        args = (inputfile, outfile)
        my_workbook(*args)

