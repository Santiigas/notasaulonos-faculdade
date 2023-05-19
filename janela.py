from tkinter import *
from principal import *
import random
import string

matricula = ''.join(random.choices(string.digits, k=12))
id_disciplina = ''.join(random.choices(string.digits, k=6))

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
nome = Entry(janela)
nome.place(width=231, height=22, x=102, y=135)

disciplina = Entry(janela)
disciplina.place(width=202, height=22, x=131, y=173)

nota1 = Entry(janela)
nota1.place(width=70, height=22, x=98, y=210)

nota2 = Entry(janela)
nota2.place(width=70, height=22, x=181, y=210)

nota3 = Entry(janela)
nota3.place(width=70, height=22, x=263, y=210)

#Botao
botao1 = Button(janela, text="Salvar", relief='flat', command=lambda: Aluno.inserir_dados(nome, matricula, id_disciplina, disciplina, nota1, nota2, nota3))
botao1.place(width=102, height=33, x=138, y=252)


#função para mapeamento da aréa
def clique_mouse(retorno):
    print(f'X: {retorno.x} | Y:{retorno.y} Geo: {janela.geometry()}')

#eventos - mapear area do pc
#master.bind("<Button-1>", clique_mouse)

janela.mainloop()
