# coding=utf-8

"""
N-GRAM Challenger - Test Software Engineer.
Marcus Vinicius Braga, 2022.
Todos os direitos reservados.
"""
import os

from simple_code import execute


def test_n_gram_1():
    output = execute(os.path.normpath("../texto.txt"), "1")
    assert len(output) == 16
    assert output["cada"] == 8
    assert output["um"] == 8
    assert output["porque"] == 3
    assert output["de"] == 2
    assert output["vai"] == 1


def test_n_gram_2():
    output = execute(os.path.normpath("../texto.txt"), "2")
    assert len(output) == 24
    assert output["cada um"] == 8
    assert output["a casa"] == 2
    assert output["é porque"] == 2
    assert output["não fosse"] == 1
    assert output["vá lá"] == 1
    assert output["queria que"] == 1
