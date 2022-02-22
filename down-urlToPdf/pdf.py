import pdfkit
import time
import sys
import os
import xlrd

log_path = "pdf_log.txt"
options = {
    'encoding': "UTF-8",
    'page-width': 158,
    'page-height': 222,
    'margin-top': '0',
    'margin-right': '0',
    'margin-bottom': '0',
    'margin-left': '0',
    'javascript-delay': '5000',
    'no-outline': None,
    # 'zoom': 1.5
}


def log(path,message):
    try:
        with open(path,"a",encoding='utf-8') as f:
            f.write(message + time.ctime() + '\r\n')
    except Exception as e:
        print("log error:" + str(e))

if __name__ == '__main__':
    try:
        fileDir = "./pdf/"        
       

        data = xlrd.open_workbook('pdf.xlsx')
        table = data.sheet_by_index(0)
        nrows = table.nrows

        for i in range(nrows):
            url = table.row_values(i)[0]
            candId = table.row_values(i)[1]
            filename = fileDir + str(candId) +".pdf"
            print(filename)
            result = pdfkit.from_url(url, filename, options=options)        
        print("ALL Done")
    except Exception as e:
        log(log_path,str(e))