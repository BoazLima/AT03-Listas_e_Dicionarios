# AT03-Listas_e_Dicionarios
Atividades das aulas de Programação

1) Manipulação da lista animais:

python
Copiar
Editar
animais = ['cachorro', 'gato', 'papagaio']

animais.append('hamster')         # Adiciona 'hamster' ao final
animais.insert(1, 'coelho')       # Insere 'coelho' na posição 1
animais.pop()                     # Remove o último elemento ('hamster')
animais.pop(2)                    # Remove o elemento da posição 2 ('gato')
animais[0] = 'leão'               # Altera o primeiro elemento para 'leão'

print(animais)  # Resultado: ['leão', 'coelho', 'papagaio']
