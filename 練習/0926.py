import pathlib
import openpyxl
import csv

lwb=openpyxl.Workbook()

lsh=lwb.active


path=pathlib.Path("..\data\sales")
for pass_obj in path.glob("**/*.*"):
    print(pass_obj)