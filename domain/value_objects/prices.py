from typing import Optional
from dataclasses import dataclass


@dataclass(frozen=True)
class Prices:
    material_cost: Optional[float]
    fot_cost: Optional[float]
    total_cost: Optional[float]
    
    base_cost: Optional[float]
    base_percent: Optional[float]
    
    base_plus_cost: Optional[float]
    base_plus_percent: Optional[float]
    
    premium_cost: Optional[float]
    premium_percent: Optional[float]
    
    premium_plus_cost: Optional[float]
    premium_plus_percent: Optional[float]
    
    limited_cost: Optional[float]
    limited_percent: Optional[float]
