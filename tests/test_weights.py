from preciousmetal_coin_calc import weights


def test_pass_at_exact_spec():
    assert weights.check_weight_tolerance("morgan_dollar", 26.73) == weights.PASS


def test_marginal_within_tolerance():
    spec = weights.COIN_SPECS["morgan_dollar"]
    edge = spec.weight_g + spec.tolerance_g * 0.9
    assert weights.check_weight_tolerance("morgan_dollar", edge) == weights.MARGINAL


def test_underweight_suspect():
    spec = weights.COIN_SPECS["mercury_dime"]
    light = spec.weight_g - spec.tolerance_g - 0.5
    assert weights.check_weight_tolerance("mercury_dime", light) == weights.UNDERWEIGHT_SUSPECT


def test_overweight_suspect():
    spec = weights.COIN_SPECS["mercury_dime"]
    heavy = spec.weight_g + spec.tolerance_g + 0.5
    assert weights.check_weight_tolerance("mercury_dime", heavy) == weights.OVERWEIGHT_SUSPECT


def test_all_coin_specs_have_positive_weight():
    for key, spec in weights.COIN_SPECS.items():
        assert spec.weight_g > 0, key
        assert spec.tolerance_g > 0, key
