import sqlite3
from os import path

def conferir_nivel(email):
    caminho = path.join(path.dirname(__file__), '..', 'banco_de_dados.sqlite')
    conexao = sqlite3.connect(caminho)
    cursor = conexao.cursor()
    
    cursor.execute(
        """SELECT nivel_acesso FROM usuarios
        WHERE email = ?""", (email,)
    )
    nivel_acesso = cursor.fetchone()
    
    conexao.close()
    return nivel_acesso[0] if nivel_acesso else None

def autenticar(email):
    caminho = path.join(path.dirname(__file__), '..', 'banco_de_dados.sqlite')
    conexao = sqlite3.connect(caminho)
    cursor = conexao.cursor()
    
    cursor.execute(
        """SELECT senha FROM usuarios
        WHERE email = ?""", (email,)
    )
    senha_criptografada = cursor.fetchone()
    
    if senha_criptografada is None:
        return None
    else:
        conexao.close()
        return senha_criptografada[0]
    
    