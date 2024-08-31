from operaçoes import *
from cor import *
from time import sleep
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
            multiplicar()
        elif resposta == 4:
            dividir()
        elif resposta == 5:
            raiz()
        elif resposta == 6:
            print(f"{red}Saindo do sistema...{reset}")
            sleep(1)
            break
        if resposta > 6:
            print(f"{red}ERRO! Digite apenas números listados no menu acima. {reset}")
            sleep(1)
    except (ValueError):
        print(f"{red}ERRO! Digite apenas números listados no menu acima. {reset}")
    sleep(1)
