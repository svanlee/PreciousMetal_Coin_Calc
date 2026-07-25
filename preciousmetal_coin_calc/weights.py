"""Gross mint weight/tolerance/diameter specs, for counterfeit weight verification.

Figures are standard published mint specifications. Coin content-value math
lives in coins.py/melt.py — this module is only for physical weight checks.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class CoinSpec:
    weight_g: float
    tolerance_g: float
    diameter_mm: float | None = None


COIN_SPECS: dict[str, CoinSpec] = {
    "morgan_dollar": CoinSpec(26.73, 0.30, 38.1),
    "peace_dollar": CoinSpec(26.73, 0.30, 38.1),
    "walking_liberty_half": CoinSpec(12.50, 0.20, 30.6),
    "franklin_half": CoinSpec(12.50, 0.20, 30.6),
    "barber_half": CoinSpec(12.50, 0.20, 30.6),
    "seated_liberty_half": CoinSpec(12.50, 0.20, 30.6),
    "kennedy_half_1964": CoinSpec(12.50, 0.20, 30.6),
    "kennedy_half_1965_1970": CoinSpec(11.50, 0.20, 30.6),
    "washington_quarter": CoinSpec(6.25, 0.15, 24.3),
    "standing_liberty_quarter": CoinSpec(6.25, 0.15, 24.3),
    "barber_quarter": CoinSpec(6.25, 0.15, 24.3),
    "mercury_dime": CoinSpec(2.50, 0.10, 17.9),
    "roosevelt_dime_silver": CoinSpec(2.50, 0.10, 17.9),
    "barber_dime": CoinSpec(2.50, 0.10, 17.9),
    "war_nickel": CoinSpec(5.00, 0.10, 21.2),
    "silver_round_1oz": CoinSpec(31.10, 0.50),
    "silver_bar_1oz": CoinSpec(31.10, 0.50),
    "american_silver_eagle": CoinSpec(31.10, 0.10, 40.6),
    "canadian_maple_leaf_silver": CoinSpec(31.10, 0.15, 38.0),
    "american_gold_eagle_1oz": CoinSpec(33.93, 0.25, 32.7),
    "american_gold_eagle_1_2oz": CoinSpec(16.97, 0.20, 27.0),
    "american_gold_eagle_1_4oz": CoinSpec(8.48, 0.15, 22.0),
    "american_gold_eagle_1_10oz": CoinSpec(3.39, 0.10, 16.5),
    "american_gold_buffalo": CoinSpec(31.11, 0.10, 32.7),
    "krugerrand": CoinSpec(33.93, 0.25, 32.6),
    "canadian_maple_leaf_gold": CoinSpec(31.10, 0.10, 30.0),
    "american_platinum_eagle": CoinSpec(31.12, 0.10, 32.7),
    "canadian_palladium_maple_leaf": CoinSpec(31.10, 0.10, 30.0),
    "trade_dollar": CoinSpec(27.22, 0.30, 38.1),
    "eisenhower_dollar_40pct": CoinSpec(24.59, 0.25, 38.1),
    "bicentennial_quarter_40pct": CoinSpec(5.75, 0.15, 24.3),
    "bicentennial_half_40pct": CoinSpec(11.50, 0.20, 30.6),
    "bicentennial_dollar_40pct": CoinSpec(24.59, 0.25, 38.1),
    "gold_double_eagle": CoinSpec(33.436, 0.25, 34.0),
    "gold_eagle_10": CoinSpec(16.718, 0.20, 27.0),
    "gold_half_eagle_5": CoinSpec(8.359, 0.15, 21.6),
    "gold_quarter_eagle_2_5": CoinSpec(4.18, 0.10, 18.0),
    "gold_dollar_1": CoinSpec(1.672, 0.05, 13.0),
    "british_sovereign": CoinSpec(7.988, 0.10, 22.05),
    "austrian_philharmonic_gold": CoinSpec(31.14, 0.10, 37.0),
    "austrian_philharmonic_silver": CoinSpec(31.10, 0.15, 37.0),
    "chinese_gold_panda_1oz": CoinSpec(31.10, 0.15, 40.0),
    "mexican_silver_libertad": CoinSpec(31.10, 0.15, 40.0),
}

PASS = "PASS"
MARGINAL = "MARGINAL"
UNDERWEIGHT_SUSPECT = "UNDERWEIGHT_SUSPECT"
OVERWEIGHT_SUSPECT = "OVERWEIGHT_SUSPECT"


def check_weight_tolerance(coin_key: str, actual_weight_g: float) -> str:
    spec = COIN_SPECS[coin_key]
    diff = actual_weight_g - spec.weight_g
    if abs(diff) <= spec.tolerance_g * 0.5:
        return PASS
    if abs(diff) <= spec.tolerance_g:
        return MARGINAL
    return UNDERWEIGHT_SUSPECT if diff < 0 else OVERWEIGHT_SUSPECT
