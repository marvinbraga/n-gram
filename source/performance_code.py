# coding=utf-8
"""
Prova "Desenvolvedor Jovens Talentos"
Desafio para Engenheiro de Software.

Marcus Vinicius Braga, 2022.

 Refaça o programa anterior, na mesma linguagem usada, ainda sem uso de bibliotecas
"prontas" ou "externas", mas ao invés de focar em código simples e legível, foque em um
código performático, isto é, que tenha pelo menos algumas das seguintes características:
— Menor uso de cpu
— Menor uso de memória ram
— Menos operações de entrada/saída (I/O)
— Menor complexidade algorítmica segundo a notação big O
"""
import sys

from utils.argv import ParserArgv
from utils.profile import profile


@profile
def execute(source_file, n_gram):
    # Ler o conteúdo do arquivo.
    file = open(source_file, encoding="utf-8", mode="r")
    try:
        lines = file.readlines()
    finally:
        file.close()

    # Ajusta o conteúdo do arquivo e carrega a lista de palavras.
    lines = [*map(lambda ln: ln.strip().split(), lines)]
    words = []
    for line in lines:
        words += [*map(lambda word: word.lower(), line)]

    # Motar a lista com o conjunto de palavras e gerar ‘strings’ de resultado.
    ngram = int(n_gram)
    data = sorted([" ".join(reg) for reg in [words[i:i + ngram] for i in range(len(words) - (ngram - 1))]])

    # Contabiliza a contagem e montar o resultado.
    result = {w: c for w, c in sorted(
        {item: data.count(item) for item in set(data)}.items(), key=lambda c: c[1], reverse=True)}

    return result


if __name__ == '__main__':
    info = ParserArgv(sys.argv[1:]).parse()
    print(execute(info.get("source_file"), info.get("n_gram")))
