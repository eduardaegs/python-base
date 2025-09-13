
#!/usr/bin/env python3

"""Guia de Estilos no Python PEP 8 - Convenções de estilo seu código em Python"""

""" Hello World Multi linguas

Dependendo da lingua configurada no ambiente o programa exibe a mensagem 
correspondente. 

Como usar:

Tenha a variável LANG devidamente configurada ex:

    export LANG=pt_BR

Execução:

    python3 hello.py
    ou
    ./hello.py
"""

# Convenções de variáveis:

__version__ = "0.0.1"
__author__ = "Eduarda Andrade"
__licence__ = "Unlicense"

import os # os significa operational system

# Se pronuncia Dunder version Dunder | Dunder author Dunder | Dunder licence Dunder
current_language = os.getenv("LANG")
msg = 'Hello, World!'

if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = 'Ciao, Mondo!'

print(msg)

# lang = "pt_BR.utf8"
# print(lang)

# len(lang)
# print(len(lang))

# lang[:5]
# print(lang[:5])

# lang.split(".")
# print(lang.split("."))

# lang.split(".")[1]
# print(lang.split(".")[1])