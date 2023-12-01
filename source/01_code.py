import os.path


def read_file(file_path):
    with open(file_path, 'r', encoding="utf-8") as file:
        return file.read()


def generate_ngrams(text, n):
    words = text.split()
    ngrams = [' '.join(words[i:i + n]) for i in range(len(words) - n + 1)]
    return ngrams


def count_ngrams(ngrams):
    frequency = {}
    for ngram in ngrams:
        if ngram in frequency:
            frequency[ngram] += 1
        else:
            frequency[ngram] = 1
    return frequency


def main(file_path, n):
    text = read_file(file_path)
    ngrams = generate_ngrams(text, n)
    frequencies = count_ngrams(ngrams)

    # Ordenar os N-gramas por frequência em ordem decrescente
    sorted_ngrams = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)

    for ngram, freq in sorted_ngrams:
        print(f"{ngram}: {freq}")


# Exemplo de uso

file_path = os.path.normpath("E:/python/n-gram/source/texto.txt")
n = 1  # Substitua por um valor de N desejado
main(file_path, n)
