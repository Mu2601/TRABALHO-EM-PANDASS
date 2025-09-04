# TRABAIO DO TOMPSO
import openpyxl
import pandas as pd
import os
import pathlib

# Funcao base.
def BancoDeDadosEscola( ):

    # Variavel base.
    escola = { "Aluno"       : [],
               "Disciplina"  : [],
               "Notas0"      : [],
               "Notas1"      : [],
               "Notas2"      : [],
               "Notas3"      : [] }

    sDiretorioAtual = os.path.dirname(os.path.realpath(__file__))

    # DEBUG; qual diretorio ele esta.
    print(f"O diretorio atual e: {sDiretorioAtual}")

    while True:

        print("""Olá, gostaria de fazer oq agora?
        |1°Mexer na planilha |2° Abrir a planilha|""")

        escolha=int(input(""))

        if escolha == 1:
            Nome=input("digite o nome do Aluno: ")
            escola["Aluno"].append(Nome)
            
            Disciplina=input("digite o nome do Disciplina: ")
            escola["Disciplina"].append(Disciplina)
            
            for i in range(4):
                nota=int(input(f"digite a { i + 1 }° nota: "))
                escola[f"Notas{i}"].append(nota)

            db = pd.DataFrame(escola)
            print( db )

            print( "Gostaria de exportar a planilha?" )
            print( "1 - Sim" )
            print( "2 - Nao" )
            exportar = int(input(""))
            if( exportar == 1 ):
                print("Qual sera o nome do arquivo?")
                sNomeDoArquivo = input("")
                sNovoArquivo = os.path.join( sDiretorioAtual, sNomeDoArquivo ) 
                db.to_excel()
    
        if escolha == 2:
            escola = db.read_excel()
            
            
BancoDeDadosEscola()
