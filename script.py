import pandas as pd
import numpy as np
import time

'''
    Pesquisas -> 


    por data



    por acidentes
    


    por quantidades de pessoas feridas

    por localizacao -> cidade


    ao escolher um dos tipos de busca, lista todos os acidentes. ao escolher um acidete, dar detalhes do acidente
    ->qtd de feridos, bairro, data, hora, e link para localizacao lat e long no google maps


'''

def menu():
    while True:
        pass

    search()




def google_maps_search(latitude, longitude):
    url = "https://www.google.com.br/maps/search/{0},+{1}?sa=X&ved=0ahUKEwj8wsmc--fYAhVJkZAKHToBCkgQ8gEIJzAA".format(latitude, longitude)
    return url





def search(desc, tipo="data", numero=10):
    if(not tipo):
        pass

    elif(tipo == "tipo_de_acidente"):
        pass
    
    elif(tipo == "qtd_pessoas_feridas"):
        pass


    elif(tipo == "local"):
        pass






def get_data(data):

    """

        data = {"21/03/2016": ["acidente1", "acidente2"]} -> pode ver cada detalhe de cada acidente

        tipo = {"batida":["acidente1", "acidente2"], "colisao" : ["acidente3", "acidente4"]}

        feridos = {1:["acidente1", "acidente2"], 2: ["acidente3"]}

        local = {"boa viagem" : ["acidente1", "acidente2"]}
    
    """

    acidentes_por_data = {}
    acidentes_por_tipo = {}
    acidentes_por_quantidade_de_feridos = {}
    acidentes_por_local = {}

    data = data.split("\n")
    for line in data:
        print(line)
        time.sleep(2)
        


    return acidentes_por_data, acidentes_por_tipo, acidentes_por_quantidade_de_feridos, acidentes_por_local


if __name__ == "__main__":
    path = "data/acidentes-2016.csv"
    
    with open(path) as f:
        f.readline() # ignore first line
        dados = f.read()

    por_data, por_tipo, por_qtd_feridos, por_local = get_data(dados)
    #menu()
