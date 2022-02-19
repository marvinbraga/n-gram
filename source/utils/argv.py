# coding=utf-8

"""
R-GRAM Challenger - Test Software Engineer.
Marcus Vinicius Braga, 2022.
Todos os direitos reservados.
"""

from utils.abstract_parser import AbstractParser


class ParserArgv(AbstractParser):
    valid_params = ["source_file", "n_gram"]

    def __init__(self, argv, decorator=None):
        super().__init__(argv, decorator)
        self._result = {
            "source_file": None,
            "n_gram": 0
        }

    def _process(self):
        for arg in self._argv:
            if "=" in arg:
                args = arg.split("=")
                if args[0] in self.valid_params:
                    self._result.update({args[0]: args[1]})
