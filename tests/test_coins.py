import pytest

from preciousmetal_coin_calc import conversions
from preciousmetal_coin_calc.coins import COIN_REFERENCE
from preciousmetal_coin_calc.weights import COIN_SPECS


def test_every_coin_reference_has_positive_content():
    for key, coin in COIN_REFERENCE.items():
        assert coin.pure_troy_oz > 0, key
        assert 0 < coin.purity <= 1, key
        assert coin.metal in {"silver", "gold", "platinum", "palladium"}, key


@pytest.mark.parametrize(
    "coin_key",
    [
        "morgan_dollar",
        "walking_liberty_half",
        "washington_quarter",
        "mercury_dime",
        "kennedy_half_1965_1970",
        "war_nickel",
    ],
)
def test_pure_content_matches_gross_weight_times_purity(coin_key):
    """pure_troy_oz must equal gross weight (from weights.py) * fineness -- this is
    the exact bug the original apps had for junk silver (some paths multiplied by
    purity twice), so this guards against reintroducing it."""
    coin = COIN_REFERENCE[coin_key]
    spec = COIN_SPECS[coin_key]
    expected = conversions.grams_to_troy_oz(spec.weight_g) * coin.purity
    assert coin.pure_troy_oz == pytest.approx(expected, abs=0.001)


def test_bullion_coins_are_one_pure_troy_oz():
    for key in ["american_silver_eagle", "american_gold_eagle_1oz", "krugerrand"]:
        assert COIN_REFERENCE[key].pure_troy_oz == pytest.approx(1.0)
