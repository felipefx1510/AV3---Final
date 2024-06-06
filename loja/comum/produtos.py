from os import system
from tabulate import tabulate
from time import sleep
from db import jogos_ativos as db_jogos_ativos, pesquisar_jogos as db_pesquisar_jogos, comprar_jogo as db_comprar_jogo, biblioteca as db_biblioteca

def listar_jogos():
    system('cls')
    print('Listando jogos...')
    sleep(1)
    jogos = db_jogos_ativos()
    cabecalho = ["ID", "Nome", "Gênero", "Preço", "Estado"]
    if jogos:
        print(tabulate(jogos, headers=cabecalho, tablefmt="grid", maxcolwidths=[None, None, None, None, 10]))  # Limita a coluna "Estado" a 10 caracteres
    else:
        print('Nenhum jogo encontrado.')
        sleep(1)
        
def pesquisar_jogo(nome):
    print('Pesquisando jogos...')
    jogos = db_pesquisar_jogos(nome)
    if jogos:
        cabecalho = ["ID", "Nome", "Gênero", "Preço", "Estado"]
        print(tabulate(jogos, headers=cabecalho, tablefmt="grid", maxcolwidths=[None, None, None, None, 10]))  # Limita a coluna "Estado" a 10 caracteres
    else:
        print('Nenhum jogo encontrado.')
        
def comprar_jogo(id_jogo, id_usuario):
    db_comprar_jogo(id_jogo, id_usuario)
    
def biblioteca(id_usuario):
    jogos = db_biblioteca(id_usuario)
    cabecalho = ["Nome", "Gênero", "Preço"]
    if jogos:
        print(tabulate(jogos, headers=cabecalho, tablefmt="grid", maxcolwidths=[None, None, None]))  # Limita a coluna "Estado" a 10 caracteres
    else:
        print('Nenhum jogo encontrado.')
        sleep(1)