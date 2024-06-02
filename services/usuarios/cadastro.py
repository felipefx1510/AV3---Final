import bcrypt
from stdiomask import getpass
from db import inserir_usuario, verificar_email

def cadastro_comum(email, senha):
    print('-'*30)
    print('Cadastro')
    print('-'*30)
    nivel_acesso = 1
    senha_criptografada = bcrypt.hashpw(senha.encode(), bcrypt.gensalt())
    
    if verificar_email(email):
        print('Email já cadastrado!')
        return False
    
    inserir_usuario(nivel_acesso, email, senha_criptografada)
    print('Usuário cadastrado com sucesso!')
    return True

def cadastro_adm():
    while True:
        print('-'*30)
        print('Cadastro')
        print('-'*30)
        nivel_acesso = int(input('Digite o nível de acesso do usuário: '))
        email = input('Digite o email desejado:')
        senha = getpass('Digite a senha desejada: ', mask='•')
        senha_criptografada = bcrypt.hashpw(senha.encode(), bcrypt.gensalt())
        
        inserir_usuario(nivel_acesso, email, senha_criptografada)
        
        print('Usuário cadastrado com sucesso!')
        while True:
            opcao = int(input('Deseja cadastrar outro usuário?\n1.Sim\n2.Não\n'))
            if opcao == 1:
                break
            elif opcao == 2:
                return