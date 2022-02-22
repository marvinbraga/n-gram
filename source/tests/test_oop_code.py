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
def source():
    source_file = os.path.normpath("./source/texto.txt")
    return Serializer(lines=Loader(source_file=source_file).execute().lines).process()


@pytest.mark.initialization
def tests_load_source_file(source):
    assert len(source.words) > 0


@pytest.mark.calculate
def tests_calculate_n_gram1(source):
    assert Fitter(n_gram=1, words=source.words).count().result


@pytest.mark.calculate
def tests_calculate_n_gram2(source):
    assert Fitter(n_gram=2, words=source.words).count().result
