from db import listar_usuarios as db_listar_usuarios, excluir_usuario as db_excluir_usuario
from os import system
from time import sleep
from tabulate import tabulate

def listar_usuarios():
    usuarios = db_listar_usuarios()
    cabecalho = ["ID", "Email"]
    print(tabulate(usuarios, headers=cabecalho, tablefmt="grid", maxcolwidths=[None, 30]))  # Limita a coluna "Email" a 30 caracteres
        
def excluir_usuario(id_usuario):
    db_excluir_usuario(id_usuario)