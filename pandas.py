# TRABAIO DO TOMPSO
import openpyxl
import pandas as pd
import os
import pathlib

# Funcao base.
def BancoDeDadosEscola( ):
    escola = { "Aluno"      : [],
               "Disciplina" : [],
               "Notas"      : [] }

    print("""Olá, gostaria de fazer oq agora?
        |1°Mexer na planilha |2° Abrir a planilha|""")
    while True:
        escolha=int(input(" "))

        if escolha == 1:

            Nome=input("digite o nome do Aluno: ")
            escola["Aluno"].append(Nome)
            
            Disciplina=input("digite o nome do Disciplina: ")
            escola["Disciplina"].append(Disciplina)
            
            for i in range(4):
                nota=int(input(f"digite a {i +1}° nota: "))
                escola["Notas"].append(nota)

            print(escola)
            print("""Gostaria de adicionar mais alguma coisa?
                  |1°Sim |2° Não|""")
            escoa=int(input(" "))
            if escoa == 2:
                break
            
            
BancoDeDadosEscola()
