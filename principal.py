import sys
import sqlite3

#Globais
conn = sqlite3.connect("alunos.db")
cursor = conn.cursor()
estudantes = []
notas = []
print("Bem-vindo ao Cadastro de Alunos")
nAlunos = int(input("Digite o número de alunos: "))

#Funções
def linha():
    print("\n")

def adc_estudante():
    for i in range(nAlunos):
        estudantes.append(input("Digite o nome do estudante: "))
        notas.append(0.00)
    return estudantes, notas

def dar_nota_geral():
    for i in range(nAlunos):
        nota = float(input("Digite a nota para %s: " % estudantes[i]))
        notas[i] = "%s - Nota: %.2f" % (estudantes[i], nota)
    return estudantes, notas

def mudar_nota():
    indice = estudantes.index(input("Digite o nome do aluno: "))
    nota = float(input("Digite a nota para %s: " % estudantes[indice]))
    notas[indice] = "%s - Nota: %.2f" % (estudantes[indice], nota)
    linha()
    print(notas[indice])
    return notas

def inicio():
    while True:
        opcao = int(input("1 - Adicionar estudantes\n2 - Dar notas a todos estudantes\n3 - Mudar nota de um único estudante\n4 - Listar todos os estudantes com notas\n5 - Sair\nResposta: "))

        if(opcao == 1):
            linha()
            adc_estudante()
            linha()
            print(estudantes)
            linha()
        elif(opcao == 2):
            linha()
            dar_nota_geral()
            linha()
            print(notas)
            linha()
        elif(opcao == 3):
            linha()
            mudar_nota()
            linha()
        elif(opcao == 4):
            linha()
            print(notas)
            linha()
        elif(opcao == 5):
            sys.exit(0)
        else:
            print("\nOpção inválida. Digite novamente\n")
            continue

inicio()
