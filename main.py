import sqlite3



#Função para conectar ao banco

def conectar():
    return sqlite3.connect("biblioteca.db")

# Criar tabela no banco
def criar_tabela():
    con = conectar()
    cur = con.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS livros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            autor TEXT NOT NULL,
            ano INTEGER,
            disponivel TEXT
        )
    """)

    con.commit()
    con.close()

# Cadastrar livro
def cadastrar_livro(titulo, autor, ano):
    con = conectar()
    cur = con.cursor()

    cur.execute("INSERT INTO livros (titulo, autor, ano, disponivel) VALUES (?, ?, ?, 'Sim')",
                (titulo, autor, ano))

    con.commit()
    con.close()