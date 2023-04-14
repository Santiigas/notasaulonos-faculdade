import sqlite3 as conector
import random
import string
matricula = ''.join(random.choices(string.digits, k=12))

conexao = conector.connect('C:/Users/Usuario/Documents/teste/meubanco11.db')
conexao.execute("PRAGMA foreign_keys = on")
cursor = conexao.cursor()

try:
    cursor.execute('''CREATE TABLE aluno (
                    cpf_aluno  INTEGER   PRIMARY KEY,
                    nome_aluno TEXT (50),
                    matricula  INTEGER);''')


    cursor.execute('''CREATE TABLE disciplina (
                    id_disciplina        INTEGER   PRIMARY KEY,
                    nome_disciplina   TEXT (40);''')

                        
    cursor.execute('''CREATE TABLE resultados (
                    aluno_id       INTEGER REFERENCES aluno (cpf_aluno),
                    disciplina_id INTEGER REFERENCES disciplina (id_disciplina),
                    nota1                    REAL,
                    nota2                    REAL,
                    nota3                    REAL,
                    media                    REAL);''')
except Exception as erro:
    print(erro)

print('*-' * 15)
print('---- Meu banco de dados ----')
print('*-' * 15)
print('>>> O que você quer fazer?\n[ 1 ] - Inserir dados\n[ 2 ] - Excluir\n[ 3 ] - Alterar')
print('*-' * 15)
escolha = int(input('-- Escolha uma opção:'))

if escolha == 1:
    while True:
        nome_aluno = str(input('Qual o nome do aluno?'))
        nota1 = float(input("Informe a primeira nota:"))
        nota2 = float(input("Informe a segunda nota:"))
        nota3 = float(input("Informe a terceira nota:"))
        media = (nota1 + nota2 + nota3) / 3
        if len(nome_aluno) > 0 and nome_aluno.isalpha():
            try:
                comando = '''INSERT INTO aluno VALUES (:cpf_aluno, :nome_aluno, :matricula);'''
                cursor.execute(comando, {"cpf_aluno": 122222, "nome_aluno": nome_aluno, "matricula": matricula})
                conexao.commit()

                comando = '''INSERT INTO disciplina VALUES (":id_disciplina", ":nome_disciplina");'''
                cursor.execute(comando, {"id_disciplina": 5555, "nome_disciplina": "eusanti"})
                conexao.commit()

                comando = '''INSERT INTO resultados VALUES (":nota1, :nota2, :nota3, :media);'''
                cursor.execute(comando, {"nota1":nota1, "nota2":nota2, "nota3":nota3, "media": media})
                conexao.commit()

                break    
            except Exception as erro:
                print(erro)
        else:
            print('>>> Valores digitados invalidos! Tente novamente')               
elif escolha == 2:
    while True:
        cpf_aluno = float(input("Informe o CPF do aluno a ser deletado:"))
        if len(cpf_aluno) == 11:
            try:
                comando = '''DELETE FROM aluno WHERE cpf_aluno = :cpf_aluno;'''
                cursor.execute(comando, {"cpf_aluno": cpf_aluno})

                conexao.commit() 
            except Exception as erro:
                print(erro)         
        print('>>> Valores digitados invalidos! Tente novamente')  
elif escolha == 3:
    while True:
        nome_aluno = str(input('Qual o nome do aluno?'))
        if len(nome_aluno) > 0 and nome_aluno.isalpha():    
            try:
                comando = '''UPDATE aluno SET nome_aluno = :nome_aluno;'''
                cursor.execute(comando, {"nome_aluno": nome_aluno})
                conexao.commit() 
                break
            except Exception as erro:
                print(erro)
        else:
            print('>>> Valores digitados invalidos! Tente novamente')                      
else:
    print('Comando invalido! Tente Novamente ')

cursor.close()
conexao.close()