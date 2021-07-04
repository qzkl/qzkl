import pathlib
import openpyxl as px
import csv
import prime_num

p_num=prime_num.prime_n(100)

wb = px.Workbook()
ws = wb.active


for i in range(0,10):
    ws.cell(row = 1, column = i+1, value = p_num[i])


ps="C:/bbpy/vs/"
fname='sample.xlsx'
sfile=ps+fname
wb.save(sfile)
