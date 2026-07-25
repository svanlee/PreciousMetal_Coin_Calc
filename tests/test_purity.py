from preciousmetal_coin_calc import purity


def test_named_constants_match_lookup():
    assert purity.FINENESS["junk_silver"] == purity.JUNK_SILVER
    assert purity.FINENESS["clad_40"] == purity.CLAD_40
    assert purity.FINENESS["war_nickel"] == purity.WAR_NICKEL
    assert purity.FINENESS["krugerrand_gold"] == purity.KRUGERRAND_GOLD


def test_junk_silver_value():
    assert purity.JUNK_SILVER == 0.900
