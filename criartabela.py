import sqlite3

conn = sqlite3.connect("alunos.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE alunos (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    nota TEXT NOT NULL
);
""")

print("Tabela criada")
conn.close()
