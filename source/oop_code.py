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


class Loader:
    """
    Classe para ler o arquivo de texto e carregá-lo em uma lista.
    """

    def __init__(self, source_file):
        self._source_file = source_file
        self._lines = None

    @property
    def lines(self):
        return self._lines

    def execute(self):
        with open(self._source_file, encoding="utf-8", mode="r") as file:
            try:
                self._lines = file.readlines()
            finally:
                file.close()
        return self


class Serializer:
    """
    Classe para ajustar o conteúdo do arquivo em uma lista de dados única.
    """

    def __init__(self, loader):
        self._loader = loader
        self._words = []

    @property
    def words(self):
        return self._words

    def process(self):
        lines = [*map(lambda ln: ln.strip().split(), self._loader.lines)]
        for line in lines:
            self._words += [*map(lambda word: word.lower(), line)]
        return self


class Fitter:
    """
    Classe para filtrar os dados conforme o N informado.
    """

    def __init__(self, n_gram, serializer):
        self._serializer = serializer
        self._ngram = n_gram
        self._result = dict()

    @property
    def result(self):
        return self._result

    def _prepare(self):
        ngram, words = int(self._ngram), self._serializer.words
        return sorted([" ".join(reg) for reg in [words[i:i + ngram] for i in range(len(words) - (ngram - 1))]])

    @profile
    def count(self):
        data = self._prepare()
        self._result = {w: c for w, c in sorted(
            {item: data.count(item) for item in set(data)}.items(), key=lambda c: c[1], reverse=True)}
        return self


if __name__ == '__main__':
    info = ParserArgv(sys.argv[1:]).parse()
    print(Fitter(
        info.get("n_gram"),
        Serializer(
            Loader(
                info.get("source_file")
            ).execute()
        ).process()
    ).count().result)
