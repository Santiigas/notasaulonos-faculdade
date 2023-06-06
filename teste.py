import random
import string

gerar = ''.join(random.choices(string.digits, k=5))
id_aluno = int(gerar)

print(id_aluno, type(id_aluno))


'''
class SalvarNoBanco:
    def __init__(self, nome_aluno, matricula, id_disciplina, nome_disciplina, nota1, nota2, nota3, media):
        self.nome_aluno = nome_aluno
        self.matricula = matricula
        self.id_disciplina = id_disciplina
        self.nome_disciplina = nome_disciplina
        self.nota1 = nota1
        self.nota2 = nota3
        self.nota3 = nota3
        self.media = media

    def inserir_dados_aluno(nome_aluno, matricula, id_aluno):
        comando = '''INSERT INTO aluno VALUES (:id_aluno, :nome_aluno, :matricula);'''
        cursor.execute(comando, {"id_aluno": id_aluno, "nome_aluno": nome_aluno, "matricula": matricula})
        conexao.commit()

    def inserir_dados_disciplina(id_disciplina, nome_disciplina):
        comando = '''INSERT INTO disciplina VALUES (:id_disciplina, :nome_disciplina);'''
        cursor.execute(comando, {"id_disciplina": id_disciplina, "nome_disciplina": nome_disciplina})
        conexao.commit()

    def inserir_dados_resultado(aluno_id, disciplina_id, nota1, nota2, nota3, media):
        comando = '''INSERT INTO resultados VALUES (:id_aluno, :id_disciplina, :nota1, :nota2, :nota3, :media);'''
        cursor.execute(comando, {"aluno_id": aluno_id, "disciplina_id": disciplina_id, "nota1": nota1, "nota2": nota2, "nota3": nota3, "media": media})
        conexao.commit()
'''