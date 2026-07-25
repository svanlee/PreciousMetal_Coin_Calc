import pytest

from preciousmetal_coin_calc import premium


def test_premium_below_spot():
    assert premium.premium(price_per_oz=3348, spot_price=3365) == pytest.approx(-17)


def test_offer_tiers():
    melt_value = 100.0
    assert premium.shop_offer(melt_value) == pytest.approx(80.0)
    assert premium.buy_ticket_secondary_offer(melt_value) == pytest.approx(90.0)
    assert premium.online_value_estimate(melt_value) == pytest.approx(95.0)


@pytest.mark.parametrize(
    "total_value,expected_prefix",
    [(10, "Small"), (49.99, "Small"), (50, "Medium"), (199.99, "Medium"), (200, "Larger")],
)
def test_lot_size_advice(total_value, expected_prefix):
    assert premium.lot_size_advice(total_value).startswith(expected_prefix)


@pytest.mark.parametrize(
    "gold,silver,expected_signal",
    [(2000, 50, premium.BUY_SILVER), (3000, 50, premium.NEUTRAL), (4000, 40, premium.HIGH)],
)
def test_gold_silver_ratio_signal(gold, silver, expected_signal):
    ratio, signal = premium.gold_silver_ratio_signal(gold, silver)
    assert ratio == pytest.approx(gold / silver)
    assert signal == expected_signal


def test_gold_silver_ratio_signal_boundaries():
    _, signal_49 = premium.gold_silver_ratio_signal(49, 1)
    _, signal_50 = premium.gold_silver_ratio_signal(50, 1)
    _, signal_74 = premium.gold_silver_ratio_signal(74, 1)
    _, signal_75 = premium.gold_silver_ratio_signal(75, 1)
    assert signal_49 == premium.BUY_SILVER
    assert signal_50 == premium.NEUTRAL
    assert signal_74 == premium.NEUTRAL
    assert signal_75 == premium.HIGH
