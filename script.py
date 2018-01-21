import time


def menu():
    while True:
        pass

    search()



def google_maps_search(latitude, longitude):
    url = "https://www.google.com.br/maps/search/{0},+{1}?sa=X&ved=0ahUKEwj8wsmc--fYAhVJkZAKHToBCkgQ8gEIJzAA".format(latitude, longitude)
    return url



'''
Pesquisas -> 
por data
por acidentes
por quantidades de pessoas feridas
por localizacao -> cidade
ao escolher um dos tipos de busca, lista todos os acidentes. ao escolher um acidete, dar detalhes do acidente
->qtd de feridos, bairro, data, hora, e link para localizacao lat e long no google maps
'''

def search(desc, tipo="data", numero=10):
    if(not tipo):
        pass

    elif(tipo == "tipo_de_acidente"):
        pass
    
    elif(tipo == "qtd_pessoas_feridas"):
        pass


    elif(tipo == "local"):
        pass



# transform an occorrency data into a dict
def reshape_data(data):

    itens = {}
    
    if('"' in data): # if description or complement has "" and ; between text
        cont = 0
        for i in data:
            if(i =='"'):
                cont+=1
        if(cont == 2):
            descricao = data.split('"')
            descricao[1] = descricao[1].replace(";", "")
            itens["descricao"] = descricao[1]
            new = "".join(descricao)
            new = new.split(";")
        else:
            new = data.split('"')
            new[1] = new[1].replace(";", "")
            new[3] = new[3].replace(";", "")
            new = ''.join(new)
            new = new.split(";")
            itens["descricao"] = new[9]

    else: # general case
        new = data.split(";")
        itens["descricao"] = new[9]

    itens["latitude"] = new[1]
    itens["longitude"] = new[0]
    itens["data"] = new[2]
    itens["hora"] = new[3]
    itens["bairro"] = new[4]
    itens["endereco"] = new[5]
    itens["complemento"] = new[6]
    itens["ocorrencia"] = new[7]
    if(new[8] == 'F' or new[8] == "f"):
        itens["qtd_vitimas"] = 0
    else:
        itens["qtd_vitimas"] = new[8]    
    itens["veiculo"] = new[10]

    return itens


"""
    data = {"21/03/2016": ["acidente1", "acidente2"]} -> pode ver cada detalhe de cada acidente

    tipo = {"batida":["acidente1", "acidente2"], "colisao" : ["acidente3", "acidente4"]}

    feridos = {1:["acidente1", "acidente2"], 2: ["acidente3"]}

    local = {"boa viagem" : ["acidente1", "acidente2"]}

"""

def get_data(data):

    acidentes_por_data = {}
    acidentes_por_tipo = {}
    acidentes_por_quantidade_de_feridos = {}
    acidentes_por_local = {}
    
    todas_ocorrencias = []
    
    data = data.split("\n")
    data.remove("")

    for line in data:
        todas_ocorrencias.append(reshape_data(line))
        
    
    for i, ocorrencia in enumerate(todas_ocorrencias):
        print(i, ocorrencia["qtd_vitimas"])
        """
    {"descricao":""
     "latitude":""
     "longitude":""
     "data":""
     "hora":""
     "bairro":""
     "endereco":""
     "complemento":""
     "ocorrencia":""
     "qtd_vitmas":""
     "veiculo":""}"""
    return acidentes_por_data, acidentes_por_tipo, acidentes_por_quantidade_de_feridos, acidentes_por_local


if __name__ == "__main__":
    path = "data/acidentes-2016.csv"
    
    with open(path) as f:
        f.readline() # ignore first line
        dados = f.read()

    por_data, por_tipo, por_qtd_feridos, por_local = get_data(dados)
    #menu()
