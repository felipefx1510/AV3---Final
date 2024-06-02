from db import adicionar_jogo, excluir_jogo, ativar_jogo as db_ativar_jogo, desativar_jogo as db_desativar_jogo, lista_jogos as db_lista_jogos
from tabulate import tabulate

def add_jogo(jogo, genero, preco):    
    adicionar_jogo(jogo, genero, preco)
    
def remover_jogo(id_jogo):
    excluir_jogo(id_jogo)
    
def desativar_jogo(id_jogo):
    db_desativar_jogo(id_jogo)

def ativar_jogo(id_jogo):
    db_ativar_jogo(id_jogo)
    
def listar_jogos():
    jogos = db_lista_jogos()
    print(tabulate(jogos, headers=['ID', 'Nome', 'Gênero', 'Preço', 'Estado'], tablefmt='grid'))