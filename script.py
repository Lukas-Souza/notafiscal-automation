import os 
import xml.etree.ElementTree as ET 
from openpyxl import load_workbook
import pandas as pd
from verify_xml import verif_xml


URI_Data_XMl = './data'
Data_XLSX = './Book 9 .xlsx'


def ReadXml(raiz):
    RPS_XML = raiz[1]
    dados_nota = {
    'numero_nota': (RPS_XML[1])[2].text,
    'data_emissao': RPS_XML[3].text,
    'data_vencimento': RPS_XML[4].text,
    'valor': RPS_XML[7].text,
    'CNPJ': (RPS_XML[17])[0].text
}

    return dados_nota

filesByData =os.listdir(URI_Data_XMl)
# try:
for file in filesByData:
        try:
            tree = ET.parse(f'{URI_Data_XMl}/{file}')
        except:
            print("Ocorreu um erro ao localizar a pasta")
        root = tree.getroot()
        # Inspect Dataframe
        try:
            df = pd.read_excel(Data_XLSX)
            cnpj_tomador = df['CNPJ'].values        
            
            if verif_xml(ReadXml(root), df,f'{URI_Data_XMl}/{file}'):
                fileXlsx = load_workbook(f'{URI_Data_XMl}/{file}')
                planilha = fileXlsx['']
                 
            

        except:
            print("ERRO: Ocorreu um erro ao tentar localizar o DataSheet")

# except:
#     print("ERRO: Ocorreu um errro na procura da pasta dos XML")
# # extract tag RPS
