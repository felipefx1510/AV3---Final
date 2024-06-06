import sqlite3
from os import path
from functools import wraps
import services

def conexao_db(func):
    def wrapper(*args, **kwargs):
        caminho = path.join(path.dirname(__file__), '..', 'banco_de_dados.sqlite')
        conexao = sqlite3.connect(caminho)
        cursor = conexao.cursor()
        
        resultado = func(cursor, conexao, *args, **kwargs)
        conexao.close()
        
        return resultado
        
    return wrapper

@conexao_db
def adicionar_jogo(cursor, conexao, jogo, genero, preco):
    
    cursor.execute(
        """INSERT INTO jogos (nome, genero, preco) 
        VALUES (?, ?, ?)""", (jogo, genero, preco)
    )
    conexao.commit()
    
    
@conexao_db
def excluir_jogo(cursor, conexao, id_jogo):
    
    cursor.execute(
        """DELETE FROM jogos WHERE id_jogo = ?""", (id_jogo,)
    )
    conexao.commit()
    
@conexao_db
def pesquisar_jogos(cursor, conexao, nome):
    
    return cursor.execute(
        """SELECT * FROM jogos WHERE nome = ?""", (nome,)
    ).fetchall()
    
@conexao_db
def lista_jogos(cursor, conexao):
    
    return cursor.execute(
     """SELECT * FROM jogos"""
     ).fetchall()


@conexao_db
def comprar_jogo(cursor, conexao, id_jogo, id_usuario):
    
    cursor.execute(
        """INSERT INTO compras (id_usuario, id_jogo) 
        VALUES (?, ?)""", (id_usuario, id_jogo)
    )
    conexao.commit()
    
@conexao_db
def desativar_jogo(cursor, conexao, id_jogo):    
    cursor.execute(
        """UPDATE jogos SET estado = 'Inativo' WHERE id_jogo = ?""", (id_jogo,)
    )
    conexao.commit()
    
@conexao_db
def ativar_jogo(cursor, conexao, id_jogo):    
    cursor.execute(
        """UPDATE jogos SET estado = 'Ativo' WHERE id_jogo = ?""", (id_jogo,)
    )
    conexao.commit()
    
@conexao_db
def biblioteca(cursor, conexao, id_usuario):
    
    return cursor.execute(
        """SELECT jogos.nome, jogos.genero, jogos.preco 
        FROM jogos 
        JOIN compras ON jogos.id_jogo = compras.id_jogo 
        WHERE compras.id_usuario = ?""", (id_usuario,)
    ).fetchall()
    
@conexao_db
def jogos_ativos(cursor, conexao):
    
    return cursor.execute(
        """SELECT * FROM jogos WHERE estado = 'Ativo'"""
    ).fetchall()

# @conexao_db
# def futuro_join(cursor, conexao):
    
#     return cursor.execute(
#         """SELECT * FROM jogos 
#         JOIN compras ON jogos.id_jogo = compras.id_jogo"""
#     ).fetchall()