### Importações ###
from tkinter import *
import sqlite3

### Globais ###
conn = sqlite3.connect("alunos.db")
cursor = conn.cursor()

def criarTabela():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS alunos (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            nota TEXT NOT NULL
        );
    """)

criarTabela()

#### Definições da Aplicação Principal ###
principal = Tk()
principal.title("Alumn - Principal")
principal.geometry("600x281")
principal.resizable(FALSE, FALSE)

#### Funções ###
def adicionar_estudante():
    nome = etNome.get()
    nota = etNota.get()
    cursor.execute("""
        INSERT INTO alunos (nome, nota) VALUES (?, ?)""", (nome, nota))
    conn.commit()
    lstAlunos.insert(END, (nome, nota))

def deletar_estudante():
    id_aluno = etID.get()
    print(delALuno)
    cursor.execute("""
        DELETE FROM alunos WHERE id=?""", (id_aluno,))
    conn.commit()
    lstAlunos.delete(ANCHOR)

def mudar_nota():
    nova_nota = etNovaNota.get()
    mudar_nota = str(lstAlunos.get(ACTIVE))
    cursor.execute("""
        UPDATE alunos SET nota = ? WHERE id = ?""", (nova_nota, mudar_nota))
    conn.commit()

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

### Widgets - Principal ###
lblTitulo = Label(principal, text="Alumn")
lblNomeNota = Label(principal, text="ID / Nome / Nota")

### Widgets - Adicionar Aluno ###
lblAdicionarAluno = Label(principal, text="Adicionar Aluno")
lblNome = Label(principal, text="Nome do Aluno: ")
lblNota = Label(principal, text="Nota do Aluno: ")
etNome = Entry(principal)
etNota = Entry(principal)
btnAdd = Button(principal, text="Adicionar", command=adicionar_estudante)

### Widgets - Deletar Aluno ###
lblDeletarAluno = Label(principal, text="Deletar Aluno")
lblID = Label(principal, text="ID: ")
etID = Entry(principal, width=10)
btnDel = Button(principal, text="Deletar", command=deletar_estudante)

### Widgets - Mudar Nota ###
lblMudarNota = Label(principal, text="Mudar Nota")
lblNovaNota = Label(principal, text="Nota Nota: ")
etNovaNota = Entry(principal)
btnMudarNota = Button(principal, text="Mudar Nota", command=mudar_nota)

### Widgets - Listar Alunos ###
scrollbar = Scrollbar(principal)
lstAlunos = Listbox(principal, width=35, height=13)
lstAlunos.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=lstAlunos.yview)
lista = cursor.execute("""
    SELECT * FROM alunos;
    """)
for i in lista:
    lstAlunos.insert(END, i)

### Posicionamento de Widgets - Principal ###
lblTitulo.place(x=275)
lblNomeNota.place(x=308, y=30)

### Posicionamento de Widgets - Listar Alunos ####
lstAlunos.place(x=310, y=52)
scrollbar.place()

### Posicionamento de Widgets - Adicionar Aluno ###
lblAdicionarAluno.place(x=100, y=30)
lblNome.place(x=10, y=52)
etNome.place(x=115, y=50)
lblNota.place(x=10, y=82)
etNota.place(x=115, y=80)
btnAdd.place(x=115, y=115)

### Posicionamento de Widgets - Deletar Aluno ###
lblDeletarAluno.place(x=100, y=145)
lblID.place(x=10, y=167)
etID.place(x=50, y=165)
btnDel.place(x=145, y=168)

### Posicionamento de Widgets - Mudar Nota ###
lblMudarNota.place(x=100, y=195)
lblNovaNota.place(x=10, y=217)
etNovaNota.place(x=115, y=215)
btnMudarNota.place(x=115, y=250)

principal.mainloop()
