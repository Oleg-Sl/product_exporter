from typing import Optional
from pydantic import BaseModel, Field

# 171
class BitrixCalculationСhairSchema(BaseModel):
    material_cost: Optional[float] = Field(..., alias='ufCrm83_1714106518')
    total_cost: Optional[float] = Field(..., alias='ufCrm83_1733206105')
    fabric_consumption_1: Optional[float] = Field(..., alias='ufCrm83_1714103434')
