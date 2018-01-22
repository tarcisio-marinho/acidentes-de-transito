from mining import *


def search(desc, tipo="data", numero=10):
    if(not tipo):
        pass

    elif(tipo == "tipo_de_acidente"):
        pass
    
    elif(tipo == "qtd_pessoas_feridas"):
        pass


    elif(tipo == "local"):
        pass


def menu():
    while True:
        pass

    search()


if __name__ == "__main__":
    path = "data/acidentes-2016.csv"
    
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
        "veiculo":""}
    """
    with open(path) as f:
        f.readline() # ignore first line
        dados = f.read()

    por_bairro, por_data, por_qtd_feridos, por_veiculo = get_data(dados)
    #menu()
