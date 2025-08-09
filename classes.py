import xml.etree.ElementTree as ET
import pandas as pd
import numpy as np
def read_xml(url):
    tree = ET.parse(url)
    root = tree.getroot()
    rps_list = root[1]
    dados_nota = {
    'numero_nota': (rps_list[1])[2].text,
    'data_emissao': rps_list[3].text,
    'data_vencimento': rps_list[4].text,
    'valor': rps_list[7].text,
    'CNPJ': (rps_list[17])[0].text
    }
    return dados_nota

def createNote(list_nota_fiscal, Data_XLSX, file):
        df = pd.read_excel(Data_XLSX)
        print('#', sep='')
        for i in range(0,len(df),1):
            dataFrame = df.loc[i]
            if pd.isna(dataFrame['NUMERO DA NOTA']):
               if dataFrame['CNPJ'] == list_nota_fiscal['CNPJ']:
                  if str(dataFrame['VALOR']) == str(list_nota_fiscal['valor']):
                     
                    if dataFrame['CLIENTE '] == file:
                       df.at[i, 'NUMERO DA NOTA'] = list_nota_fiscal['numero_nota']
                       df.at[i, 'DATA DE EMISÃO'] = list_nota_fiscal['data_emissao']
                       df.at[i, 'DATA DE VENCIMENTO'] = list_nota_fiscal['data_vencimento']
                       df.to_excel(Data_XLSX, index=False)
                       return True
                    else:
                        print(':::::::::: NOTA NÂO ENCONTRADA :::::::::::::')
                        print(f"| DESEJA CRIAR UMA NOVA LINHA COM O NOME DE {file} ?")
                        print("| DIGITE S para SIM")
                        return True
                  else:
                     print(f"ERRO: VALORES DIFERENTE")
                     print(f"TIPO DO ERRO: O VALOR QUE ESTA NA PLANILHA É: {dataFrame['VALOR']} E O VALOR DA NOTA FISCAL É {list_nota_fiscal['valor']}")
                  #    print("DESEJA CONTINUAR?")
               else:
                  print("CNPJ NÂO SÂO IGUAIS")
      return True