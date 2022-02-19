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


@profile
def execute(source_file, n_gram):
    if not source_file or not n_gram:
        return

    ngram = int(n_gram)
    file = open(source_file, encoding="utf-8", mode="r")
    try:
        lines = file.readlines()
    finally:
        file.close()

    result = []
    for line in lines:
        data = line.split("\n")[:-1]
        if data:
            for word in data[0].split():
                result.append(word)

    text, n, n_gram_result = "", 1, []
    for i in result:
        text += " " + i.lower()
        n += 1
        if n > ngram:
            n_gram_result.append(text.strip())
            text = "" if ngram == 1 else i.lower()
            n = 1 if ngram == 1 else 2

    output = dict()
    for item in n_gram_result:
        output.update({item: output.get(item, 0) + 1})
    sorted_list = sorted(output, key=output.get, reverse=True)
    sorted_output = dict()
    for item in sorted_list:
        sorted_output[item] = output.get(item)
    print(sorted_output)


if __name__ == '__main__':
    info = ParserArgv(sys.argv[1:]).parse()
    execute(info.get("source_file"), info.get("n_gram"))
