import sqlite3 as conector
import random
import string

conexao = conector.connect('C:/Users/Usuario/Documents/teste/meubanco10.db')
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

    def inserir_dados(nome_aluno, matricula, id_disciplina, nome_disciplina, nota1, nota2, nota3):
        media = (nota1 + nota2 + nota3) / 3
        comando = '''INSERT INTO aluno VALUES (:matricula, :nome_aluno);'''
        cursor.execute(comando, {"matricula": matricula, "nome_aluno": nome_aluno})
        conexao.commit()

        comando = '''INSERT INTO disciplina VALUES (:id_disciplina, :nome_disciplina);'''
        cursor.execute(comando, {"id_disciplina": id_disciplina, "nome_disciplina": nome_disciplina})
        conexao.commit()

        comando = '''INSERT INTO resultados VALUES (:aluno_id, :disciplina_id, :nota1, :nota2, :nota3, :media);'''
        cursor.execute(comando, {"aluno_id": matricula, "disciplina_id": id_disciplina, "nota1": nota1, "nota2": nota2, "nota3": nota3, "media": media})
        conexao.commit()
        print(">>> Dados adicionados com sucesso!")


    def excluir_dados(matricula):
        comando = '''DELETE FROM aluno WHERE matricula = :matricula;'''
        cursor.execute(comando, {"matricula": matricula})
        conexao.commit()

        comando = '''DELETE FROM resultados WHERE aluno_id = :aluno_id;'''
        cursor.execute(comando, {"aluno_id": matricula})
        conexao.commit()
        print(">>> Dados apagados com sucesso!")


    def alterar_dados(matricula, nome_aluno):
        cursor.execute("UPDATE aluno SET nome_aluno = ? WHERE matricula = ?", (nome_aluno, matricula))
        conexao.commit()
        print(">>> Dados atualizados com sucesso!")

class BancoDeDados:
    def todos_os_alunos():
        cursor.execute("SELECT nome_aluno FROM aluno;")
        selecao_resultado = cursor.fetchall()
        if not selecao_resultado:
            print(">>> Não há dados de alunos a serem visualizados!")
        else:
            print('>>> Lista de todos os alunos:')
            for dado in selecao_resultado:
                print(dado)


    def todos_as_disciplinas():
        cursor.execute("SELECT nome_disciplina FROM disciplina;")
        selecao_resultado = cursor.fetchall()
        if not selecao_resultado:
            print(">>> Não há dados de disciplinas a serem visualizados!")
        else:
            print('>>> Lista de todos as disciplinas')
            for dado in selecao_resultado:
                print(dado)


    def all_medias_alunos():
        cursor.execute("SELECT aluno.nome_aluno, resultados.media "
                       "FROM aluno JOIN resultados "
                       "ON aluno.matricula = resultados.aluno_id ")
        selecao_resultado = cursor.fetchall()
        if not selecao_resultado:
            print(">>> Não há dados de alunos e médias a serem visualizados!")
        else:
            print(">>> Lista de todos os alunos e suas médias!")
            for dado in selecao_resultado:
                print(dado)

try:
    while True:
        matricula = ''.join(random.choices(string.digits, k=12))
        id_disciplina = ''.join(random.choices(string.digits, k=6))
        print('*-' * 15)
        print('---- Meu banco de dados ----')
        print('*-' * 15)
        print('>>> O que você quer fazer?'
            '\n[ 1 ] - Inserir dados\n[ 2 ] - Excluir dados\n[ 3 ] - Alterar dados'
            '\n[ 4 ] - Lista de todos os alunos\n[ 5 ] - Lista de todos as disciplinas\n[ 6 ] - Lista todas as medias\n[ 7 ] - Sair')
        escolha = int(input('>>> Escolha uma opção:'))
        if escolha == 1:
            while True:
                nome_aluno = str(input('Qual o nome do aluno?')).strip()
                if len(nome_aluno) > 0 and nome_aluno.isalpha():
                    break
                else:
                    print('-- Nome invalido! Tente novamente')   
            while True:
                nome_disciplina = str(input('Nome da disciplina:')).strip()
                if len(nome_disciplina) > 0 and nome_disciplina.isalpha():
                    break
                else:
                    print('-- Disciplina invalida! Tente novamente')
            while True:  
                nota1 = float(input('Informe a 1ª nota: '))
                nota2 = float(input('Informe a 2ª nota: '))
                nota3 = float(input('Informe a 3ª nota: '))
                if nota1 <= 10 and nota2 <= 10 and nota3 <= 10:
                    break
                else:
                    print('--- Notas invalidas! Tente novamente')
            Aluno.inserir_dados(nome_aluno, matricula, id_disciplina, nome_disciplina, nota1, nota2, nota3)

        elif escolha == 2:
            while True:
                matricula = str(input("Informe a matricula do aluno a ser deletado:")).strip()
                if len(matricula) == 12:
                    break
                else:
                    print('-- Matricula invalida! Tente novamente')
            Aluno.excluir_dados(matricula)

        elif escolha == 3:
            while True:
                matricula = str(input("Informe a matricula do aluno a ser alterado:")).strip()
                if len(matricula) == 12:
                    break
                else:
                    print('-- Matricula invalida! Tente novamente')
            while True:
                nome_aluno = str(input('Qual será o novo nome?')).strip()
                if len(nome_aluno) > 0 and nome_aluno.isalpha():
                    break
                else:
                    print('-- Nome invalido! Tente novamente')   
            Aluno.alterar_dados(matricula, nome_aluno)
                    
        elif escolha == 4:
            BancoDeDados.todos_os_alunos()

        elif escolha == 5:
            BancoDeDados.todos_as_disciplinas()
   
        elif escolha == 6:
            BancoDeDados.all_medias_alunos()

        elif escolha == 7:
            print('>>> Obrigado por utilizar...Até a próxima!')
            break
        else:
            print('Comando invalido! Tente Novamente')
except:
    print("Ocorreu um erro")

cursor.close()
conexao.close()
