### Importações ###
from tkinter import *
import sqlite3

#### Definições da Aplicação Principal ###
principal = Tk()
principal.title("Alumn - Principal")
principal.geometry("383x400")
principal.resizable(FALSE, FALSE)

### Definicões de outras telas ###
def adc():
    adc = Tk()
    adc.title("Alumn - Adicionar alunos")
    adc.geometry("400x400")
    adc.resizable(FALSE, FALSE)

    ### Função Adicionar ###
    #O método get() não está funcionando, está inserindo dados em branco
    #no banco de dados
    def adicionar():
        nome = etNome.get()
        nota = etNota.get()
        cursor.execute("""
            INSERT INTO alunos (nome, nota) VALUES (?, ?)""", (nome, nota))
        conn.commit()

    ### Objetos - Adicionar Aluno ###
    lblTitulo = Label(adc, text="Alumn - Adicionar Alunos")
    etNome = Entry(adc)
    etNota = Entry(adc)
    btnAdc = Button(adc, text="Adicionar", commmand=adicionar())

    adc.bind('<Return>', adicionar())

    ### Posicionamento de Objetos - Adicionar Aluno ###
    lblTitulo.grid(row=0, padx=119, columnspan=5)
    etNome.grid(row=1)
    etNota.grid(row=2)
    btnAdc.grid(row=3)

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

### Objeto - Principal ###
lblTitulo = Label(principal, text="Alumn")
btnAdc = Button(principal, text="Adicionar alunos", command=adc)
btnDel = Button(principal, text="Deletar aluno", command=dele)
btnMudar = Button(principal, text="Mudar nota", command=mudar)
btnExportar = Button(principal, text="Exportar", command=expo)

### Posicionamento de Objetos - Principal ###
lblTitulo.grid(row=0, padx=169, columnspan=5)
btnAdc.grid(row=1, column=0, sticky=E)
btnDel.grid(row=1, column=1, sticky=E)
btnMudar.grid(row=1, column=2, sticky=E)
btnExportar.grid(row=1, column=3, sticky=E)

principal.mainloop()
