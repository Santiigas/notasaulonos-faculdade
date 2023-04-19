import sqlite3 as conector
import random
import string

conexao = conector.connect('C:/Users/Usuario/Documents/teste/meubanco8.db')
#conexao.execute("PRAGMA foreign_keys = on")
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

class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        pass
    
    def InserirDados(self, nome_aluno, matricula, nome_disciplina, id_disciplina, nota1, nota2, nota3):
        media = (nota1 + nota2 + nota3) / 3
        try:
            comando = '''INSERT INTO aluno VALUES (:matricula, :nome_aluno);'''
            cursor.execute(comando, {"matricula": matricula, "nome_aluno": nome_aluno})
            conexao.commit()
        except Exception as erro:
            print(erro)

        try:
            comando = '''INSERT INTO disciplina VALUES (:id_disciplina, :nome_disciplina);'''
            cursor.execute(comando, {"id_disciplina": id_disciplina, "nome_disciplina": nome_disciplina})
            conexao.commit()
        except Exception as erro:
            print(erro)

        try:
            comando = '''INSERT INTO resultados VALUES (:aluno_id, :disciplina_id, :nota1, :nota2, :nota3, :media);'''
            cursor.execute(comando, {"aluno_id": matricula, "disciplina_id": id_disciplina, "nota1": nota1, "nota2": nota2, "nota3": nota3, "media": media})
            conexao.commit()
        except Exception as erro:
            print(erro)

    def ExcluirDados(self, matricula):
        try:
            comando = '''DELETE FROM aluno WHERE matricula = :matricula;'''
            cursor.execute(comando, {"matricula": matricula})

            comando = '''DELETE FROM resultados WHERE aluno_id = :aluno_id;'''
            cursor.execute(comando, {"aluno_id": matricula})
            conexao.commit()
        except Exception as erro:
            print(erro)         

    def AlterarDados(self, matricula, nome_aluno):
        try:
            cursor.execute("UPDATE aluno SET nome_aluno = ? WHERE matricula = ?", (nome_aluno, matricula))
            conexao.commit()
        except Exception as erro:
            print(erro)

    def Finalizar(self):
        pass

while True:
    matricula = ''.join(random.choices(string.digits, k=12))
    id_disciplina = ''.join(random.choices(string.digits, k=6))
    print('*-' * 15)
    print('\n---- Meu banco de dados ----')
    print('*-' * 15)
    print('>>> O que você quer fazer?\n[ 1 ] - Inserir dados\n[ 2 ] - Excluir\n[ 3 ] - Alterar\n[ 4 ] - Sair' )
    print('*-' * 15)
    escolha = int(input('-- Escolha uma opção:'))
    if escolha == 1:
        while True:
            nome_aluno = str(input('Qual o nome do aluno?'))
            if len(nome_aluno) > 0 and nome_aluno.isalpha():
                pass
            else:
                print('-- Nome invalido! Tente novamente')   
            nome_disciplina = str(input('Nome da disciplina:'))
            if len(nome_disciplina) > 0 and nome_disciplina.isalpha():
                pass
            else:
                print('-- Disciplina invalida! Tente novamente')  
            nota1 = float(input('Informe a 1ª nota: '))
            nota2 = float(input('Informe a 2ª nota: '))
            nota3 = float(input('Informe a 3ª nota: '))
            Aluno.InserirDados(nome_aluno, matricula, nome_disciplina, id_disciplina, nota1, nota2, nota3)

    elif escolha == 2:
        while True:
            matricula = float(input("Informe a matricula do aluno a ser deletado:"))
            Aluno.ExcluirDados(matricula)

    elif escolha == 3:
        while True:
            matricula = float(input("Informe a matricula do aluno a ser alterado:"))
            nome_aluno = str(input('Qual será o novo nome?'))
            if len(nome_aluno) > 0 and nome_aluno.isalpha():
                Aluno.AlterarDados(matricula, nome_aluno)
                
    elif escolha == 4:
        Aluno.Finalizar()
        break                     
    else:
        print('Comando invalido! Tente Novamente')
cursor.close()
conexao.close()
