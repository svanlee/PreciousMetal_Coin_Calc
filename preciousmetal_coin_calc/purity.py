"""Named fineness (purity) constants for common precious metal alloys."""

FINE_900 = 0.900
JUNK_SILVER = FINE_900  # alias: 90% fineness used by pre-1965 US silver coinage
CLAD_40 = 0.400
WAR_NICKEL = 0.350
STERLING = 0.925
BULLION_999 = 0.999
BULLION_9995 = 0.9995
BULLION_9999 = 0.9999
KRUGERRAND_GOLD = 0.9167  # 22k gold alloy: Krugerrand, US Gold Eagle, British Sovereign

FINENESS = {
    "fine_900": FINE_900,
    "junk_silver": JUNK_SILVER,
    "clad_40": CLAD_40,
    "war_nickel": WAR_NICKEL,
    "sterling": STERLING,
    "bullion_999": BULLION_999,
    "bullion_9995": BULLION_9995,
    "bullion_9999": BULLION_9999,
    "krugerrand_gold": KRUGERRAND_GOLD,
}
