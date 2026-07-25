"""Premium/offer-tier calculations and market-ratio signals."""

SHOP_BID = 0.80
BUY_TICKET_SECONDARY = 0.90
ONLINE_VALUE = 0.95

RATIO_BUY_SILVER_BELOW = 50
RATIO_NEUTRAL_BELOW = 75

BUY_SILVER = "BUY_SILVER"
NEUTRAL = "NEUTRAL"
HIGH = "HIGH"


def premium(price_per_oz: float, spot_price: float) -> float:
    return price_per_oz - spot_price


def shop_offer(melt_value: float) -> float:
    return melt_value * SHOP_BID


def buy_ticket_secondary_offer(melt_value: float) -> float:
    return melt_value * BUY_TICKET_SECONDARY


def online_value_estimate(melt_value: float) -> float:
    return melt_value * ONLINE_VALUE


def lot_size_advice(total_value: float) -> str:
    if total_value < 50:
        return "Small lot — shop offer is quickest."
    if total_value < 200:
        return "Medium lot — Facebook Marketplace near spot, no fees."
    return "Larger lot — split key dates to eBay, bulk to dealer."


def gold_silver_ratio_signal(gold_spot: float, silver_spot: float) -> tuple[float, str]:
    ratio = gold_spot / silver_spot
    if ratio < RATIO_BUY_SILVER_BELOW:
        signal = BUY_SILVER
    elif ratio < RATIO_NEUTRAL_BELOW:
        signal = NEUTRAL
    else:
        signal = HIGH
    return ratio, signal
