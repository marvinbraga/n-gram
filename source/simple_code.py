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
import os


def execute(file_name):
    with open(file_name, encoding="utf-8", mode="r") as file:
        try:
            lines = file.readlines()
        finally:
            file.close()

    for line in lines:
        data = line.split("\n")[:-1]
        if data:
            for word in data[0].split():
                data.append(word)


if __name__ == '__main__':
    execute(os.path.normpath("texto.txt"))
