from stdiomask import getpass
from db import autenticar, conferir_nivel
import bcrypt

aut_email = None

def autenticacao(email, senha):
    global aut_email
    aut_email = email
        
    senha_criptografada = autenticar(email)
        
    if senha_criptografada is None or not bcrypt.checkpw(senha.encode(), senha_criptografada):
        print('Usuário ou senha inválidos')
        return None
    
    nivel = conferir_nivel(email)
    return nivel
    
def id_aut_email():
    return aut_email
            
            
            