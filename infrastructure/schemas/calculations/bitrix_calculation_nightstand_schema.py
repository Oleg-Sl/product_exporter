from typing import Optional
from pydantic import BaseModel, Field

# 170
class BitrixCalculationNightstandSchema(BaseModel):
    material_cost: Optional[float] = Field(..., alias='ufCrm79_1714100309')
    total_cost: Optional[float] = Field(..., alias='ufCrm79_1733206043')
    fabric_consumption_1: Optional[float] = Field(..., alias='ufCrm79_1714099581')
