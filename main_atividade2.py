from modulos.soma_notas import calcular_soma
from modulos.media_notas import calcular_media

notas = list(map(float, input("Digite as notas dos alunos separadas por espaço: ").split()))
soma = calcular_soma(notas)
media = calcular_media(soma, len(notas))
print(f"A média das notas é: {media:.2f}")
