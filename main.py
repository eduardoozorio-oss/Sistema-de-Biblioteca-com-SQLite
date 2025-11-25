import sqlite3



#Função para conectar ao banco

def conectar():
    return sqlite3.connect("biblioteca.db")
