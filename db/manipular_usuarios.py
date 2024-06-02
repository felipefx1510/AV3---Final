import sqlite3
from os import path


def conexao_db(funcao):
    def wrapper(*args, **kwargs):
        caminho = path.join(path.dirname(__file__), '..', 'banco_de_dados.sqlite')
        conexao = sqlite3.connect(caminho)
        cursor = conexao.cursor()
        resultado = funcao(cursor, *args, **kwargs)
        conexao.commit()
        conexao.close()
        return resultado
    return wrapper

@conexao_db
def verificar_email(cursor, email):
    return cursor.execute(
        """SELECT email FROM usuarios
        WHERE email = ?""", (email,)
    ).fetchone()

@conexao_db
def inserir_usuario(cursor, nivel_acesso, email, senha_criptografada):
    cursor.execute(
        """INSERT INTO usuarios (nivel_acesso, email, senha)
        VALUES (?, ?, ?)""", (nivel_acesso, email, senha_criptografada)
    )
    
@conexao_db
def obter_id(cursor, email):
    return cursor.execute(
        """SELECT id_usuario FROM usuarios WHERE email = ?""", (email,)
    ).fetchone()
    
@conexao_db
def excluir_usuario(cursor, id_usuario):
    cursor.execute(
        """DELETE FROM usuarios WHERE id_usuario = ?""", (id_usuario,)
    )
    
@conexao_db
def listar_usuarios(cursor):
    return cursor.execute(
        """SELECT id_usuario, email FROM usuarios"""
    ).fetchall()

@conexao_db
def pesquisar_usuario(cursor, email):
    return cursor.execute(
        """SELECT * FROM usuarios WHERE email = ?""", (email,)
    ).fetchone()