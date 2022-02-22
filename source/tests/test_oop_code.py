# coding=utf-8

"""
N-GRAM Challenger - Test Software Engineer.
Marcus Vinicius Braga, 2022.
Todos os direitos reservados.
"""
import os.path

import pytest

from source.oop_code import Serializer, Loader, Fitter


@pytest.fixture
def test_loader():
    source_file = os.path.normpath("./source/texto.txt")
    return Loader(source_file=source_file).execute()


@pytest.fixture
def test_source(test_loader):
    return Serializer(lines=test_loader.lines).process()


@pytest.mark.oop_code
@pytest.mark.initialization
def tests_loader(test_loader):
    assert len(test_loader.lines) > 0


@pytest.mark.oop_code
@pytest.mark.initialization
def tests_load_source_file(test_source):
    assert len(test_source.words) > 0


@pytest.mark.oop_code
@pytest.mark.calculate
def tests_calculate_n_gram1(test_source):
    output = Fitter(n_gram=1, words=test_source.words).count().result
    assert output
    assert len(output) == 16
    assert output["cada"] == 8
    assert output["um"] == 8
    assert output["porque"] == 3
    assert output["de"] == 2
    assert output["vai"] == 1


@pytest.mark.oop_code
@pytest.mark.calculate
def tests_calculate_n_gram2(test_source):
    output = Fitter(n_gram=2, words=test_source.words).count().result
    assert output
    assert len(output) == 24
    assert output["cada um"] == 8
    assert output["a casa"] == 2
    assert output["é porque"] == 2
    assert output["não fosse"] == 1
    assert output["vá lá"] == 1
    assert output["queria que"] == 1
