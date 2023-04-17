import sqlite3 as conector
import random
import string
matricula = ''.join(random.choices(string.digits, k=12))

conexao = conector.connect('C:/Users/Usuario/Documents/teste/meubanco20.db')
conexao.execute("PRAGMA foreign_keys = on")
cursor = conexao.cursor()

try:
    cursor.execute('''CREATE TABLE aluno (
                        matricula INTEGER PRIMARY KEY,
                        nome_aluno TEXT (50));''')

    cursor.execute('''CREATE TABLE disciplina (
                        id_disciplina INTEGER PRIMARY KEY,
                        nome_disciplina TEXT (40));''')
                            
    cursor.execute('''CREATE TABLE resultados (
                        aluno_id INTEGER REFERENCES aluno (matricula),
                        disciplina_id INTEGER REFERENCES disciplina (id_disciplina),
                        nota1 REAL,
                        nota2 REAL,
                        nota3 REAL,
                        media REAL);''')

except Exception as erro:
    print(erro)
while True:
    matricula = ''.join(random.choices(string.digits, k=12))
    print('*-' * 15)
    print('---- Meu banco de dados ----')
    print('*-' * 15)
    print('>>> O que você quer fazer?\n[ 1 ] - Inserir dados\n[ 2 ] - Excluir\n[ 3 ] - Alterar\n[ 4 ] - Sair' )
    print('*-' * 15)
    escolha = int(input('-- Escolha uma opção:'))
    if escolha == 1:
        while True:
            nome_aluno = str(input('Qual o nome do aluno?'))
            if len(nome_aluno) > 0 and nome_aluno.isalpha():
                    try:
                        comando = '''INSERT INTO aluno VALUES (:matricula, :nome_aluno);'''
                        cursor.execute(comando, {"matricula": matricula, "nome_aluno": nome_aluno})
                        conexao.commit()
                        print(">>>> Dados adicionados com sucesso!")
                        break    
                    except Exception as erro:
                        print(erro)
            else:
                print('>>> Valores digitados invalidos! Tente novamente')               
    elif escolha == 2:
        while True:
            matricula = float(input("Informe a matricula do aluno a ser deletado:"))
            try:
                comando = '''DELETE FROM aluno WHERE matricula = :matricula;'''
                cursor.execute(comando, {"matricula": matricula})
                conexao.commit()
                print(">>> Dados apagados com sucesso!")
                break
            except Exception as erro:
                print(erro)         
                print('>>> Valores digitados invalidos! Tente novamente')  
    elif escolha == 3:
        while True:
            matricula = float(input("Informe a matricula do aluno a ser alterado:"))
            nome_aluno = str(input('Qual será o novo nome?'))
            if len(nome_aluno) > 0 and nome_aluno.isalpha():    
                try:
                    cursor.execute("UPDATE aluno SET nome_aluno = ? WHERE matricula = ?", (nome_aluno, matricula))
                    conexao.commit() 
                    print(">>> Dados atualizados com sucesso!")
                    break
                except Exception as erro:
                    print(erro)
            else:
                print('>>> Valores digitados invalidos! Tente novamente') 
    elif escolha == 4:
        print("Encerrando...")
        print('>>> Obrigado por utilizar!')
        break                     
    else:
        print('Comando invalido! Tente Novamente ')
cursor.close()
conexao.close()
