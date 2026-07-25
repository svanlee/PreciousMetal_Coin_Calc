"""Melt value calculations."""

from . import conversions
from .coins import COIN_REFERENCE


def calculate_melt(pure_troy_oz: float, qty: int, spot_price: float) -> float:
    return pure_troy_oz * qty * spot_price


def melt_from_weight(weight_troy_oz: float, purity: float, qty: int, spot_price: float) -> float:
    """For a raw scale weight + fineness (e.g. manual entry), not a COIN_REFERENCE lookup."""
    return weight_troy_oz * purity * qty * spot_price


def melt_from_grams(grams: float, purity: float, spot_price: float) -> float:
    return conversions.grams_to_troy_oz(grams) * purity * spot_price


def melt_for_coin(coin_key: str, qty: int, spot_price: float) -> float:
    coin = COIN_REFERENCE[coin_key]
    return calculate_melt(coin.pure_troy_oz, qty, spot_price)
