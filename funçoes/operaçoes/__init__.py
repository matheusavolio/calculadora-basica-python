from math import sqrt as rq
from funçoes.cor import *
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
            ok = False
            return print(f"{n1} + {n2} = {r} ")

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
        
def operador(a=0):
    ok = True
    while ok == True:
        try:
            a = int(input("""[1] para somar
[2] para subtrair,
[3] para multiplicar,
[4] para dividir,
[5] para raiz quadrada,
Sua opção: """))
        except (ValueError, KeyboardInterrupt, TypeError):
            print(f"{red}ERRO! Digite apenas números inteiros.{reset}")
        else:
            ok = False
            return a