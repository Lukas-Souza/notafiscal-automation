def verif_xml(information, df_, name_file):
    # Verificar o cnpj
    if information['numero_nota'] != null:
    
        if verifyCNPJ(information, df_):
            if verifyClient:
                if verifyValue(information['valor'], df_):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    


def verifyCNPJ(information, df_):
      if information['CNPJ'] == df_['CNPJ']:
            
        return 0

def verifyValue(value, df_):
    if value != null:
        if value == df_['VALOR']:
            return True
        else:
            return False
        
def verifyClient(edf_client, name_file):
    if df_client != null:
        if name_file == df_client:
            return True
        else:
            return False