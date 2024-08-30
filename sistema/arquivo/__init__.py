from operaçoes import *
from cor import *
def arquivoExiste(nome):
    try:
        a = open(nome, "rt")
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
def criarArquivo(nome):
    try:
        a = open(nome, "wt+")
        a.close
    except:
        print("Houve um erro na criação do arquivo")
    else:
        print(f"Arquivo {nome} criado com sucesso")


def lerArquivo(nome):
    menu(f"{green}CALCULOS{reset}")
    try:
        a = open(nome, "rt")
    except:
        print(f"Erro ao ler arquivo")
    else:
        for linha in a:
            dado = linha.split(";")
            dado[1] = dado[1].replace("\n", "")
        print(f"{cian}{dado[0]:<30}{dado[1]:>3} anos{reset}")    
    


def menuArq(lista):
    menu(f"{green}MENU DOS CALCULOS{reset}")
    for item in lista:
        print(f"{blue}{item}{reset}")
    opc = int(input(f"{green}Qual sua opção: {reset}"))
    


def salvarArq(arq, calculo):
    try:
        with open(arq, "at") as a:
            a.write(f"{calculo}\n")
    except Exception as e:
        print(f"Houve um erro na hora de escrever os dados: {e}")
    else:
        print("Novo cálculo salvo!")