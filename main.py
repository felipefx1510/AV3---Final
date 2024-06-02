import tkinter as tk
from tkinter import messagebox
from services import cadastro_comum, autenticacao
from loja import administrador, pagina_inicial
from db import create_table, criar_adm

create_table()
criar_adm()

def cadastro():
    email = email_entry.get()
    senha = senha_entry.get()
    
    if not email or not senha:
        messagebox.showerror("Erro", "Email e senha são obrigatórios!")
        return
    
    resultado = cadastro_comum(email, senha)
    
    if resultado:
        messagebox.showinfo("Cadastro", "Usuário cadastrado com sucesso!")
    else:
        messagebox.showerror("Erro", "Falha no cadastro!")


def autenticar():
    email = email_entry.get()
    senha = senha_entry.get()

    if not email or not senha:
        messagebox.showerror("Erro", "Email e senha são obrigatórios!")
        return

    nivel = autenticacao(email, senha)
    if nivel is None:
        messagebox.showerror("Erro", "Email ou senha incorretos!")
        return
    elif nivel == 1:
        messagebox.showinfo("Autenticação", "Você é um usuário comum!")
        root.destroy()
        pagina_inicial()
    else:
        messagebox.showinfo("Autenticação", "Você é um administrador!")
        root.destroy()
        administrador()
        
root = tk.Tk()
root.title("Ninja Games")

# Welcome label
label = tk.Label(root, text="Olá, seja bem-vindo ao Ninja Games!")
label.pack()

# Email label and entry
email_label = tk.Label(root, text="Email:")
email_label.pack()
email_entry = tk.Entry(root)
email_entry.pack()

# Password label and entry
password_label = tk.Label(root, text="Senha:")
password_label.pack()
senha_entry = tk.Entry(root, show="•")
senha_entry.pack()

# Login button
login_button = tk.Button(root, text="Entrar", command=autenticar)
login_button.pack()

cadastro_button = tk.Button(root, text="Cadastrar", command=cadastro)
cadastro_button.pack()

root.mainloop()