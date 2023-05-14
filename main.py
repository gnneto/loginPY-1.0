import banco, sqlite3, bcrypt
import os, time

def limpar():
    limpar = os.system('cls')
def cadastro():
    limpar()
    print('Cadastro.\n')
    email = input('Email: ')
    senha = input('Senha: ')

    if banco.verifica_email(email):
        print(f'O email "{email}" não esta disponivel para cadastro.\n\n')
        time.sleep(2)
    else:
        banco.inserir_usuario(email,senha)
        print('Usuario cadastrado com sucesso.\n\n')
        time.sleep(2)

def login():
    limpar()
    print('Login\n')
    email = input('Email: ')
    senha = input('Senha: ')

    conexao = sqlite3.connect('dados.db')
    cursor = conexao.cursor()

    cursor.execute('SELECT * FROM usuarios WHERE email = ?', (email,))
    registro = cursor.fetchone()

    cursor.close()
    conexao.close()

    if registro is not None and bcrypt.checkpw(senha.encode('utf-8'), registro[2].encode('utf-8')):
        print('Login efetuado com sucesso')
        time.sleep(2)
    else:
        print('Email ou senha incorretos.')
        time.sleep(2)

while True:
    
    limpar()
    escUser = input('Painel.\n\nCadastro [1]\nLogin [2]\nSair [3]\n')

    if escUser == '1':
        cadastro()
    elif escUser == '2':
        login()
    elif escUser == '3':
        break
        limpar()
    else:
        print('\nEscolha invalida.\n')
        time.sleep(2)
        limpar()