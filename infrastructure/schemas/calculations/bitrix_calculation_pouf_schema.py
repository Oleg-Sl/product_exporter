from typing import Optional
from pydantic import BaseModel, Field

# 148
class BitrixCalculationPoufSchema(BaseModel):
    material_cost: Optional[float] = Field(..., alias='ufCrm69_1713851296')
    total_cost: Optional[float] = Field(..., alias='ufCrm69_1733206058')
    fabric_consumption_1: Optional[float] = Field(..., alias='ufCrm69_1713850234')
    fabric_consumption_2: Optional[float] = Field(..., alias='ufCrm69_1713850312')
    fabric_consumption_3: Optional[float] = Field(..., alias='ufCrm69_1713850328')
