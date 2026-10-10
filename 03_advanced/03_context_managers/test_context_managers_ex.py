import os
import time

import pytest

from context_managers_ex import Timer, cd, suppress_errors


def test_timer_measures_time():
    with Timer() as t:
        time.sleep(0.05)
    assert 0.04 < t.elapsed < 0.5


def test_timer_records_time_even_on_error():
    with pytest.raises(ValueError):
        with Timer() as t:
            raise ValueError("x")
    assert t.elapsed >= 0


def test_suppress_errors_swallows_listed():
    with suppress_errors(KeyError, ValueError):
        raise KeyError("gone")


def test_suppress_errors_lets_others_through():
    with pytest.raises(TypeError):
        with suppress_errors(KeyError):
            raise TypeError("not suppressed")


def test_cd_changes_and_restores(tmp_path):
    before = os.getcwd()
    with cd(tmp_path):
        assert os.path.samefile(os.getcwd(), tmp_path)
    assert os.getcwd() == before


def test_cd_restores_after_error(tmp_path):
    before = os.getcwd()
    with pytest.raises(RuntimeError):
        with cd(tmp_path):
            raise RuntimeError("fail inside")
    assert os.getcwd() == before
