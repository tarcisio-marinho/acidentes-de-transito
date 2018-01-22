import time

# metadados = "data/metadata/acidentes-de-transito-com-vitimas.json"

def google_maps_search(latitude, longitude):
    url = "https://www.google.com.br/maps/search/{0},+{1}?sa=X&ved=0ahUKEwj8wsmc--fYAhVJkZAKHToBCkgQ8gEIJzAA".format(latitude, longitude)
    return url


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

    itens["link"] = google_maps_search(new[1], new[0])
    itens["data"] = new[2]
    itens["hora"] = new[3]
    itens["bairro"] = new[4]
    itens["endereco"] = new[5]
    itens["complemento"] = new[6]
    itens["ocorrencia"] = new[7]
    if(new[8] == 'F' or new[8] == "f" or new[8] == "-" or new[8] == "'''"):
        itens["qtd_vitimas"] = 0
    else:
        itens["qtd_vitimas"] = int(new[8]) 
    itens["veiculo"] = new[10]

    return itens


def get_data(data):

    acidentes_por_data = {}
    acidentes_por_quantidade_de_feridos = {}
    acidentes_por_veiculo = {}
    acidentes_por_bairro = {}
    
    todas_ocorrencias = []
    
    data = data.split("\n")
    data.remove("")

    for line in data:
        todas_ocorrencias.append(reshape_data(line))
        
    
    # bairro
    for ocorrencia in todas_ocorrencias: 
        if(ocorrencia["bairro"] not in acidentes_por_bairro):
            acidentes_por_bairro[ocorrencia["bairro"]] = []
            acidentes_por_bairro[ocorrencia["bairro"]].append(ocorrencia)
        else:
            acidentes_por_bairro[ocorrencia["bairro"]].append(ocorrencia)

    # data
    for ocorrencia in todas_ocorrencias:
        if(ocorrencia["data"] not in acidentes_por_data):
            acidentes_por_data[ocorrencia["data"]] = []
            acidentes_por_data[ocorrencia["data"]].append(ocorrencia)
        else:
            acidentes_por_data[ocorrencia["data"]].append(ocorrencia)
    
    # qtd_feridos
    for ocorrencia in todas_ocorrencias:
        if(ocorrencia["qtd_vitimas"] not in acidentes_por_quantidade_de_feridos):
            acidentes_por_quantidade_de_feridos[ocorrencia["qtd_vitimas"]] = []
            acidentes_por_quantidade_de_feridos[ocorrencia["qtd_vitimas"]].append(ocorrencia)
        else:
            acidentes_por_quantidade_de_feridos[ocorrencia["qtd_vitimas"]].append(ocorrencia)
    
    # veiculo
    for ocorrencia in todas_ocorrencias:
        if(ocorrencia["veiculo"] not in acidentes_por_veiculo):
            acidentes_por_veiculo[ocorrencia["veiculo"]] = []
            acidentes_por_veiculo[ocorrencia["veiculo"]].append(ocorrencia)
        else:
            acidentes_por_veiculo[ocorrencia["veiculo"]].append(ocorrencia)


    return acidentes_por_bairro, acidentes_por_data, acidentes_por_quantidade_de_feridos,
           acidentes_por_veiculo
