import os
import pandas as pd
from classes import read_xml


URI_Data_XMl = './data'
Data_XLSX = './Book 9 .xlsx'

filesByData =os.listdir(URI_Data_XMl)
for file in filesByData:
   try:
      list_nota_fiscal = read_xml(f'{URI_Data_XMl}/{file}')
      try:
         df = pd.read_excel(Data_XLSX)
      except:
         print("Ocorreu um erro ao ler o arquivo Excel")
   except:
      print("Ocorreu um erro ao localizar a pasta")