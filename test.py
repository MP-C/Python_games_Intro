import os

univ = {'cursos': []}

def adicionarCurso(curso):
    univ["cursos"].append(curso)
    
adicionarCurso({'nome': 'test'})
print(univ)

a 