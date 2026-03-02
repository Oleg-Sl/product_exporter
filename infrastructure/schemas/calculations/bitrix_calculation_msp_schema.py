from typing import Optional
from pydantic import BaseModel, Field

# 145
class BitrixCalculationMspSchema(BaseModel):
    material_cost: Optional[float] = Field(..., alias='ufCrm27_1708681937')
    total_cost: Optional[float] = Field(..., alias='ufCrm27_1733206071')
    fabric_consumption_1: Optional[float] = Field(..., alias='ufCrm27_1708658296')
    fabric_consumption_2: Optional[float] = Field(..., alias='ufCrm27_1708658336')
    fabric_consumption_3: Optional[float] = Field(..., alias='ufCrm27_1708658363')
