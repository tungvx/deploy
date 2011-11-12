import datetime
from django.db import models
from django import forms
from settings import FILE_UPlOAD_PATH
import xlrd
import re

def fileEtracter(file):
    result = []
    fd = xlrd.open_workbook('%s /%s' % (FILE_UPlOAD_PATH, f.name), 'wb')     #Read excel file for get data
    sheet = fd.sheet_by_index(0) # Get the first sheet
    for col_x in range(sheet.ncols):
        for row_x in range(sheet.nrows):
            value = sheet.cell(row_x,col_x).value
            if value:
                temp = re.search('#<.*?>',unicode(value))
                if temp:
                    result.append(temp.group(0).rstrip('>').lstrip('#<'))
    return result
