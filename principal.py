import sqlite3 as conector
import random
import string
matricula = ''.join(random.choices(string.digits, k=12))
conexao = conector.connect('C:/Users/alunoti/Desktop/meubanco2.db')
cursor = conexao.cursor()

try:
    cursor.execute('''CREATE TABLE aluno (
                    cpf_aluno  INTEGER   PRIMARY KEY,
                    nome_aluno TEXT (50),
                    matricula  INTEGER);''')


    cursor.execute('''CREATE TABLE disciplina (
                    id_disciplina        INTEGER   PRIMARY KEY,
                    [nome_disciplina ]   TEXT (40) NOT NULL,
                    professor_disciplina TEXT);''')

                        
    cursor.execute('''CREATE TABLE resultados (
                    aluno_indentifacao       INTEGER REFERENCES aluno (cpf_aluno),
                    disciplina_identificador INTEGER REFERENCES disciplina (id_disciplina),
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
                cursor.execute(comando, {"cpf_aluno": "null", "nome_aluno": nome_aluno, "matricula": matricula, })

                comando = '''INSERT INTO resultados VALUES (:nota1, :nota2, :nota3, :media),'''
                cursor.execute(comando, {"nota1":nota1, "nota2":nota2, "nota3":nota3, "media": media})

                conexao.commit()      
            except Exception as erro:
                print(erro)
        else:
            print('Valores digitados invalidos')
                  
elif escolha == 2:
    try:
        comando = '''DELETE FROM aluno where matricula = ?  ;'''
        cursor.execute(comando, {"nome_aluno": "Santiago", })
    except Exception as erro:
        print(erro)
    
    conexao.commit()      
            
elif escolha == 3:
    while True:
        nome_aluno = str(input('Qual o nome do aluno?'))
        if len(nome_aluno) > 0 and nome_aluno.isalpha():    
            try:
                comando = '''UPDATE aluno SET nome_aluno = :nome_aluno ;'''
                cursor.execute(comando, {"nome_aluno": nome_aluno })
            except Exception as erro:
                print(erro)
        else:
            print('Valores digitados invalidos')

            conexao.commit()      
                        
else:
    print('Comando invalido! Tente Novamente ')

cursor.close()
conexao.close()