# coding=utf-8

"""
R-GRAM Challenger - Test Software Engineer.
Marcus Vinicius Braga, 2022.
Todos os direitos reservados.
"""
from abc import ABCMeta, abstractmethod


class AbstractParser(metaclass=ABCMeta):
    valid_params = []

    def __init__(self, argv, decorator=None):
        self._decorator = decorator
        self._argv = argv
        self._params = []
        self._result = dict()

    def parse(self) -> dict:
        if self._decorator:
            self._result.update(self._decorator.parse())
        if self._argv:
            self._process()
        return self._result

    @abstractmethod
    def _process(self):
        pass
