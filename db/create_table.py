import sqlite3
import bcrypt

def conexao_db(func):
    def wrapper(*args, **kwargs):
        conexao = sqlite3.connect('banco_de_dados.sqlite')
        cursor = conexao.cursor()
        
        resultado = func(cursor, conexao, *args, **kwargs)
        conexao.close()
        
        return resultado
    
    return wrapper


@conexao_db
def create_table(cursor, conexao):
    cursor.execute(
    """CREATE TABLE IF NOT EXISTS usuarios (
        id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
        nivel_acesso INTEGER NOT NULL,
        email VARCHAR(255) UNIQUE NOT NULL,
        senha VARCHAR(255) NOT NULL
    );"""
)
    cursor.execute(
    """CREATE TABLE IF NOT EXISTS jogos (
        id_jogo INTEGER PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(255) UNIQUE NOT NULL,
        genero VARCHAR(255) NOT NULL,
        preco VARCHAR(255) NOT NULL,
        estado VARCHAR(255) DEFAULT 'Ativo'
        );"""
)
    cursor.execute(
    """CREATE TABLE IF NOT EXISTS compras (
        id_compra INTEGER PRIMARY KEY AUTOINCREMENT,
        id_usuario INTEGER REFERENCES usuarios(id_usuario),
        id_jogo INTEGER REFERENCES jogos(id_jogo)
    );"""
)
    
#     cursor.execute(
#     """CREATE TABLE IF NOT EXISTS carrinho (
#         id_carrinho INTEGER PRIMARY KEY AUTOINCREMENT,
#         id_usuario INTEGER REFERENCES usuarios(id_usuario),
#         id_jogo INTEGER REFERENCES jogos(id_jogo)
#     );"""
# )    
#     conexao.commit()
    
@conexao_db
def criar_adm(cursor, conexao):
    email = 'adm'
    senha = 'adm'
    nivel_acesso = 2
    senha_criptografada = bcrypt.hashpw(senha.encode(), bcrypt.gensalt())
    cursor.execute(
        """SELECT * FROM usuarios WHERE email = ?""", (email,))
    if cursor.fetchone() is None:
        cursor.execute(
            """INSERT INTO usuarios (nivel_acesso, email, senha)
            VALUES (?, ?, ?)""", (nivel_acesso, email, senha_criptografada)
        )
        conexao.commit()