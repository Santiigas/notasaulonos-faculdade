import sqlite3 as conector
import random
import string
matricula = ''.join(random.choices(string.digits, k=12))

conexao = conector.connect('C:/Users/Usuario/Documents/teste/meubanco13.db')
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
while True:
    print('*-' * 15)
    print('---- Meu banco de dados ----')
    print('*-' * 15)
    print('>>> O que você quer fazer?\n[ 1 ] - Inserir dados\n[ 2 ] - Excluir\n[ 3 ] - Alterar\n[ 4 ] - Sair' )
    print('*-' * 15)
    escolha = int(input('-- Escolha uma opção:'))
    if escolha == 1:
        while True:
            nome_aluno = str(input('Qual o nome do aluno?'))
            cpf_aluno = int(input("Informe o CPF do aluno:"))
            if len(nome_aluno) > 0 and nome_aluno.isalpha():
                    try:
                        comando = '''INSERT INTO aluno VALUES (:cpf_aluno, :nome_aluno, :matricula);'''
                        cursor.execute(comando, {"cpf_aluno": cpf_aluno, "nome_aluno": nome_aluno, "matricula": matricula})
                        conexao.commit()
                        print(">>>> Dados adicionados com sucesso!")
                        break    
                    except Exception as erro:
                        print(erro)
            else:
                print('>>> Valores digitados invalidos! Tente novamente')               
    elif escolha == 2:
        while True:
            cpf_aluno = float(input("Informe o CPF do aluno a ser deletado:"))
            try:
                comando = '''DELETE FROM aluno WHERE cpf_aluno = :cpf_aluno;'''
                cursor.execute(comando, {"cpf_aluno": cpf_aluno})
                conexao.commit()
                print(">>> Dados apagados com sucesso!")
                break
            except Exception as erro:
                print(erro)         
                print('>>> Valores digitados invalidos! Tente novamente')  
    elif escolha == 3:
        while True:
            cpf_aluno = float(input("Informe o CPF do aluno a ser alterado:"))
            nome_aluno = str(input('Qual será o novo nome?'))
            if len(nome_aluno) > 0 and nome_aluno.isalpha():    
                try:
                    cursor.execute("UPDATE aluno SET nome_aluno = ? WHERE cpf_aluno = ?", (nome_aluno, cpf_aluno))
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

'''Minha ideia no inicio era add todos os dados em todas as tabelas, mas estava dando muitos erros de chaves etc.
Acredito que tenha encontrado a solução, mas resolvi deixar somente na tabela alunos.

Outro ponto que está falando é colocar uma verificação de CPF por meio de uma função e add classes.
Também irei trocar a chave primaria para matricula, já que está com o cpf, e isso a longo prazo não iria funcionar bem!

Irei realizar mais atulizações durante a semana, mas acho que o que eu fiz já resolve a atividade haha, valeu professor'''