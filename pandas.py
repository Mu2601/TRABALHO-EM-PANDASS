# TRABAIO DO TOMPSO
import openpyxl
import pandas as pd
import os
import pathlib

<<<<<<< HEAD
escola = { "Aluno"      : [],
           "Disciplina"   : [],
           "notas"      : [] }
=======
# Funcao base.
def BancoDeDadosEscola( ):
    escola = { "Aluno"      : [],
               "Disciplina"   : [],
               "Notas"      : [] }
>>>>>>> 8eea30491efdcc78d886eea6640f30c009b4974f

<<<<<<< HEAD
print("""Olá, gostaria de fazer oq agora?
      |1°Mexer na planilha |2° Abrir a planilha|""")
escolha=int(input(" "))
=======
    print("""Olá, gostaria de fazer oq agora?
          |1°Mexer na planilha | 2° Abrir a planilha|""")
>>>>>>> 8eea30491efdcc78d886eea6640f30c009b4974f

<<<<<<< HEAD
if escolha == 1:
    a=input("digite o nome do aluno: ")
    escola["Aluno"]=a
    print(escola)
def fodase():
    return 0
=======
BancoDeDadosEscola()
>>>>>>> 8eea30491efdcc78d886eea6640f30c009b4974f
