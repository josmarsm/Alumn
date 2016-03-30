### Importações ###
from tkinter import *
import sqlite3

#### Definições da Aplicação Principal ###
janela = Tk()
janela.title("Alunos 2000")
janela.geometry("383x400")
janela.resizable(FALSE, FALSE)

### Definicões de outras telas ###
def adc():
    adc = Tk()
    adc.title("Adicionar alunos")
    adc.geometry("400x400")
    adc.resizable(FALSE, FALSE)

def dele():
    dele = Tk()
    dele.title("Deletar aluno")
    dele.geometry("400x400")
    dele.resizable(FALSE, FALSE)

def mudar():
    mudar = Tk()
    mudar.title("Mudar nota de aluno")
    mudar.geometry("400x400")
    mudar.resizable(FALSE, FALSE)

def expo():
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

### Globais ###
conn = sqlite3.connect("alunos.db")
cursor = conn.cursor()

#### Funções ###
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

### Objetos ###
lblTitulo = Label(janela, text="Alunos 2000")
btnAdc = Button(janela, text="Adicionar alunos", command=adc)
btnDel = Button(janela, text="Deletar aluno", command=dele)
btnMudar = Button(janela, text="Mudar nota", command=mudar)
btnExportar = Button(janela, text="Exportar", command=expo)

### Posicionamento dos Objetos ###
lblTitulo.grid(row=0, padx=151, columnspan=5)
btnAdc.grid(row=1, column=0)
btnDel.grid(row=1, column=1)
btnMudar.grid(row=1, column=2)
btnExportar.grid(row=1, column=3)

janela.mainloop()
