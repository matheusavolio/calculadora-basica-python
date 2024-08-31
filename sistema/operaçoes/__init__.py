from math import sqrt as rq
from cor import *
from time import sleep

def linha(tam=42):
    """
    Função que retorna linhas
    param tam -> define param opcional de impressão das linhas caso não seja inserido nenhum
    parâmetro
    """
    return "-" * tam

def menu(txt):
    print(linha())
    print(f"{green}{txt.center(42)}{reset}")
    print(linha())

def opeArit(lista):
        menu(f"{green}MENU PRINCIPAL{reset}")
        for item in lista:
            print(f"{blue}{item}{reset}")
        opc = int(input(f"{green}Sua opção: {reset}"))
        return opc

def lista(msg):
    lista.append(msg)


def somar(n1=0, n2=0):
    """
    Função para somar dois números.
    param n1 -> recebe um número int do usuário
    param n2 -> recebe outro número int do usuário
    try -> 
        enquanto nao ocorrer nenhum erro, o sistema irá pedir pro usuário inserir dois números
        r -> Resultado da soma 
    except -> 
        Retorna uma mensagem de erro caso o usuário insira um dado incorreto ou não insira nada
    else -> 
        interrompe o loop transformando o ok em False  
        return -> Imprime os dois números inseridos pelo usuário e o resultado da soma.
    """
    ok = True
    while ok == True:
        try:
            n1 = int(input("Digite um valor: "))
            n2 = int(input("Digite outro valor: "))
            r = n1 + n2
        except (ValueError, TypeError, KeyboardInterrupt):
            print(f"{red}ERRO! Digite um número inteiro!{reset}")
        else:
            return print(f"{n1} + {n2} = {r}")

def subtrair(n1=0, n2=0):
    """
    Função para subtrair dois números.
    param n1 -> Recebe um número int do usuário
    param n2 -> Recebe outro número int do usuário
    try -> 
        enquanto nao ocorrer nenhum erro, o sistema irá pedir pro usuário inserir dois números
        r -> Resultado da subtração 
    except -> 
        Retorna uma mensagem de erro 
    else -> 
        interrompe o loop transformando o ok em False  
        return -> Imprime os dois números inseridos pelo usuário e o resultado da subtração.
    """
    ok = True
    while ok == True:
        try:
            n1 = int(input("Digite um valor: "))
            n2 = int(input("Digite outro valor: "))
            r = n1 - n2
            ok = True
        except (ValueError, TypeError, ):
            print(f"{red}ERRO! Digite um número inteiro!{reset}")
        else:
            return print(f"{n1} - {n2} = {r}")
        

def multiplicar(n1=0, n2=0):
    ok = True
    while ok == True:
        try:
            n1 = int(input("Digite um valor: "))
            n2 = int(input("Digite outro valor: "))
            r = n1 * n2
        except (ValueError, TypeError, KeyboardInterrupt):
            print(f"{red}ERRO! Digite um número inteiro!{reset}")
        else:
            ok = False
            return print(f"{n1} x {n2} = {r} ")
        

def dividir(n1=0, n2=0):
    ok = True
    while ok == True:
        try:
            n1 = int(input("Digite Dividendo: "))
            n2 = int(input("Digite o Divisor: "))
            r = n1 / n2
        except ZeroDivisionError:
            print(f"{red}ERRO! Não é possível dividir um número por 0.{reset}")
        except (ValueError, TypeError, KeyboardInterrupt):
            print(f"{red}ERRO! Digite um número inteiro!{reset}")
        else:
            ok = False
            return print(f"{n1} / {n2} = {r} ")
        
def raiz(n1=0):
    ok = True
    while ok == True:
        try:
            n1 = int(input("Insira um número para descobrir sua raiz quadrada: "))
            r = rq(n1)
        except (ValueError, TypeError, KeyboardInterrupt):
            print(f"{red}ERRO! Digite um número inteiro!{reset}")
        else:
            ok = False
            return print(f" √{n1} é {r}")