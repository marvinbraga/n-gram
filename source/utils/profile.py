# coding=utf-8

"""
R-GRAM Challenger - Test Software Engineer.
Marcus Vinicius Braga, 2022.
Todos os direitos reservados.
"""

import cProfile
import io
import pstats
import timeit
from datetime import datetime, timedelta
from functools import wraps

from string import Template


class DeltaTemplate(Template):
    delimiter = "%"


class TimeDelta:

    @staticmethod
    def strfdelta(time_delta, fmt):
        d = {"D": time_delta.days}
        hours, rem = divmod(time_delta.seconds, 3600)
        minutes, seconds = divmod(rem, 60)
        d["H"] = '{:02d}'.format(hours)
        d["M"] = '{:02d}'.format(minutes)
        d["S"] = '{:02d}'.format(seconds)
        d["Z"] = '{:06d}'.format(time_delta.microseconds)
        t = DeltaTemplate(fmt)
        return t.substitute(**d)


def profile(repeat=0, number=1):
    def dec_profile(fnc):
        """
        A decorator that uses cProfile to profile a function.
        :param fnc:
        :return:
        """

        @wraps(fnc)
        def inner(*args, **kwargs):
            pr = cProfile.Profile()
            pr.enable()
            t_min, delta = 0, timedelta(0)
            try:
                retval = fnc(*args, **kwargs)
                t1 = datetime.now()
                t_min = min(timeit.Timer(lambda: fnc(*args, **kwargs)).repeat(repeat=repeat, number=number))
                delta = datetime.now() - t1
            finally:
                pr.disable()
                s = io.StringIO()
                ps = pstats.Stats(pr, stream=s).sort_stats("cumulative")
                ps.print_stats()
                print(s.getvalue())
                print(f'Minimum Time: {t_min:.6f}')
                print(f'Total Run Time: {TimeDelta.strfdelta(delta, "%H:%M:%S.%Z")}')
                print(f'Now: {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}')
            return retval

        return inner

    return dec_profile
