def contar_palavras(texto):
    texto = texto.lower()
    palavras = texto.split()
    contagem = {}
    for palavra in palavras:
        contagem[palavra] = contagem.get(palavra, 0) + 1
    return contagem
