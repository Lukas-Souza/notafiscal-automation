import os 
import xml.etree.ElementTree as ET 
import pandas as pd

URI_Data_XMl = './data'
Data_XLSX = './Book 9 .xlsx'


def ReadXml(raiz):
    RPS_XML = raiz[1]
    dados_nota = {
    'numero_nota': (RPS_XML[1])[2].text,
    'data_emissao': RPS_XML[3].text,
    'data_vencimento': RPS_XML[4].text,
    'valor': RPS_XML[7].text,
    'cnpj_tomador': (RPS_XML[17])[0].text
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
        info = ReadXml(root)
        # Inspect Dataframe
        try:
            df = pd.read_excel(Data_XLSX)

        except:
            print("ERRO: Ocorreu um erro ao tentar localizar o DataSheet")

# except:
#     print("ERRO: Ocorreu um errro na procura da pasta dos XML")
# # extract tag RPS
