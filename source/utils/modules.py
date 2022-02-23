# coding=utf-8

"""
N-GRAM Challenger - Test Software Engineer.
Marcus Vinicius Braga, 2022.
Todos os direitos reservados.
"""

import os


class ModuleName:
    def __init__(self, module: str):
        self._module_str = module

    def get(self):
        return os.path.normpath(self._module_str.split()[-1:][0].split("'")[1])
