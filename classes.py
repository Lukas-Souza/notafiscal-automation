import xml.etree.ElementTree as ET
def read_xml(url):
    print("DDD")
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
