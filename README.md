# Calculadora Básica feita em python

#### **1. Arquivo sistema.py**

* Contém o programa principal, que exibe um menu com as opções de operações matemáticas.

- Utiliza um laço de repetição while True para manter o sistema em execução contínua até que o usuário escolha sair.

- O menu é construído por meio da função opeArit, importada do módulo operações.

- Para controle de erros, foi utilizado o bloco try-except para capturar exceções como ValueError, impedindo que o programa trave com entradas inválidas.

- O comando sleep() da biblioteca time é usado para dar uma pequena pausa após cada operação, melhorando a experiência do usuário.

#### **2. Módulo operações (__init__.py)**

- Reúne todas as funções responsáveis pelas operações matemáticas: somar, subtrair, multiplicar, dividir e raiz.

- Cada função utiliza:

  - Entrada de dados com input().

  - Conversão de tipos com int().

  - Blocos try-except-else para validar as entradas e evitar erros como:

  - Inserção de texto em vez de números.

  - Interrupções inesperadas (como KeyboardInterrupt).

  - Divisão por zero (ZeroDivisionError).

- As funções também fazem uso de:

  - Loop while com flag de controle (ok = True) para garantir que apenas entradas válidas sejam processadas.

  - A função raiz() usa sqrt() da biblioteca math, importada com alias rq.

  - Funções auxiliares como linha() e menu() ajudam a formatar a interface do usuário.

#### **3. Módulo cor (__init__.py)**
- Define códigos de escape ANSI para aplicar cores ao texto do terminal.

- Variáveis como green, red, blue, reset, entre outras, são utilizadas para colorir mensagens, menus e alertas de erro, melhorando a interface visual e usabilidade.

#### **4. Principais Recursos Utilizados:**
- Laço de repetição while True: mantém o sistema funcionando até o usuário decidir sair.

- Blocos try-except: garantem robustez contra erros de entrada e execução.

- Funções com parâmetros padrão: facilitam o reaproveitamento e teste das operações.

- Importação modular (from ... import *): separa as responsabilidades do sistema.

- Códigos ANSI para cores: melhoram a leitura e o design visual do terminal.

- Organização em módulos (sistema.py, operações, cor): promove clareza e manutenibilidade.

