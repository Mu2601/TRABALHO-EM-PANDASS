# TRABAIO DO TOMPSO
import openpyxl
import pandas as pd
import os
import pathlib

# Funcao base.
def BancoDeDadosEscola( ):
    escola = { "Aluno"      : [],
               "Disciplina"   : [],
               "Notas"      : [] }

    print("""Olá, gostaria de fazer oq agora?
          |1°Mexer na planilha | 2° Abrir a planilha|""")

BancoDeDadosEscola()
