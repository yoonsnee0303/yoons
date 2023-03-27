# Initializing
import json
import requests
import pandas as pd
import openpyxl as xls
import time
import json

# 도매매 상품리스트
from get_product_numbers import get_product_numbers

err_cnt = 0
cnt = 0
row = 5 # 입력을 시작하는 row

pass_point = False

# Open the JSON file
with open('data.json',encoding='utf-8') as file:
    # Load the contents of the file
    data = json.load(file)

dicts = {
 1: data['domeggook']['basis']['title'],
 21: data['domeggook']['seller']['nick'],
 11: data['domeggook']['basis']['keywords']['kw'],
 22: data['domeggook']['detail']['country'],
 22: data['domeggook']['price']['dome'],
 107: data['domeggook']['thumb']['original'],
}

temp_list = []
for i in range(149):
    temp_list.append('')


for i in range(149):
    for k,v in dicts.items():
        if k == i:
            temp_list[i] = v
            break
print(temp_list)

# # Save the changes to the Excel file
#     workbook.save('C:/Users/Data2/OneDrive/바탕 화면/윤/코드/dom_to_godo/dom_to_godo_rev1.xlsx')
