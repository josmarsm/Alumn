import sys
import sqlite3
import io

#Globais
conn = sqlite3.connect("alunos.db")
cursor = conn.cursor()
print("Bem-vindo ao Cadastro de Alunos")

#Funções
def linha():
    print("\n")

def adc_estudante():
    nAlunos = int(input("Digite o número de alunos: "))
    for i in range(nAlunos):
        nome = input("Digite o nome do estudante: ")
        nota = input("Digite a nota para %s: " % nome)
        cursor.execute("""
            INSERT INTO alunos (nome, nota) VALUES (?, ?)""", (nome, nota))
        conn.commit()

def del_estudante():
    id = int(input("Digite o ID do aluno: "))
    cursor.execute("""
        DELETE FROM alunos WHERE id = ?""", (id,))
    conn.commit()
    print("Estudante de ID %i deletado" % id)

def mudar_nota():
    id = int(input("Digite o ID do aluno: "))
    nota = input("Digite a nota para o aluno de ID %i: " % id)
    cursor.execute("""
        UPDATE alunos SET nota = ? WHERE id = ?""", (nota, id))
    conn.commit()
    cursor.execute("""
    SELECT nota FROM alunos;
    """)
    for item in cursor.fetchone():
        linha()
        print("A nota do aluno de ID %i foi alterada para %s" % (id, nota))

def exibir():
    cursor.execute("""
    SELECT * FROM alunos;
    """)
    for linha in cursor.fetchall():
        print(linha)

def exportar():
    with io.open('alunos.sql', 'w') as f:
        for linha in conn.iterdump():
            f.write('%s\n' % linha)
    cursor.execute("""
    SELECT * FROM alunos;
    """)
    with io.open('alunos.txt', 'w') as f:
        for linha in cursor.fetchall():
            linha = str(linha)
            f.write('%s\n' % linha)

def inicio():
    while True:
        opcao = int(input("1 - Adicionar estudantes\n2 - Deletar estudante\n3 - Mudar nota de um único estudante\n4 - Listar todos os estudantes com notas\n5 - Exportar\n6 - Sair\nResposta: "))

        if(opcao == 1):
            linha()
            adc_estudante()
            linha()
        elif(opcao == 2):
            linha()
            del_estudante()
            linha()
        elif(opcao == 3):
            linha()
            mudar_nota()
            linha()
        elif(opcao == 4):
            linha()
            exibir()
            linha()
        elif(opcao == 5):
            linha()
            exportar()
            linha()
        elif(opcao == 6):
            conn.close()
            sys.exit(0)
        else:
            print("\nOpção inválida. Digite novamente\n")
            continue

inicio()
