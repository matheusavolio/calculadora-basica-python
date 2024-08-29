from operaçoes import *
from cor import *
from arquivo import *
# arq = "teste.txt"
# if not arquivoExiste(arq):
#     criarArquivo(arq)
# abrirArquivo(arq)


while opeArit() != 6:
    menu("MENU DE OPÇÔES")
    try:
        opeArit(a = int(input(f"""{blue}[1] para somar
[2] para subtrair
[3] para multiplicar
[4] para dividir
[5] para raiz quadrada
[6] para sair do programa
Sua opção:{reset} """)))
        ok = False
    except(ValueError, TypeError):
        print(f"{red}ERRO! Digite apenas números inteiros.{reset}")
        ok = True
    except (KeyboardInterrupt):
        print(f"{red}O usuário decidiu não inserir nenhuma informação{reset}")
        print(f"{red}Finalizando o programa...{reset}")
        sleep(1)
        print(f"{green}Programa finalizado! Volte sempre.{reset}")
        ok = False
        break

print(lista())


# ARMAZENAR TODAS AS CONTAS EM UMA LISTA
# IMPRIMIR ESSA LISTA EM UM ARQUIVO .TXT
# CADA CONTA EM UMA LINHA
# APÓS ENCERRAR O PROGRAMA, MOSTRAR UM NOVO MENU DE OPÇÕES
# NESSE MENU IRÁ CONTER: MOSTRAR TODOS OS CALCULOS FEITOS, SOMAR TODOS OS RESULTADOS, SAIR DO PROGRAMA.
