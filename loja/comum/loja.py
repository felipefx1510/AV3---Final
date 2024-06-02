from .produtos import *
from db import obter_id
from services.usuarios.autenticacao import id_aut_email # Importa a função id_aut_email diretamente

def pagina_inicial():
    while True:
        print('O que deseja fazer?')
        print('1 - Ver jogos disponíveis')
        print('2 - Comprar')
        print('3 - Biblioteca')
        sleep(1)
        
        opcao = input('Digite a opção desejada: ')
        
        if opcao == '1':
            while True:
                listar_jogos()
                break
            
        elif opcao == '2':
            while True:
                id_jogo = input('Digite o ID do jogo que deseja comprar: ')
                id_usuario = obter_id(id_aut_email())[0]
                comprar_jogo(id_jogo, id_usuario)
                print('Jogo comprado com sucesso!')
                break
            
        elif opcao == '3':
            while True:
                id_usuario = obter_id(id_aut_email())[0]
                biblioteca(id_usuario)
                break
        
        else:
            print('Opção inválida!')
            continue