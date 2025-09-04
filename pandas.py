# TRABAIO DO TOMPSO
import openpyxl
import pandas as pd
import os
import pathlib

escola = { "Aluno"      : [],
           "Disciplina"   : [],
           "notas"      : [] }
# Funcao base.
def BancoDeDadosEscola( ):
    escola = { "Aluno"      : [],
               "Disciplina"   : [],
               "Notas"      : [] }

    print("""Olá, gostaria de fazer oq agora?
        |1°Mexer na planilha |2° Abrir a planilha|""")
    escolha=int(input(" "))

    if escolha == 1:
        a=input("digite o nome do Aluno: ")
        escola["Aluno"]=a
        a=input("digite o nome do Disciplina: ")
        escola["Disciplina"]=a
        print(escola)
        
BancoDeDadosEscola()
