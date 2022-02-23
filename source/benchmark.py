# coding=utf-8

"""
N-GRAM Challenger — Test Software Engineer.
Marcus Vinicius Braga, 2022.
Todos os direitos reservados.

Faça um benchmark dos programas comparando-os em entradas de diferentes tamanhos.
"""
import os
import timeit
from abc import ABCMeta, abstractmethod
from collections import Counter

import oop_code
import performance_code
import simple_code
from utils.argv import ParserArgv
from utils.profile import profile


class AbstractBenchmark(metaclass=ABCMeta):
    _source_file = ""
    _ngram = ""

    @profile(repeat=1, number=0)
    def execute_simple_code(self):
        simple_code.execute(self._source_file, self._ngram)
        return self

    @profile(repeat=1, number=0)
    def execute_performance_code(self):
        performance_code.execute(self._source_file, self._ngram)
        return self

    @profile(repeat=1, number=0)
    def execute_oop_code(self):
        info = ParserArgv([f'source_file={self._source_file}', f'n_gram={self._ngram}']).parse()
        oop_code.exec_oop_code(info)
        return self

    @abstractmethod
    def execute(self):
        pass


class Benchmark(AbstractBenchmark):
    melhor = ""

    def execute(self):
        resultados = dict()
        resultados['simple_code'] = min(
            timeit.Timer(lambda: self.execute_simple_code()).repeat(repeat=1, number=0))
        resultados['performance_code'] = min(
            timeit.Timer(lambda: self.execute_performance_code()).repeat(repeat=1, number=0))
        resultados['oop_code'] = min(
            timeit.Timer(lambda: self.execute_oop_code()).repeat(repeat=1, number=0))
        self.melhor = sorted(resultados, key=resultados.get)[0]
        print("--------------------------------------------------------------------------------------------")
        print(f'TESTE: {self.__class__.__name__}')
        print('Tempo de Execução dos programas: ')
        print(f'- simple_code ....: {resultados["simple_code"]:.21f}')
        print(f'- performance_code: {resultados["performance_code"]:.21f}')
        print(f'- oop_code .......: {resultados["oop_code"]:.21f}')
        print(f'O programa mais rápido foi o {self.melhor} com {resultados[self.melhor]:.21f}')
        print("--------------------------------------------------------------------------------------------")
        return self


class BenchmarkTexto1Ngram1(Benchmark):
    _source_file = os.path.normpath("./texto.txt")
    _ngram = 1


class BenchmarkTexto1Ngram2(Benchmark):
    _source_file = os.path.normpath("./texto.txt")
    _ngram = 2


class BenchmarkTexto1Ngram3(Benchmark):
    _source_file = os.path.normpath("./texto.txt")
    _ngram = 3


class BenchmarkTexto2Ngram1(Benchmark):
    _source_file = os.path.normpath("./texto_2.txt")
    _ngram = 1


class BenchmarkTexto2Ngram2(Benchmark):
    _source_file = os.path.normpath("./texto_2.txt")
    _ngram = 2


class BenchmarkTexto2Ngram3(Benchmark):
    _source_file = os.path.normpath("./texto_2.txt")
    _ngram = 3


class BenchmarkTexto3Ngram1(Benchmark):
    _source_file = os.path.normpath("./texto_3.txt")
    _ngram = 1


class BenchmarkTexto3Ngram2(Benchmark):
    _source_file = os.path.normpath("./texto_3.txt")
    _ngram = 2


class BenchmarkTexto3Ngram3(Benchmark):
    _source_file = os.path.normpath("./texto_3.txt")
    _ngram = 3


if __name__ == '__main__':
    classes = [
        BenchmarkTexto1Ngram1, BenchmarkTexto1Ngram2, BenchmarkTexto1Ngram3,
        BenchmarkTexto2Ngram1, BenchmarkTexto2Ngram2, BenchmarkTexto2Ngram3,
        BenchmarkTexto3Ngram1, BenchmarkTexto3Ngram2, BenchmarkTexto3Ngram3
    ]
    melhores = []
    for cls in classes:
        melhores.append(cls().execute().melhor)

    print(Counter(melhores))
