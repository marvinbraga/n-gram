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


def execute(source_file, n_gram):
    if not source_file or not n_gram:
        return

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

    print(result)


if __name__ == '__main__':
    info = ParserArgv(sys.argv[1:]).parse()
    execute(info.get("source_file"), info.get("n_gram"))
