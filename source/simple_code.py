# coding=utf-8
"""
Prova "Desenvolvedor Jovens Talentos"
Desafio para Engenheiro de Software.

Marcus Vinicius Braga, 2022.

Faça um programa simples e legível, em qualquer linguagem de programação, mas sem uso
de bibliotecas "prontas" ou "externas", que:
— leia um arquivo de texto e receba um parâmetro N > 0;
— Gere uma saída do arquivo com as frequências ordenadas dos N-gramas.
"""
import sys

from utils.argv import ParserArgv
from utils.profile import profile


@profile(repeat=1, number=1000)
def execute(source_file, n_gram):
    if not source_file or not n_gram:
        return

    # Ler o conteúdo do arquivo.
    file = open(source_file, encoding="utf-8", mode="r")
    try:
        lines = file.readlines()
    finally:
        file.close()

    # Ajusta o conteúdo do arquivo e carrega a lista de palavras.
    words = []
    for line in lines:
        data = line.strip().split()
        if data:
            for word in data:
                words.append(word.lower())

    # Motar a lista com o conjunto de palavras.
    ngram, output = int(n_gram), []
    ngram_range = len(words) - (ngram - 1)
    for i in range(ngram_range):
        output.append(words[i:i + ngram])

    # Gerar ‘strings’ de resultado.
    data = []
    for reg in output:
        data.append(" ".join(reg))
    data = sorted(data)

    # Contabiliza a contagem.
    result = dict()
    for item in data:
        result.update({item: result.get(item, 0) + 1})
    sorted_list = sorted(result, key=result.get, reverse=True)

    # Montar o resultado.
    sorted_result = dict()
    for item in sorted_list:
        sorted_result[item] = result.get(item)

    return sorted_result


if __name__ == '__main__':
    info = ParserArgv(sys.argv[1:]).parse()
    print(execute(info.get("source_file"), info.get("n_gram")))
