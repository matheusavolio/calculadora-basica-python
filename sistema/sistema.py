from operaçoes import *
from cor import *
from arquivo import *
from time import sleep


arq = "teste.txt"
if not arquivoExiste(arq):
    criarArquivo(arq)



while True:
    try:
        resposta = opeArit(["[1] - somar\n"
                            "[2] - subtrair\n"
                            "[3] - Multiplicar\n"
                            "[4] - divisão\n"
                            "[5] - raiz quadrada\n"
                            "[6] - sair"])
        
        if resposta == 1:
            somar()
        elif resposta == 2:
            subtrair()
        elif resposta == 3:
            salvarArq(arq, multiplicar())
        elif resposta == 4:
            dividir()
        elif resposta == 5:
            raiz()
        elif resposta == 6:
            print(f"{red}Saindo do sistema...")
            sleep(1)
            respostaArq = menuArq(["[1] - ver lista de calculos feitos\n"
                                   "[2] - ver soma de todos os resultados\n"
                                   "[3] - sair e encerrar"])
        if resposta > 6:
            print(f"{red}ERRO! Digite apenas números listados no menu acima. {reset}")
            sleep(1)
    except (ValueError):
        print(f"{red}ERRO! Digite apenas números listados no menu acima. {reset}")
    sleep(1)
        



# DESCOBRIR UM JEITO DE ARMAZENAR AS CONTAS DENTRO DO ARQUIVO .TXT
# TERMINAR DE DOCUMENTAR AS FUNÇÕES
