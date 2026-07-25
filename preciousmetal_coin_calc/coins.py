"""Reference table of common coins/bullion: net (pure) metal content and fineness.

`pure_troy_oz` is the actual troy oz of pure metal a coin contains — the
figure melt value is computed from directly, no further multiplication by
purity needed. This is deliberately distinct from the gross/mint weight in
weights.py: for a 90%-silver coin, pure_troy_oz already has the 0.900
fineness baked in (it equals gross_weight_troy_oz * purity), so callers
should never multiply COIN_REFERENCE entries by purity a second time.
"""

from dataclasses import dataclass

from . import purity as p


@dataclass(frozen=True)
class CoinRef:
    name: str
    pure_troy_oz: float
    purity: float
    metal: str


COIN_REFERENCE: dict[str, CoinRef] = {
    # Pre-1965 90% silver circulating coinage
    "morgan_dollar": CoinRef("Morgan Dollar", 0.7735, p.JUNK_SILVER, "silver"),
    "peace_dollar": CoinRef("Peace Dollar", 0.7735, p.JUNK_SILVER, "silver"),
    "walking_liberty_half": CoinRef("Walking Liberty Half Dollar", 0.3617, p.JUNK_SILVER, "silver"),
    "franklin_half": CoinRef("Franklin Half Dollar", 0.3617, p.JUNK_SILVER, "silver"),
    "barber_half": CoinRef("Barber Half Dollar", 0.3617, p.JUNK_SILVER, "silver"),
    "seated_liberty_half": CoinRef("Seated Liberty Half Dollar", 0.3617, p.JUNK_SILVER, "silver"),
    "kennedy_half_1964": CoinRef("Kennedy Half Dollar (1964)", 0.3617, p.JUNK_SILVER, "silver"),
    "washington_quarter": CoinRef("Washington Quarter (pre-1965)", 0.1808, p.JUNK_SILVER, "silver"),
    "standing_liberty_quarter": CoinRef("Standing Liberty Quarter", 0.1808, p.JUNK_SILVER, "silver"),
    "barber_quarter": CoinRef("Barber Quarter", 0.1808, p.JUNK_SILVER, "silver"),
    "mercury_dime": CoinRef("Mercury Dime", 0.0723, p.JUNK_SILVER, "silver"),
    "roosevelt_dime_silver": CoinRef("Roosevelt Dime (pre-1965)", 0.0723, p.JUNK_SILVER, "silver"),
    "barber_dime": CoinRef("Barber Dime", 0.0723, p.JUNK_SILVER, "silver"),
    # Clad/reduced-silver issues
    "kennedy_half_1965_1970": CoinRef("Kennedy Half Dollar (1965-1970, 40% silver)", 0.1479, p.CLAD_40, "silver"),
    "war_nickel": CoinRef("Jefferson War Nickel (1942-1945, 35% silver)", 0.0563, p.WAR_NICKEL, "silver"),
    # Silver bullion
    "silver_round_1oz": CoinRef("1oz Silver Round", 1.000, p.BULLION_999, "silver"),
    "silver_bar_1oz": CoinRef("1oz Silver Bar", 1.000, p.BULLION_999, "silver"),
    "american_silver_eagle": CoinRef("American Silver Eagle", 1.000, p.BULLION_999, "silver"),
    "canadian_maple_leaf_silver": CoinRef("Canadian Silver Maple Leaf", 1.000, p.BULLION_9999, "silver"),
    # Gold bullion
    "american_gold_eagle_1oz": CoinRef("American Gold Eagle 1oz", 1.000, p.KRUGERRAND_GOLD, "gold"),
    "american_gold_eagle_1_2oz": CoinRef("American Gold Eagle 1/2oz", 0.500, p.KRUGERRAND_GOLD, "gold"),
    "american_gold_eagle_1_4oz": CoinRef("American Gold Eagle 1/4oz", 0.250, p.KRUGERRAND_GOLD, "gold"),
    "american_gold_eagle_1_10oz": CoinRef("American Gold Eagle 1/10oz", 0.100, p.KRUGERRAND_GOLD, "gold"),
    "american_gold_buffalo": CoinRef("American Gold Buffalo 1oz", 1.000, p.BULLION_9999, "gold"),
    "krugerrand": CoinRef("Krugerrand 1oz", 1.000, p.KRUGERRAND_GOLD, "gold"),
    "canadian_maple_leaf_gold": CoinRef("Canadian Gold Maple Leaf", 1.000, p.BULLION_9999, "gold"),
    # Platinum / palladium
    "american_platinum_eagle": CoinRef("American Platinum Eagle 1oz", 1.000, p.BULLION_9995, "platinum"),
    "canadian_palladium_maple_leaf": CoinRef("Canadian Palladium Maple Leaf 1oz", 1.000, p.BULLION_9995, "palladium"),
    # Trade dollar / early US commemorative silver
    "trade_dollar": CoinRef("Trade Dollar (1873-1885)", 0.7877, p.FINE_900, "silver"),
    # 40%-silver special-strike issues (not general circulation)
    "eisenhower_dollar_40pct": CoinRef("Eisenhower Dollar (1971-1976, 40% silver \"Blue Ike\")", 0.3163, p.CLAD_40, "silver"),
    "bicentennial_quarter_40pct": CoinRef("Bicentennial Quarter (1976, 40% silver)", 0.0740, p.CLAD_40, "silver"),
    "bicentennial_half_40pct": CoinRef("Bicentennial Half Dollar (1976, 40% silver)", 0.1479, p.CLAD_40, "silver"),
    "bicentennial_dollar_40pct": CoinRef("Bicentennial Eisenhower Dollar (1976, 40% silver)", 0.3163, p.CLAD_40, "silver"),
    # Pre-1933 US gold coinage (.900 fine)
    "gold_double_eagle": CoinRef("Gold Double Eagle ($20, Liberty/Saint-Gaudens)", 0.9675, p.FINE_900, "gold"),
    "gold_eagle_10": CoinRef("Gold Eagle ($10, pre-1933)", 0.4837, p.FINE_900, "gold"),
    "gold_half_eagle_5": CoinRef("Gold Half Eagle ($5, pre-1933)", 0.2419, p.FINE_900, "gold"),
    "gold_quarter_eagle_2_5": CoinRef("Gold Quarter Eagle ($2.50, pre-1933)", 0.1209, p.FINE_900, "gold"),
    "gold_dollar_1": CoinRef("Gold Dollar ($1, Type 1/2/3)", 0.0484, p.FINE_900, "gold"),
    # World bullion
    "british_sovereign": CoinRef("British Sovereign", 0.2354, p.KRUGERRAND_GOLD, "gold"),
    "austrian_philharmonic_gold": CoinRef("Austrian Gold Philharmonic 1oz", 1.000, p.BULLION_9999, "gold"),
    "austrian_philharmonic_silver": CoinRef("Austrian Silver Philharmonic 1oz", 1.000, p.BULLION_999, "silver"),
    "chinese_gold_panda_1oz": CoinRef("Chinese Gold Panda 1oz", 1.000, p.BULLION_999, "gold"),
    "mexican_silver_libertad": CoinRef("Mexican Silver Libertad 1oz", 1.000, p.BULLION_999, "silver"),
}
