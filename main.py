import time
from mining import *

def search(info, tipo, data, numero=10):
    if(tipo == "data"):
        pass

    elif(tipo == "bairro"):


    elif(tipo == "tipo"):
        pass
    
    elif(tipo == "feridos"):
        pass


def menu(dados):

    bairro, data, feridos, veiculo = get_data(dados)

    while True:
        pesquisa = input("Pesquisar por: ")
        if(pesquisa == "bairro"):
            for local in bairro:
                print(local)

            escolha = input("Escolha o bairro: ")
            search(escolha, "bairro", bairro)

        elif(pesquisa == "data"):
            for dia in data:
                print(dia)

            escolha = input("Escolha a data: ")
            search(escolha, "data", data)

        elif(pesquisa == "feridos"):
            for quantidade in feridos:
                print(quantidade)

            escolha = input("Escolha a quantidade de feridos: ")
            search(escolha, "feridos", feridos)

        elif(pesquisa == "veiculo"):
            for automovel in veiculo:
                print(automovel)
            
            escolha = input("Escolha o veiculo: ")
            search(escolha, "veiculo", veiculo)


def read_file():
    path = "data/acidentes-2016.csv"

    with open(path) as f:
        f.readline() # ignore first line
        dados = f.read()
    
    return dados

if __name__ == "__main__":
    dados = read_file()
    menu(dados)
