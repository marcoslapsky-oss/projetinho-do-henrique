# Lista para armazenar os tempos dos atletas
tempos = []

# Registrar o tempo de 20 atletas
for i in range(20):
    tempo = float(input(f"Digite o tempo do atleta {i+1} (em segundos): "))
    tempos.append(tempo)

# Calcular a soma e quantidade manualmente
soma = 0
quantidade = 0

for t in tempos:
    soma += t
    quantidade += 1

media = soma / quantidade

# Contar acima e abaixo da média
acima_media = 0
abaixo_media = 0

for t in tempos:
    if t > media:
        acima_media += 1
    elif t < media:
        abaixo_media += 1

# Melhor e pior tempo (manual)
melhor_tempo = tempos[0]
pior_tempo = tempos[0]

for t in tempos:
    if t < melhor_tempo:
        melhor_tempo = t
    if t > pior_tempo:
        pior_tempo = t

# Diferença entre melhor e pior
diferenca = pior_tempo - melhor_tempo

# Posição do melhor atleta (manual)
posicao_melhor = 0

for i in range(quantidade):
    if tempos[i] == melhor_tempo:
        posicao_melhor = i + 1
        break

# Classificação dos atletas
elite = 0
regular = 0
iniciante = 0

for t in tempos:
    if t < (media - 10):
        elite += 1
    elif (media - 10) <= t <= (media + 10):
        regular += 1
    else:
        iniciante += 1

# Resultados
print("\n--- RESULTADOS ---")
print(f"Tempo médio: {media:.2f} segundos")
print(f"Atletas acima da média: {acima_media}")
print(f"Atletas abaixo da média: {abaixo_media}")
print(f"Melhor tempo: {melhor_tempo} segundos")
print(f"Pior tempo: {pior_tempo} segundos")
print(f"Diferença entre melhor e pior: {diferenca} segundos")
print(f"Posição do melhor atleta: {posicao_melhor}")

print("\nClassificação:")
print(f"Elite: {elite}")
print(f"Regular: {regular}")
print(f"Iniciante: {iniciante}")