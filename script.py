import pandas as pd
import numpy as np


'''
    Pesquisas -> 


    por data



    por acidentes
    


    por quantidades de pessoas feridas


'''

def search(tipo="data", numero=10):
    if(not tipo):
        pass

    elif(tipo == "acidentes"):
        pass
    
    elif(tipo == "qtd_pessoas_feridas"):
        pass

def get_data(data):
    acidentes_por_data = []
    acidentes_por_tipo = []
    acidentes_por_quantidade_de_feridos = []

    data = data.split("\n")
    for line in data:
        print(line)


    return data


if __name__ == "__main__":
    path = "data/acidentes-2016.csv"
    with open(path) as f:
        dados = f.read()
    print(dados)
    dados = get_data(dados)
