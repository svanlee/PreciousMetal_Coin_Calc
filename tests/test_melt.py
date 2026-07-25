import pytest

from preciousmetal_coin_calc import melt


def test_calculate_melt():
    assert melt.calculate_melt(pure_troy_oz=1.0, qty=1, spot_price=32.0) == pytest.approx(32.0)


def test_calculate_melt_with_qty():
    assert melt.calculate_melt(pure_troy_oz=0.7735, qty=10, spot_price=32.0) == pytest.approx(247.52)


def test_melt_from_weight():
    # pre-1965 quarter: 0.1808 gross troy oz-equivalent weight * 0.900 purity
    result = melt.melt_from_weight(weight_troy_oz=0.2009, purity=0.900, qty=1, spot_price=32.0)
    assert result == pytest.approx(5.786, abs=0.01)


def test_melt_from_grams():
    result = melt.melt_from_grams(grams=31.1035, purity=0.999, spot_price=32.0)
    assert result == pytest.approx(31.968, abs=0.01)


def test_melt_for_coin_american_silver_eagle():
    assert melt.melt_for_coin("american_silver_eagle", qty=1, spot_price=32.0) == pytest.approx(32.0)


def test_melt_for_coin_morgan_dollar():
    assert melt.melt_for_coin("morgan_dollar", qty=1, spot_price=32.0) == pytest.approx(24.752, abs=0.01)
