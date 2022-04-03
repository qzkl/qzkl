import openpyxl
import glob

fold=r"C:\Users\qzkl2\Documents\create"

file=glob.glob(fold+"/**/*.xlsx",recursive=True)

wbori=r"C:\Users\qzkl2\Documents\データ取得2.xlsx"
sheetori="ファイル名"
wb=openpyxl.load_workbook(wbori)
sheet=wb[sheetori]

for i in range(0,len(file)):
    sheet.cell(row=i+1,column=3).value=file[i]

wb.save(wbori)
wb.close()

