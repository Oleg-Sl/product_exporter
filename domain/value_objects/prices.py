from dataclasses import dataclass


@dataclass(frozen=True)
class Prices:
    material_cost: float
    fot_cost: float
    total_cost: float
    base_cost: float
    base_percent: float
    base_plus_cost: float
    base_plus_percent: float
    premium_cost: float
    premium_percent: float
    premium_plus_cost: float
    premium_plus_percent: float
    limited_cost: float
    limited_percent: float
