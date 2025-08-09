import os
import pandas as pd
from pathlib import Path
from classes import *


URI_Data_XMl = './data'
Data_XLSX = './table.xlsx'

filesByData =os.listdir(URI_Data_XMl)
for file in filesByData:
   try:
      path_ = f'{URI_Data_XMl}/{file}'
      list_nota_fiscal = read_xml(path_)
      nameFile = Path(file).stem
      try:
         if createNote(list_nota_fiscal, Data_XLSX,nameFile) != True:
            print("Ocorreu um erro")
         else:
            print(f"Nota {file} adicionada com sucesso")
      except Exception as erro:
         print(f"Ocorreu um erro ao ler o arquivo Excel: {erro}")
   except Exception as e:
      print(f"Ocorreu um erro ao localizar a pasta: {e}")