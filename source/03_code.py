import itertools
import os
from collections import Counter


class NGramFactory:
    """Fábrica para criar N-grams."""

    @staticmethod
    def create_ngrams(words, n):
        return [' '.join(words[i:i + n]) for i in range(len(words) - n + 1)]


class FileReader:
    """Classe responsável por ler arquivos."""

    def __init__(self, file_path):
        self.file_path = file_path

    def __iter__(self):
        with open(self.file_path, 'r', encoding='utf-8') as file:
            for line in file:
                yield line.strip().split()


class NGramCounter:
    """Classe para contar N-grams."""

    def __init__(self, reader, n):
        self.reader = reader
        self.n = n

    def count_ngrams(self):
        return Counter(
            itertools.chain.from_iterable(
                NGramFactory.create_ngrams(words, self.n) for words in self.reader
            )
        )


def main(file_path, n):
    reader = FileReader(file_path)
    counter = NGramCounter(reader, n)
    frequencies = counter.count_ngrams()

    for ngram, freq in frequencies.most_common():
        print(f"{ngram}: {freq}")


# Exemplo de uso
_file_path = os.path.normpath("E:/python/n-gram/source/texto.txt")
_n = 3  # Substitua por um valor de N desejado
main(_file_path, _n)
