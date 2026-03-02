from typing import Optional
from pydantic import BaseModel, Field

# 190
class BitrixCalculationBedSchema(BaseModel):
    material_cost: Optional[float] = Field(..., alias='ufCrm71_1713849381')
    total_cost: Optional[float] = Field(..., alias='ufCrm71_1733206023')
    fabric_consumption_1: Optional[float] = Field(..., alias='ufCrm71_1713848377')
    fabric_consumption_2: Optional[float] = Field(..., alias='ufCrm71_1713848392')
    fabric_consumption_3: Optional[float] = Field(..., alias='ufCrm71_1713848524')
    fabric_consumption_4: Optional[float] = Field(..., alias='ufCrm71_1713848541')
