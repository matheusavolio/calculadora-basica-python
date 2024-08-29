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

def opeArit(a=0):
    """
    Função para receber a operação aritmética escolhida pelo usuário
    param a -> recebe um número int do usuário 
    try -> se nenhum erro acontecer até o momento, irá exibir um menu de opções
    except 1 -> se o usuário interromper por conta propria, encerra o programa
    except 2 -> exibe uma mensagem de erro caso ele insira um valor errado
    else -> finaliza o loop e retorna o resultado de a
    ok True -> usado para manter o loop ativo se o usuário não inserir algum dado de forma correta
    if a > 6 -> se o número do usuário for maior do que 6, irá exibir uma mensagem de erro
    caso o usuário insira um número 
    """
    ok = True
    while ok == True:
        try:
            if a == 1:
                return somar()
            elif a == 2:
                return subtrair()
            elif a == 3:
                return multiplicar()
            elif a == 4:
                return dividir()
            elif a == 5:
                raiz()
            elif a == 6:
                ok = False
                print(f"{red}Finalizando o programa...{reset}")
                sleep(1)
                print(f"{green}Programa finalizado! Volte sempre.{reset}")
                break 
        except:
            if a > 6:
                print(f"{red}ERRO! Digite apenas números listados no menu de opções.{reset}")
        else:
            ok = False
            return a

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
            r = [f"{n1} + {n2} = {n1 + n2}"]
        except (ValueError, TypeError, KeyboardInterrupt):
            print(f"{red}ERRO! Digite um número inteiro!{reset}")
        else:
            ok = False
            for c in r:
                return print(c)
            lista(c)

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