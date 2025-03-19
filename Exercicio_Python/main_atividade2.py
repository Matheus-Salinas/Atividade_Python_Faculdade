from modulos.soma_notas import calcular_soma
from modulos.media_notas import calcular_media

notas = [7.5, 8.0, 6.5, 9.0, 7.0]
soma = calcular_soma(notas)
media = calcular_media(soma, len(notas))
print(f"A média das notas é: {media:.2f}")
