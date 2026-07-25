"""Numismatically significant dates/varieties within the series in coins.py --
a "don't melt this one, check it first" flag list, not a pricing guide.

These are widely-cited key/semi-key dates from standard numismatic references
(e.g. PCGS CoinFacts, the Red Book). Descriptions are intentionally
qualitative rather than quoting exact mintage figures or dollar values --
verify against a current guide before making a buy/sell/melt decision based
on key-date status alone.
"""

from dataclasses import dataclass

KEY = "key"
SEMI_KEY = "semi_key"
BETTER_DATE = "better_date"


@dataclass(frozen=True)
class KeyDate:
    coin_key: str
    year: str
    mint_mark: str
    label: str
    why: str
    tier: str


KEY_DATES: list[KeyDate] = [
    # Morgan Dollar
    KeyDate("morgan_dollar", "1893", "S", "1893-S Morgan Dollar", "Lowest-mintage business strike in the series; the classic Morgan key date.", KEY),
    KeyDate("morgan_dollar", "1889", "CC", "1889-CC Morgan Dollar", "Key Carson City date; scarce with few high-grade survivors.", KEY),
    KeyDate("morgan_dollar", "1895", "", "1895 Morgan Dollar (\"King of Morgans\")", "Proof-only issue -- no confirmed business strikes are known to survive.", KEY),
    KeyDate("morgan_dollar", "1894", "", "1894 Morgan Dollar", "Low Philadelphia mintage; a genuine key date.", KEY),
    KeyDate("morgan_dollar", "1901", "", "1901 Morgan Dollar", "Common in raw counts but a serious condition rarity in mint state.", SEMI_KEY),
    # Peace Dollar
    KeyDate("peace_dollar", "1921", "", "1921 Peace Dollar", "First year of issue, high-relief design distinct from 1922 onward.", KEY),
    KeyDate("peace_dollar", "1928", "", "1928 Peace Dollar", "Lowest mintage of the series.", KEY),
    KeyDate("peace_dollar", "1934", "S", "1934-S Peace Dollar", "Scarce in high grade; a recognized semi-key.", SEMI_KEY),
    # Walking Liberty Half Dollar
    KeyDate("walking_liberty_half", "1921", "", "1921 Walking Liberty Half", "Low mintage; one of the series' three 1921 key dates.", KEY),
    KeyDate("walking_liberty_half", "1921", "D", "1921-D Walking Liberty Half", "Lowest mintage in the entire series.", KEY),
    KeyDate("walking_liberty_half", "1921", "S", "1921-S Walking Liberty Half", "Low mintage, especially scarce in higher grades.", KEY),
    KeyDate("walking_liberty_half", "1938", "D", "1938-D Walking Liberty Half", "Lowest mintage of the later-date run.", SEMI_KEY),
    # Mercury Dime
    KeyDate("mercury_dime", "1916", "D", "1916-D Mercury Dime", "The key date of the series -- lowest mintage by a wide margin.", KEY),
    KeyDate("mercury_dime", "1921", "", "1921 Mercury Dime", "Low mintage year for the series.", SEMI_KEY),
    KeyDate("mercury_dime", "1921", "D", "1921-D Mercury Dime", "Low mintage year for the series.", SEMI_KEY),
    KeyDate("mercury_dime", "1942", "", "1942/1 Mercury Dime (overdate)", "Famous overdate variety -- check under magnification before assuming a common 1942.", KEY),
    KeyDate("mercury_dime", "1942", "D", "1942/1-D Mercury Dime (overdate)", "Famous overdate variety, scarcer than the Philadelphia 1942/1.", KEY),
    # Standing Liberty Quarter
    KeyDate("standing_liberty_quarter", "1916", "", "1916 Standing Liberty Quarter", "First year of issue and by far the lowest mintage -- the series key date.", KEY),
    KeyDate("standing_liberty_quarter", "1918", "S", "1918/7-S Standing Liberty Quarter (overdate)", "Famous overdate variety; verify under magnification before assuming a common 1918-S.", KEY),
    KeyDate("standing_liberty_quarter", "1927", "S", "1927-S Standing Liberty Quarter", "Low mintage, notably scarce in high grade.", SEMI_KEY),
    # Washington Quarter (silver)
    KeyDate("washington_quarter", "1932", "D", "1932-D Washington Quarter", "First year of issue, low mintage -- a series key date.", KEY),
    KeyDate("washington_quarter", "1932", "S", "1932-S Washington Quarter", "First year of issue, low mintage -- a series key date.", KEY),
    # Barber coinage
    KeyDate("barber_quarter", "1901", "S", "1901-S Barber Quarter", "The classic Barber quarter key date -- very low mintage.", KEY),
    KeyDate("barber_dime", "1892", "S", "1892-S Barber Dime", "Low first-year-of-type mintage.", SEMI_KEY),
    # Trade Dollar
    KeyDate("trade_dollar", "1878", "CC", "1878-CC Trade Dollar", "Low Carson City mintage; a recognized key date.", KEY),
    KeyDate("trade_dollar", "1884", "", "1884 Trade Dollar", "Proof-only restrike, extremely low surviving population -- get this authenticated, do not melt.", KEY),
    KeyDate("trade_dollar", "1885", "", "1885 Trade Dollar", "Proof-only restrike, among the rarest US coins -- get this authenticated, do not melt.", KEY),
    # Gold
    KeyDate("gold_double_eagle", "1927", "D", "1927-D Double Eagle", "Nearly the entire mintage was melted -- one of the great US gold rarities. Get expert authentication before doing anything else.", KEY),
    KeyDate("gold_double_eagle", "1933", "", "1933 Double Eagle", "Never officially released; private ownership is legally restricted except for one specimen. Do not sell or melt -- consult a specialist/attorney immediately.", KEY),
    KeyDate("gold_dollar_1", "1875", "", "1875 Gold Dollar", "One of the lowest-mintage US gold dollars -- a recognized key date.", KEY),
]


def key_dates_for(coin_key: str) -> list[KeyDate]:
    return [kd for kd in KEY_DATES if kd.coin_key == coin_key]


def lookup(coin_key: str, year: str, mint_mark: str = "") -> KeyDate | None:
    for kd in KEY_DATES:
        if kd.coin_key == coin_key and kd.year == year and kd.mint_mark == (mint_mark or ""):
            return kd
    return None
