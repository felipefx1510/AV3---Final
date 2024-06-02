from db import criar_adm, create_table
from loja import administrador, pagina_inicial
from services import *
from time import sleep

create_table()
criar_adm()

while True:
    
    print('Olá, seja bem-vindo ao Ninja Games!')
    print('Aguarde enquanto carregamos o sistema...')

    sleep(1.5)
    while True:
        print('O que deseja fazer?')
        print('1 - Cadastro')
        print('2 - Autenticação')
        sleep(1)
        
        opcao = input('Digite a opção desejada: ')

        if opcao == '1':
            cadastro_comum()
                
        elif opcao == '2':
            nivel = autenticacao()
            if nivel == 1:
                pagina_inicial()
            else:
                print('Você é um administrador!')
                administrador()  
        else:
            print('Opção inválida!')
            continue
        