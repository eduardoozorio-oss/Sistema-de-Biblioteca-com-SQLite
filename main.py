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



# Listar livros
def listar_livros():
    con = conectar()
    cur = con.cursor()

    cur.execute("SELECT * FROM livros")
    livros = cur.fetchall()

    con.close()
    return livros

# Atualizar disponibilidade
def atualizar_disponibilidade(id_livro):
    con = conectar()
    cur = con.cursor()

    cur.execute("SELECT disponivel FROM livros WHERE id = ?", (id_livro,))
    resposta = cur.fetchone()

    if resposta:
        atual = resposta[0]
        novo = "Não" if atual == "Sim" else "Sim"

        cur.execute("UPDATE livros SET disponivel = ? WHERE id = ?", (novo, id_livro))
        con.commit()
    else:
        print("Livro não encontrado.")

    con.close()

# Remover livro
def remover_livro(id_livro):
    con = conectar()
    cur = con.cursor()

    cur.execute("DELETE FROM livros WHERE id = ?", (id_livro,))
    con.commit()
    con.close()