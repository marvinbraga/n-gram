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
        self._data = []

    @property
    def data(self):
        return self._data

    def process(self):
        for line in self._loader.lines:
            data = line.split("\n")[:-1]
            if data:
                for word in data[0].split():
                    self._data.append(word)
        return self


class Fitter:
    """
    Classe para filtrar os dados conforme o N informado.
    """

    def __init__(self, n_gram, serializer):
        self._serializer = serializer
        self._n_gram = n_gram
        self._result = None

    @property
    def result(self):
        return self._result

    def _prepare(self):
        return self

    def count(self):
        return self
