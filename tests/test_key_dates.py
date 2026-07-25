from preciousmetal_coin_calc import KEY_DATES, COIN_REFERENCE, key_dates_for, lookup_key_date


def test_every_key_date_references_a_real_coin():
    for kd in KEY_DATES:
        assert kd.coin_key in COIN_REFERENCE, kd.label


def test_key_dates_for_morgan_dollar():
    morgans = key_dates_for("morgan_dollar")
    labels = {kd.label for kd in morgans}
    assert "1893-S Morgan Dollar" in labels
    assert len(morgans) >= 3


def test_lookup_finds_1916d_mercury_dime():
    kd = lookup_key_date("mercury_dime", "1916", "D")
    assert kd is not None
    assert kd.tier == "key"


def test_lookup_returns_none_for_common_date():
    assert lookup_key_date("mercury_dime", "1944", "") is None


def test_1933_double_eagle_flagged_key():
    kd = lookup_key_date("gold_double_eagle", "1933", "")
    assert kd is not None
    assert "legal" in kd.why.lower()
