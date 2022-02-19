# coding=utf-8

"""
R-GRAM Challenger - Test Software Engineer.
Marcus Vinicius Braga, 2022.
Todos os direitos reservados.
"""
from utils.argv import ParserArgv


def test_argv_one_invalid_param():
    argv = ["./source/texto.txt"]
    result = ParserArgv(argv).parse()
    assert not result.get("source_file") and not result.get("n_gram")


def test_argv_two_invalid_params():
    argv = ["./source/texto.txt", "1"]
    result = ParserArgv(argv).parse()
    assert not result.get("source_file") and not result.get("n_gram")


def test_argv_source_file_valid():
    argv = ["source_file=./source/texto.txt"]
    result = ParserArgv(argv).parse()
    assert result.get("source_file") and not result.get("n_gram")


def test_argv_n_gram_valid():
    argv = ["n_gram=1"]
    result = ParserArgv(argv).parse()
    assert not result.get("source_file") and result.get("n_gram")


def test_argv_valid_params():
    argv = ["source_file=./source/texto.txt", "n_gram=1"]
    result = ParserArgv(argv).parse()
    assert result.get("source_file") and result.get("n_gram")
