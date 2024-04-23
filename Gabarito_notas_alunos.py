

# variavel_lista.append(variavel input)

num_alunos = int(input("Digite a quantidade de alunos: "))

media_alunos = []
notas_turma = []

for i in range(1, num_alunos +1):
    print(f"Aluno {i}: ")
    notas_aluno = [] # lista pentencente ao for' dentro
    
    for j in range(1, 4):
        nota = float(input(f"Insira a nota {j}: "))
        notas_aluno.append(nota) # lista -> variavel do input
        notas_turma.append(nota) # salvou tbm na lista da turma

        media_aluno = sum(notas_aluno) / len(notas_aluno) # sum() -> soma dividido pelo len() -> tamanho
        media_alunos.append(media_aluno)
        print(f"A média do Aluno {i} é: {media_aluno:.2f}")
    
media_turma = sum(notas_turma) / len(notas_turma)
nota_maxima = max(notas_turma)
nota_minima_turma = min(notas_turma)


print(f"Média da Turma: {media_turma:.2f}")
print(f"Nota mais alta da Turma: {nota_maxima:.2f}")
print(f"Nota mínima da Turma: {nota_minima_turma:.2f}")
