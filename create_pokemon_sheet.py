import openpyxl
from openpyxl import load_workbook
import xlrd




path = 'Pokemon_Dex - Copy.xlsx'
wb = xlrd.open_workbook(path)
book = openpyxl.Workbook()