from mining import *

def search(desc, tipo="data", numero=10):
    if(not tipo):
        pass

    elif(tipo == "tipo"):
        pass
    
    elif(tipo == "feridos"):
        pass


    elif(tipo == "local"):
        pass


def menu():
    while True:
        pesquisa = input("Pesquisar por: ")
        search(pesquisa)



if __name__ == "__main__":
    path = "data/acidentes-2016.csv"

    with open(path) as f:
        f.readline() # ignore first line
        dados = f.read()

    por_bairro, por_data, por_qtd_feridos, por_veiculo = get_data(dados)
    #menu()
