from modulos.contagem_palavras import contar_palavras

texto = input("Digite o texto para análise: ")
resultado = contar_palavras(texto)

print("Frequência das palavras no texto:")
for palavra, contagem in resultado.items():
    print(f"{palavra}: {contagem}")
