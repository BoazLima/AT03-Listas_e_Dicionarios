# Criação e inicialização do dicionário
alunos = {
    "Ana": 8.5,
    "Pedro": 7.0,
    "Maria": 9.2
}

# Adiciona o aluno Carlos com nota 6.5
alunos["Carlos"] = 6.5

# Atualiza a nota da Ana para 9.0
alunos["Ana"] = 9.0

# Remove o aluno Pedro
alunos.pop("Pedro")

# Calcula a média das notas
media = sum(alunos.values()) / len(alunos)
print(f"Média das notas: {media:.2f}")

# Verifica se Maria está no dicionário
if "Maria" in alunos:
    print("Maria está no dicionário.")
else:
    print("Maria NÃO está no dicionário.")
