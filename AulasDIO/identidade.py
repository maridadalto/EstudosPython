# -*- coding: utf-8 -*-
'''São operadores utilizados para comparar se dois objetos testados ocupam a mesma posição na memória'''

curso = "Curso em Python"
nome_curso = curso
saldo,limite = 200,300

# o operador é o is
print(curso is nome_curso)

print(curso is not nome_curso)

print(saldo is limite)