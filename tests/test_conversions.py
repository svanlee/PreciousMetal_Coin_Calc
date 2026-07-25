import pytest

from preciousmetal_coin_calc import conversions


def test_grams_to_troy_oz():
    assert conversions.grams_to_troy_oz(31.1035) == pytest.approx(1.0)


def test_troy_oz_to_grams():
    assert conversions.troy_oz_to_grams(1.0) == pytest.approx(31.1035)


def test_dwt_roundtrip():
    assert conversions.dwt_to_troy_oz(20) == pytest.approx(1.0)
    assert conversions.troy_oz_to_dwt(1.0) == pytest.approx(20)


def test_grams_dwt_roundtrip():
    grams = 15.55175
    dwt = conversions.grams_to_dwt(grams)
    assert conversions.dwt_to_grams(dwt) == pytest.approx(grams)
