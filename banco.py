import sqlite3
import bcrypt


# Cria a tabela 'usuarios' se ela nao exister em dados.db, com as colunas: id, email e senha 
def criar_tabela():
    conexao = sqlite3.connect('dados.db')
    cusor = conexao.cursor()

    cusor.execute('CREATE TABLE IF NOT EXISTS usuarios ('
                  'id INTEGER PRIMARY KEY AUTOINCREMENT,'
                  'email TEXT UNIQUE,'
                  'senha TEXT'
                  ')')
    conexao.commit()

    cusor.close()
    conexao.close()

# Insere o email e senha no banco, a senha ja vai criptografada para o banco.
def inserir_usuario(email, senha):
    conexao = sqlite3.connect('dados.db')
    cusor = conexao.cursor()

    salt = bcrypt.gensalt()
    senha_hash = bcrypt.hashpw(senha.encode('utf-8'), salt)

    cusor.execute('INSERT INTO usuarios (email, senha) VALUES (?, ?)', (email, senha_hash.decode('utf-8')))
    conexao.commit()

    cusor.close()
    conexao.close()

# Verifica se ja existe um email no banco de dados.
def verifica_email(email):
    conexao = sqlite3.connect('dados.db')
    cursor = conexao.cursor()

    cursor.execute('SELECT * FROM usuarios WHERE email = ?', (email,))
    registro = cursor.fetchone()

    cursor.close()
    conexao.close()

    if registro is not None:
        return True
    else:
        return False