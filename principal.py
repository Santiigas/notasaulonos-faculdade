import sqlite3 as conector
from tkinter import *
from tkinter import ttk
import random
import string

conexao = conector.connect('C:/Users/Usuario/Documents/teste/meubanco100.db')
cursor = conexao.cursor()

lista_disciplinas = ["Português", "História", "Biologia", "Literatura", "Química", "Matemática", "Física", "Inglês", "Espanhol" ]

def CriarBancoDeDados():
    try:
        cursor.execute('''CREATE TABLE aluno (
                            id_aluno INTEGER PRIMARY KEY,
                            nome_aluno TEXT (50),
                            matricula INTEGER);''')

        cursor.execute('''CREATE TABLE disciplina (
                            id_disciplina INTEGER PRIMARY KEY,
                            nome_disciplina TEXT (40));''')

        cursor.execute('''CREATE TABLE resultados (
                            aluno_id INTEGER REFERENCES aluno (id_aluno),
                            disciplina_id INTEGER REFERENCES disciplina (id_disciplina),
                            nota1 REAL,
                            nota2 REAL,
                            nota3 REAL,
                            media REAL);''')
    except Exception as erro:
        print("Erro na criacão do banco:",erro)

def PegarDadosAlunos(parametro):
    try:
        if parametro == 1:
            id_aluno = ''.join(random.choices(string.digits, k=8))
            nome = str(entrada_nome_aluno.get())
            matricula = str(entrada_nome_matricula.get())
            if len(nome) > 0 and nome.isalpha():
                if len(matricula) > 0:
                    SalvarNoBanco.inserir_dados_aluno(nome, int(matricula), id_aluno)
                    mensagem['text'] = 'Dados inseridos com sucesso!'
                else:
                    mensagem['text'] = 'Matricula invalida! Tente novamente'
            else:
                mensagem['text'] = 'Nome invalido! Tente novamente'

        elif parametro == 2:
            nome = str(entrada_nome_aluno.get())
            matricula = int(entrada_nome_matricula.get())
            id_aluno = str(entrada_id_aluno.get())
            if len(nome) > 0 and nome.isalpha():
                if len(id_aluno) == 8:
                    if len(matricula) > 0:
                        AlterarNoBanco.alterar_dados_aluno(int(id_aluno), nome, matricula)
                        mensagem['text'] = 'Dados alterados com sucesso!'
                    else:
                        mensagem['text'] = 'Matricula invalida! Tente novamente'
                else:
                    mensagem['text'] = 'Id do aluno invalido! Tente novamente'
            else:
                mensagem['text'] = 'Novo nome invalido! Tente novamente'

        elif parametro == 3:
            id_aluno = str(entrada_id_aluno.get())
            if len(id_aluno) == 8:
                ExcluirNoBanco.excluir_dados_aluno(int(id_aluno))
                mensagem['text'] = 'Dados deletados com sucesso!'
            else:
                mensagem['text'] = 'Id do aluno invalido! Tente novamente!'
    except Exception as erro:
        print("Erro na coleta de dados(aluno):",erro)

def PegarDadosDisciplina(parametro):
    try:
        if parametro == 1:
            id_disciplina = ''.join(random.choices(string.digits, k=6))
            disciplina = str(entrada_disciplina.get())
            if len(disciplina) > 0 and disciplina.isalpha():
                SalvarNoBanco.inserir_dados_disciplina(id_disciplina, disciplina)
                mensagem['text'] = 'Dados inseridos com sucesso!' 
            else:
                mensagem['text'] = 'Matricula! Tente novamente'

        elif parametro == 2:
            disciplina = str(entrada_disciplina.get())
            id_disciplina = str(entrada_id_disciplina.get())
            if len(disciplina) > 0 and disciplina.isalpha():
                if len(id_disciplina) == 6:
                    AlterarNoBanco.alterar_dados_disciplina(int(id_disciplina), disciplina)
                    mensagem['text'] = 'Dados alterados com sucesso!'
                else:
                    mensagem['text'] = 'Id da disciplina invalido! Tente novamente'
            else:
                mensagem['text'] = 'Nova disciplina invalida! Tente novamente'

        elif parametro == 3:
            id_disciplina = str(entrada_id_disciplina.get())
            if len(id_disciplina) == 6:
                ExcluirNoBanco.excluir_dados_disciplinas(int(id_disciplina))
                mensagem['text'] = 'Dados deletados com sucesso!'
            else:
                mensagem['text'] = 'Id da disciplina invalida! Tente novamente!'
    except Exception as erro:
        print("Erro na coleta de dados(disciplina):",erro)

def PegarDadosResultado(parametro):
    try:
        if parametro == 1:
            id_aluno = str(entrada_id_aluno_resultado.get())
            id_disciplina = str(entrada_id_disciplina_resultado.get())
            nota1 = float(entrada_nota1.get())
            nota2 = float(entrada_nota2.get())
            nota3 = float(entrada_nota3.get())
            media = ((nota1 + nota2 + nota3) / 3)
            if len(id_aluno) == 8:
                if len(id_disciplina) == 6:
                    if nota1 <= 10 and nota2 <= 10 and nota3 <= 10:
                        SalvarNoBanco.inserir_dados_resultado(int(id_aluno), int(id_disciplina), nota1, nota2, nota3, media)
                        mensagem['text'] = 'Dados inseridos com sucesso!' 
                    else:
                        mensagem['text'] = 'Notas invalidas! Tente novamente!'
                else:
                    mensagem['text'] = 'Id disiciplina invalido! Tente novamente'
            else:
                mensagem['text'] = 'Id aluno invalido! Tente novamente'
        elif parametro == 2:
            id_aluno = str(entrada_id_aluno_resultado.get())
            nota1 = float(entrada_nota1.get())
            nota2 = float(entrada_nota2.get())
            nota3 = float(entrada_nota3.get())
            media = (nota1 + nota2 + nota3) / 3
            if len(id_aluno) == 8:
                if nota1 <= 10 and nota2 <= 10 and nota3 <= 10:
                    AlterarNoBanco.alterar_dados_resultado(int(id_aluno), nota1, nota2, nota3, media)
                    mensagem['text'] = 'Dados atualizados com sucesso!' 
                else:
                    mensagem['text'] = 'Notas invalidas! Tente novamente'
            else:
                mensagem['text'] = 'Id aluno invalido! Tente novamente'
        elif parametro == 3:
            id_aluno = str(entrada_id_aluno_resultado.get())
            if len(id_aluno) == 8:
                ExcluirNoBanco.exluir_dados_resultado(int(id_aluno))
                mensagem['text'] = 'Dados deletados com sucesso!'
            else:
                mensagem['text'] = 'Id do aluno errado! Tente novamente!'
    except Exception as erro:
        print("Erro na coleta de dados(resultado):",erro)

def RetornarDados(parametro):
    try:
        if parametro == 1:
            BancoDeDados.todos_os_alunos()
            mensagem['text'] = 'Dados de todos os alunos retornados!'
            ResultadoPesquisa(1)
        elif parametro == 2:
            BancoDeDados.todos_as_disciplinas()
            mensagem['text'] = 'Dados de todas as disciplinas retornados!'
            ResultadoPesquisa(2)
        elif parametro == 3:
            BancoDeDados.all_medias_alunos()
            mensagem['text'] = 'Dados de todas os alunos e medias retornados!'
            ResultadoPesquisa(3)
    except Exception as erro:
        print("Erro na retorno de dados:",erro)

def ResultadoPesquisa(parametro):
    janela2 = Tk()
    janela2.title("Resultado de pesquisa")
    #master.iconbitmap(default="icone.ico")
    janela2.geometry("300x400+560+150")
    janela2.wm_resizable(width=False, height=False)

    botao_voltar = Button(janela2, text="Concluido", command = janela2.destroy)
    botao_voltar.place(width=102, height=33, x=100, y=350)

    texto = Text(janela2, font='Arial 10')
    texto.place(width=300, height=350, x=0, y=0)
    try:
        if parametro == 1:
            resultado = open("todos_os_alunos.txt","r")
            texto.insert(0.0, resultado.read())
        if parametro == 2:
            resultado = open("todas_as_disciplinas.txt","r")
            texto.insert(0.0, resultado.read())
        if parametro == 3:
            resultado = open("todas_as_medias_e_alunos.txt","r")
            texto.insert(0.0, resultado.read())
    except Exception as erro:
        print("Erro na janela 2:",erro)
    janela2.mainloop()

class SalvarNoBanco:
    try:
        def inserir_dados_aluno(nome_aluno, matricula, id_aluno):
            comando = '''INSERT INTO aluno VALUES (:id_aluno, :nome_aluno, :matricula);'''
            cursor.execute(comando, {"id_aluno": id_aluno, "nome_aluno": nome_aluno, "matricula": matricula})
            conexao.commit()

        def inserir_dados_disciplina(id_disciplina, nome_disciplina):
            comando = '''INSERT INTO disciplina VALUES (:id_disciplina, :nome_disciplina);'''
            cursor.execute(comando, {"id_disciplina": id_disciplina, "nome_disciplina": nome_disciplina})
            conexao.commit()

        def inserir_dados_resultado(id_aluno, id_disciplina, nota1, nota2, nota3, media):
            comando = '''INSERT INTO resultados VALUES (:aluno_id, :disciplina_id, :nota1, :nota2, :nota3, :media);'''
            cursor.execute(comando, {"aluno_id": id_aluno, "disciplina_id": id_disciplina, "nota1": nota1, "nota2": nota2, "nota3": nota3, "media": media})
            conexao.commit()
    except Exception as erro:
        print("Erro em salvar(banco de dados):",erro)

class ExcluirNoBanco:
    try:
        def excluir_dados_aluno(id_aluno):
            comando = '''DELETE FROM aluno WHERE id_aluno = :id_aluno;'''
            cursor.execute(comando, {"id_aluno": id_aluno})
            conexao.commit()

        def excluir_dados_disciplinas(id_disciplina):
            comando = '''DELETE FROM disciplina WHERE id_disciplina = :id_disciplina;'''
            cursor.execute(comando, {"id_disciplina": id_disciplina})
            conexao.commit()

        def exluir_dados_resultado(id_aluno):
            comando = '''DELETE FROM resultados WHERE aluno_id = :aluno_id;'''
            cursor.execute(comando, {"aluno_id": id_aluno})
            conexao.commit()
    except Exception as erro:
        print("Erro em excluir(banco de dados):",erro)

class AlterarNoBanco:
    try:
        def alterar_dados_aluno(id_aluno, nome_aluno, matricula):
            cursor.execute("UPDATE aluno SET nome_aluno = ?, matricula = ? WHERE id_aluno = ?", (nome_aluno, matricula, id_aluno))
            conexao.commit()

        def alterar_dados_disciplina(id_disciplina, nome_disciplina):
            cursor.execute("UPDATE disciplina SET nome_disciplina = ? WHERE id_disciplina = ?", (nome_disciplina, id_disciplina))
            conexao.commit()

        def alterar_dados_resultado(aluno_id, nota1, nota2, nota3, media):
            cursor.execute("UPDATE resultados SET nota1 = ?, nota2 = ?, nota3 = ?, media = ? WHERE aluno_id = ?", (nota1, nota2, nota3, media, aluno_id))
            conexao.commit()

    except Exception as erro:
        print("Erro em alterar dados(banco de dados):",erro)

class BancoDeDados:
    def todos_os_alunos():
        try:
            cursor.execute("SELECT id_aluno, nome_aluno, matricula FROM aluno;")
            selecao_resultado = cursor.fetchall()
            if not selecao_resultado:
                mensagem2['text'] = 'Não há dados a serem visualizados'
            else:
                '''O banco de dados retorna uma lista com varias tuplas.
                Cada tupla contem o nome de um aluno.
                O que fiz abaixo foi transformar essas tuplas em listas.
                Ou seja: Lista do banco de dados -contem- varias lista com um nome do aluno cada
                No fim retornamos os dados, ou seja, somente o nome do aluno
                '''
                arquivo = open("todos_os_alunos.txt","w")
                arquivo.write(">>> Lista de todos os alunos:\n")
                for dado in selecao_resultado:
                    id_aluno, aluno, matricula = dado
                    arquivo.write(f"Id: {id_aluno} | Aluno: {aluno} | Matricula: {matricula}")
                    arquivo.write("\n")
                arquivo.close()
        except Exception as erro:
            print("Erro na consulta: Alunos:",erro)
    def todos_as_disciplinas():
        try:
            cursor.execute("SELECT id_disciplina, nome_disciplina FROM disciplina;")
            selecao_resultado = cursor.fetchall()
            if not selecao_resultado:
                mensagem2['text'] = 'Não há dados a serem visualizados'
            else:
                arquivo = open("todas_as_disciplinas.txt","w")
                arquivo.write(">>> Lista de todos as disciplinas:\n")
                for dado in selecao_resultado:
                    id_disciplina, disciplina = dado
                    arquivo.write(f"ID: {id_disciplina} | Disciplina: {disciplina}")
                    arquivo.write("\n")
                arquivo.close()
        except Exception as erro:
            print("Erro na consulta: Disciplinas:",erro)
    def all_medias_alunos():
        try:
            cursor.execute("SELECT aluno.nome_aluno, resultados.media "
                        "FROM aluno JOIN resultados "
                        "ON aluno.id_aluno = resultados.aluno_id ")
            selecao_resultado = cursor.fetchall()
            if not selecao_resultado:
                mensagem2['text'] = 'Não há dados a serem visualizados'
            else:
                arquivo = open("todas_as_medias_e_alunos.txt","w")
                arquivo.write(">>> Lista de todos os alunos e suas medias:\n")
                for dado in selecao_resultado:
                    aluno, media = dado
                    arquivo.write(f"Aluno: {aluno} | Media: {media}")
                    arquivo.write("\n")
            arquivo.close()
        except Exception as erro:
            print("Erro na consulta: Medias e Alunos:",erro)

#criação da janela
janela = Tk()
janela.title("Laçamento de notas de alunos")
janela.geometry("1100x550+155+70")
janela.wm_resizable(width=False, height=False)

#importação da imagem de fundo
fundo_imagem = PhotoImage(file="modelo.png")

#Label
labelfundo = Label(janela, image=fundo_imagem)
labelfundo.place(x=0, y=0)

#Aluno ------------------------------------

#Entradas
entrada_nome_aluno = Entry(janela, justify=LEFT)
entrada_nome_aluno.place(width=228, height=22, x=105, y=120)

entrada_nome_matricula = Entry(janela, justify=LEFT)
entrada_nome_matricula.place(width=202, height=22, x=131, y=160)

entrada_id_aluno = Entry(janela, justify=LEFT)
entrada_id_aluno.place(width=100, height=22, x=119, y=195)

#Botao
botao1 = Button(janela, text="Salvar", relief='raised', command=lambda:PegarDadosAlunos(1))
botao1.place(width=70, height=33, x=72, y=232)

botao1 = Button(janela, text="Alterar", relief='raised', command=lambda:PegarDadosAlunos(2))
botao1.place(width=70, height=33, x=158, y=232)

botao1 = Button(janela, text="Excluir", relief='raised', command=lambda:PegarDadosAlunos(3))
botao1.place(width=70, height=33, x=244, y=232)

#Disciplinas ------------------------------------

#Entradas
entrada_disciplina = ttk.Combobox(janela, values=lista_disciplinas)
entrada_disciplina.place(width=232, height=22, x=462, y=120)

entrada_id_disciplina = Entry(janela, justify=LEFT)
entrada_id_disciplina.place(width=187, height=22, x=506, y=160)

#Botao
botao1 = Button(janela, text="Salvar", relief='raised', command=lambda:PegarDadosDisciplina(1))
botao1.place(width=70, height=33, x=428, y=232)

botao1 = Button(janela, text="Alterar", relief='raised', command=lambda:PegarDadosDisciplina(2))
botao1.place(width=70, height=33, x=514, y=232)

botao1 = Button(janela, text="Excluir", relief='raised', command=lambda:PegarDadosDisciplina(3))
botao1.place(width=70, height=33, x=600, y=232)

#Resultado ------------------------------------

#Entradas
entrada_id_aluno_resultado = Entry(janela, justify=LEFT)
entrada_id_aluno_resultado.place(width=217, height=22, x=838, y=119)

entrada_id_disciplina_resultado = Entry(janela, justify=LEFT)
entrada_id_disciplina_resultado.place(width=190, height=22, x=865, y=157)

entrada_nota1 = Entry(janela, justify=LEFT)
entrada_nota1.place(width=70, height=22, x=820, y=195)

entrada_nota2 = Entry(janela, justify=LEFT)
entrada_nota2.place(width=70, height=22, x=903, y=195)

entrada_nota3 = Entry(janela, justify=LEFT)
entrada_nota3.place(width=70, height=22, x=986, y=195)

#Botao
botao1 = Button(janela, text="Salvar", relief='raised', command=lambda:PegarDadosResultado(1))
botao1.place(width=70, height=33, x=794, y=232)

botao1 = Button(janela, text="Alterar", relief='raised', command=lambda:PegarDadosResultado(2))
botao1.place(width=70, height=33, x=877, y=232)

botao1 = Button(janela, text="Excluir", relief='raised', command=lambda:PegarDadosResultado(3))
botao1.place(width=70, height=33, x=960, y=232)

#Consultas ------------------------------------------

botao_consultar_alunos = Button(janela, text="Alunos", relief='raised', command=lambda:RetornarDados(1))
botao_consultar_alunos.place(width=232, height=32, x=72, y=340)

botao_consultar_disciplinas = Button(janela, text="Disciplinas", relief='raised', command=lambda:RetornarDados(2))
botao_consultar_disciplinas.place(width=232, height=32, x=72, y=390)

botao_consultar_medias = Button(janela, text="Médias", relief='raised', command=lambda:RetornarDados(3))
botao_consultar_medias.place(width=232, height=32, x=72, y=440)

#--------------------------------------------------------------
#Mensagens na tela
mensagem = Label(janela, text='', font="Arial 17", relief='flat', fg='#020304', bg='#ededed')
mensagem.place(width=500, height=25, x=500, y=380)

mensagem2 = Label(janela, text='', font="Arial 17", relief='flat', fg='#020304', bg='#ededed')
mensagem2.place(width=500, height=25, x=500, y=410)

janela.mainloop()
cursor.close()
conexao.close()

''''
Alguns comentários sobre o código:
Fiz as alterações que o senhor me falou na última aula, agora é possível adicionar, 
alterar e excluir todos os valores de todas as tabelas:

O projeto até o momento está funcionando bem nos testes que fiz, 
porém pensei em algumas melhorias, não implementei pois fiquei corrigindo o 
código e o por conta do trabalho, pouco tempo.

Pendencias: 
Excluir a criação de arquivos para mostrar na tela, visto que não é necessário a criação dos mesmos.

Para fazer uma alteração é necessário digitar o id correspondente da tabela.
O usuário pode obter esses ids pelas consultas, mas o trabalho fica um pouco chato, 
visto que você teria que copiar e colar para alterar. Pensei em fazer um dicionário para 
mostrar todos os nomes dos alunos, ao clicar aparecida o id no campo e realizaria a exclusão/alteração.

A orientação a objetos também não está boa, falta iniciar as variáveis entre outras coisas. 
POO ainda não dominei muito bem.

Fiquei devendo a modularização do código, visto que ficaria mais fácil realizar alterações.
'''