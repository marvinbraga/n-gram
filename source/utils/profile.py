# coding=utf-8

"""
R-GRAM Challenger - Test Software Engineer.
Marcus Vinicius Braga, 2022.
Todos os direitos reservados.
"""

import cProfile
import io
import pstats


def profile(fnc):
    """
    A deco tha uses cProfile to profile a function.
    :param fnc:
    :return:
    """

    def inner(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()
        try:
            retval = fnc(*args, **kwargs)
        finally:
            pr.disable()
            s = io.StringIO()
            ps = pstats.Stats(pr, stream=s).sort_stats("cumulative")
            ps.print_stats()
            print(s.getvalue())
        return retval

    return inner
