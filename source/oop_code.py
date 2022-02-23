# coding=utf-8
"""
Prova "Desenvolvedor Jovens Talentos"
Desafio para Engenheiro de Software.
Marcus Vinicius Braga, 2022.

Refaça um dos programas anteriores, mas agora podendo usar qualquer biblioteca
(provavelmente o que você faria em um ambiente profissional).
"""
import os.path
import sys
from collections import Counter

from source.utils.argv import ParserArgv
from utils.modules import ModuleName
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

    def __init__(self, lines):
        self._lines = lines
        self._words = []

    @property
    def words(self):
        return self._words

    def process(self):
        lines = [*map(lambda ln: ln.strip().split(), self._lines)]
        for line in lines:
            self._words += [*map(lambda word: word.lower(), line)]
        return self


class Fitter:
    """
    Classe para filtrar os dados conforme o N informado.
    """

    def __init__(self, n_gram, words):
        self._words = words
        self._ngram = n_gram
        self._result = dict()

    @property
    def result(self):
        return self._result

    def count(self):
        ngram, words = int(self._ngram), self._words
        self._result = {i: v for i, v in sorted(
            Counter(
                [" ".join(reg) for reg in [words[i:i + ngram] for i in range(len(words) - (ngram - 1))]]
            ).items(), key=lambda item: (-item[1], item[0])
        )}
        return self


@profile(repeat=1, number=1000)
def exec_oop_code(info_env):
    return Fitter(
        n_gram=info_env.get("n_gram"),
        words=Serializer(
            lines=Loader(source_file=info_env.get("source_file")).execute().lines
        ).process().words
    ).count().result


if __name__ == '__main__':
    info = ParserArgv(sys.argv[1:]).parse()
    if not info["source_file"] or not info["n_gram"]:
        module = ModuleName(str(sys.modules[__name__])).get()
        print("Utilize a linha de comando da seguinte forma:")
        print(f"python {module} source_file={os.path.join(os.path.dirname(module), 'texto.txt')} n_gram=1")
    else:
        print(exec_oop_code(info))
