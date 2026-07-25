"""Weight unit conversions between grams, troy ounces, and pennyweight."""

G_PER_TROY_OZ = 31.1035
DWT_PER_TROY_OZ = 20
G_PER_DWT = G_PER_TROY_OZ / DWT_PER_TROY_OZ


def grams_to_troy_oz(grams: float) -> float:
    return grams / G_PER_TROY_OZ


def troy_oz_to_grams(troy_oz: float) -> float:
    return troy_oz * G_PER_TROY_OZ


def dwt_to_troy_oz(dwt: float) -> float:
    return dwt / DWT_PER_TROY_OZ


def troy_oz_to_dwt(troy_oz: float) -> float:
    return troy_oz * DWT_PER_TROY_OZ


def grams_to_dwt(grams: float) -> float:
    return grams / G_PER_DWT


def dwt_to_grams(dwt: float) -> float:
    return dwt * G_PER_DWT
