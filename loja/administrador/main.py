from .produtos import *
from .usuarios import *
from time import sleep
from os import system
from stdiomask import getpass
import bcrypt
from db import inserir_usuario

def voltando():
    print('Voltando ao menu principal...')
    sleep(1)
    system('cls')
    return

def administrador(): 
    while True:
        print('Seja bem-vindo, administrador, ao sistema do Ninja Games!')
        print('O que desejar fazer hoje?')
        print('1 - Adicionar um jogo.')
        print('2 - Excluir um jogo.')
        print('3 - Listar jogos.')
        print('4 - Desativar jogo no banco de dados.')
        print('5 - Ativar jogo no banco de dados.')
        print('6 - Listar usuarios')
        print('7 - Adicionar um usuário.')
        print('8 - Excluir um usuário.')

        opcao = int(input())
        if opcao == 1:
            while True:
                jogo = input('Digite o nome do jogo que você deseja adcionar: ')
                genero = input('Digite o gênero do jogo adicionado: ') 
                preco = input('Digite o preço do jogo adicionado: ')
                add_jogo(jogo, genero, preco)
                print('Jogo adicionado com sucesso!')
                opcao = input('Deseja adicionar outro jogo? (S/N)').upper()
                
                if opcao == 'S':
                    continue
                elif opcao == 'N':
                    voltando()
                    break
                else:
                    print('Opção inválida!')

        elif opcao == 2:
            while True:
                id = input('Digite o ID do jogo que você deseja excluir: ')
                remover_jogo(id)
                print('Jogo removido com sucesso!')
                opcao = input('Deseja excluir outro jogo? (S/N)').upper()
                if opcao == 'S':
                    continue
                elif opcao == 'N':
                    voltando()
                    break
                else:
                    print('Opção inválida!')
                
        elif opcao == 3:
            while True:
                listar_jogos()
                break
                
        elif opcao == 4:
            while True:
                id = input('Digite o ID do jogo que você deseja desativar: ')
                desativar_jogo(id)
                print('Jogo desativado com sucesso!')
                opcao = input('Deseja desativar outro jogo? (S/N)').upper()
                if opcao == 'S':
                    continue
                elif opcao == 'N':
                    voltando()
                    break
                else:
                    print('Opção inválida!')
                    
        elif opcao == 5:
            while True:
                id = input('Digite o ID do jogo que você deseja ativar: ')
                ativar_jogo(id)
                print('Jogo ativado com sucesso!')
                opcao = input('Deseja ativar outro jogo? (S/N)').upper()
                if opcao == 'S':
                    continue
                elif opcao == 'N':
                    voltando()
                    break
                else:
                    print('Opção inválida!')
                    
        elif opcao == 6:
            while True:
                system('cls')
                print('Listando usuários...')
                sleep(1)
                listar_usuarios()
                sleep(1)
                break
                
        elif opcao == 7:
            while True:
                email = input('Digite o email do usuário que deseja adicionar: ')
                senha = getpass('Digite a senha do usuário que deseja adicionar: ', mask='•')
                nivel = input('Digite o nível do usuário que deseja adicionar: ')
                senha_criptografada = bcrypt.hashpw(senha.encode(), bcrypt.gensalt())
                inserir_usuario(nivel, email, senha_criptografada)
                print('Usuário adicionado com sucesso!')
                opcao = input('Deseja adicionar outro usuário? (S/N)').upper()
                if opcao == 'S':
                    continue
                elif opcao == 'N':
                    voltando()
                    break
                else:
                    print('Opção inválida!')
            
        elif opcao == 8:
            while True:
                id = input('Digite o ID do usuário que você deseja excluir: ')
                excluir_usuario(id)
                print('Usuário removido com sucesso!')
                opcao = input('Deseja excluir outro usuário? (S/N)').upper()
                if opcao == 'S':
                    continue
                elif opcao == 'N':
                    voltando()
                    break
                else:
                    print('Opção inválida!')
                

            
            
            