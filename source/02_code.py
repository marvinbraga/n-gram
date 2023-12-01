import heapq
import os


def file_generator(file_path, chunk_size=1024):
    """Gera pedaços do arquivo para processamento eficiente."""
    with open(file_path, 'r', encoding="utf-8") as file:
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break
            yield chunk


def generate_ngrams(words, n):
    """Gera N-grams usando um gerador."""
    for i in range(len(words) - n + 1):
        yield ' '.join(words[i:i + n])


def count_ngrams(file_path, n):
    """Conta a frequência dos N-grams otimizando a memória e CPU."""
    frequency = {}
    for chunk in file_generator(file_path):
        words = chunk.split()
        for ngram in generate_ngrams(words, n):
            frequency[ngram] = frequency.get(ngram, 0) + 1
    return frequency


def main(file_path, n):
    frequencies = count_ngrams(file_path, n)

    # Ordenar os N-grams usando uma heap para eficiência
    top_ngrams = heapq.nlargest(len(frequencies), frequencies, key=frequencies.get)

    for ngram in top_ngrams:
        print(f"{ngram}: {frequencies[ngram]}")


# Exemplo de uso
file_path = os.path.normpath("E:/python/n-gram/source/texto.txt")
n = 1  # Substitua por um valor de N desejado
main(file_path, n)
