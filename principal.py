import sqlite3 as conector
from tkinter import *
from tkinter import ttk
import random
import string

conexao = conector.connect('C:/Users/Usuario/Documents/teste/meubanco11.db')
cursor = conexao.cursor()

lista_disciplinas = ["Português", "História", "Biologia", "Literatura", "Química", "Matemática", "Física", "Inglês", "Espanhol" ]
motivo = ["Trancamento", "Transferência interna", "Transferência externa"]

def CriarBancoDeDados():
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

def PegarDadosAlunos(parametro):
    try:
        matricula = ''.join(random.choices(string.digits, k=12))
        id_disciplina = ''.join(random.choices(string.digits, k=6))
        if parametro == 1:
            nome = str(entrada_nome_aluno.get())
            disciplina = str(entrada_nome_disciplina.get())
            nota1 = float(entrada_nota1.get())
            nota2 = float(entrada_nota2.get())
            nota3 = float(entrada_nota3.get())
            media = (nota1 + nota2 + nota3) / 3
            if len(nome) > 0 and nome.isalpha():
                if len(disciplina) > 0 and disciplina.isalpha() and disciplina in lista_disciplinas:
                    if nota1 <= 10 and nota2 <= 10 and nota3 <= 10:
                        Aluno.inserir_dados(nome, matricula, id_disciplina, disciplina, nota1, nota2, nota3, media)
                        mensagem['text'] = 'Dados inseridos com sucesso!' 
                    else:
                        mensagem['text'] = 'Notas invalidas! Tente novamente'
                else:
                    mensagem['text'] = 'Disciplina invalida! Tente novamente'
            else:
                mensagem['text'] = 'Nome invalido! Tente novamente'
        elif parametro == 2:
            matricula_alterar= str(entrada_matricula.get())
            novo_nome = str(entrada_novo_nome .get())
            if len(matricula_alterar) == 12 and matricula_alterar.isdigit():
                if len(novo_nome) > 0 and novo_nome.isalpha():
                    Aluno.alterar_dados(matricula_alterar, novo_nome)
                    mensagem['text'] = 'Dados alterados com sucesso!'
                else:
                    mensagem['text'] = 'Novo nome invalido'
            else:
                mensagem['text'] = 'Matricula invalida'
        elif parametro == 3:
            matricula_delete = str(entrada_matricula_delete.get())
            if len(matricula_delete) == 12 and matricula_delete.isdigit():
                Aluno.excluir_dados(matricula_delete)
                mensagem['text'] = 'Dados deletados com sucesso!'
            else:
                mensagem['text'] = 'Matricula invalida!'
        elif parametro == 4:
            BancoDeDados.todos_os_alunos()
            mensagem['text'] = 'Dados de todos os alunos retornados!'
            ResultadoPesquisa()
        elif parametro == 5:
            BancoDeDados.todos_as_disciplinas()
            mensagem['text'] = 'Dados de todas as disciplinas retornados!'
            ResultadoPesquisa()
        elif parametro == 6:
            BancoDeDados.all_medias_alunos()
            mensagem['text'] = 'Dados de todas os alunos e medias retornados!'
            ResultadoPesquisa()
    except Exception as erro:
        print("Ocorreu um erro:",erro)

def ResultadoPesquisa():
    janela2 = Tk()
    janela2.title("Resultado de pesquisa")
    #master.iconbitmap(default="icone.ico")
    janela2.geometry("300x400+560+150")
    janela2.wm_resizable(width=False, height=False)

    botao_voltar = Button(janela2, text="Concluido", command = janela2.destroy)
    botao_voltar.place(width=102, height=33, x=100, y=350)

    dados = Label(janela2, text='0000', font="Arial 12", relief='flat', fg='#020304', bg='#ededed')
    dados.place(width=300, height=350, x=0, y=0)

    janela2.mainloop()

class Aluno:
    def __init__(self, nome_aluno, matricula, id_disciplina, nome_disciplina, nota1, nota2, nota3, media):
        self.nome_aluno = nome_aluno
        self.matricula = matricula

    def inserir_dados(nome_aluno, matricula, id_disciplina, nome_disciplina, nota1, nota2, nota3, media):
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
        try:
            cursor.execute("SELECT nome_aluno FROM aluno;")
            selecao_resultado = cursor.fetchall()
            if not selecao_resultado:
                print(">>> Não há dados de alunos a serem visualizados!")
            else:
                '''O banco de dados retorna uma lista com varias tuplas.
                Cada tupla contem o nome de um aluno.
                O que fiz abaixo foi transformar essas tuplas em listas.
                Ou seja: Lista do banco de dados -contem- varias lista com um nome do aluno cada
                No fim retornamos os dados, ou seja, somente o nome do aluno
                '''
                arquivo = open("todas_os_alunos.txt","w")
                arquivo.write(">>> Lista de todos os alunos:\n")
                for dado in selecao_resultado:
                    dados_lista = list(dado)
                    for aluno in dados_lista:
                        arquivo.write(aluno)
                        arquivo.write("\n")          
                arquivo.close()
        except Exception as erro:
            print(erro)
    def todos_as_disciplinas():
        try:
            cursor.execute("SELECT nome_disciplina FROM disciplina;")
            selecao_resultado = cursor.fetchall()
            if not selecao_resultado:
                print(">>> Não há dados de disciplinas a serem visualizados!")
            else:
                arquivo = open("todas_as_disciplinas.txt","w")
                arquivo.write(">>> Lista de todos as disciplinas:\n")
                for dado in selecao_resultado:
                    dados_lista = list(dado)
                    for disciplina in dados_lista:
                        arquivo.write(disciplina)
                        arquivo.write("\n")
                arquivo.close()
        except Exception as erro:
            print(erro)
    def all_medias_alunos():
        try:
            cursor.execute("SELECT aluno.nome_aluno, resultados.media "
                        "FROM aluno JOIN resultados "
                        "ON aluno.matricula = resultados.aluno_id ")
            selecao_resultado = cursor.fetchall()
            if not selecao_resultado:
                print(">>> Não há dados de alunos e médias a serem visualizados!")
            else:
                arquivo = open("todas_as_medias_e_alunos.txt","w")
                arquivo.write(">>> Lista de todos os alunos e suas medias:\n")
                for dado in selecao_resultado:
                    aluno, media = dado
                    arquivo.write(f"Aluno: {aluno} | Media: {media}")
                    arquivo.write("\n")
            arquivo.close()
        except Exception as erro:
            print(erro)

#criação da janela
janela = Tk()
janela.title("Laçamento de notas de alunos")
#master.iconbitmap(default="icone.ico")
janela.geometry("1100x550+155+70")
janela.wm_resizable(width=False, height=False)

#importação da imagem de fundo
fundo_imagem = PhotoImage(file="modelo.png")

#Label
labelfundo = Label(janela, image=fundo_imagem)
labelfundo.place(x=0, y=0)

#Adicionar Aluno ------------------------------------

#Entradas
entrada_nome_aluno = Entry(janela, justify=LEFT)
entrada_nome_aluno.place(width=231, height=22, x=102, y=135)

entrada_nome_disciplina = ttk.Combobox(janela, values=lista_disciplinas)
entrada_nome_disciplina.place(width=202, height=22, x=131, y=173)

entrada_nota1 = Entry(janela, justify=LEFT)
entrada_nota1.place(width=70, height=22, x=98, y=210)

entrada_nota2 = Entry(janela, justify=LEFT)
entrada_nota2.place(width=70, height=22, x=181, y=210)

entrada_nota3 = Entry(janela, justify=LEFT)
entrada_nota3.place(width=70, height=22, x=263, y=210)

#Botao
botao1 = Button(janela, text="Salvar", relief='raised', command=lambda:PegarDadosAlunos(1))
botao1.place(width=102, height=33, x=138, y=252)

#Alterar aluno ------------------------------------

#Entradas
entrada_matricula = Entry(janela, justify=LEFT)
entrada_matricula.place(width=202, height=22, x=492, y=171)

entrada_novo_nome = Entry(janela, justify=LEFT)
entrada_novo_nome.place(width=187, height=22, x=506, y=210)

#Botao
botao2 = Button(janela, text="Alterar", relief='raised', command=lambda:PegarDadosAlunos(2))
botao2.place(width=102, height=33, x=500, y=252)

#Excluir alunos ------------------------------------

#Entradas
entrada_matricula_delete = Entry(janela, justify=LEFT)
entrada_matricula_delete.place(width=205, height=22, x=850, y=173)

entrada_motivo = ttk.Combobox(janela, values=motivo)
entrada_motivo.place(width=225, height=22, x=831, y=210)

#Botao
botao3 = Button(janela, text="Excluir", relief='raised', command=lambda:PegarDadosAlunos(3))
botao3.place(width=102, height=33, x=861, y=252)

#Consultas ------------------------------------------

botao_consultar_alunos = Button(janela, text="Alunos", relief='raised', command=lambda:PegarDadosAlunos(4))
botao_consultar_alunos.place(width=232, height=32, x=72, y=367)

botao_consultar_disciplinas = Button(janela, text="Disciplinas", relief='raised', command=lambda:PegarDadosAlunos(5))
botao_consultar_disciplinas.place(width=232, height=32, x=72, y=415)

botao_consultar_medias = Button(janela, text="Médias", relief='raised', command=lambda:PegarDadosAlunos(6))
botao_consultar_medias.place(width=232, height=32, x=72, y=464)

#--------------------------------------------------------------
#Mensagens na tela
mensagem = Label(janela, text='', font="Arial 17", relief='flat', fg='#020304', bg='#ededed')
mensagem.place(width=500, height=25, x=500, y=420)

janela.mainloop()
cursor.close()
conexao.close()
