from typing import Optional
from pydantic import BaseModel, Field

# 132
class BitrixCalculationTableSchema(BaseModel):
    material_cost: Optional[float] = Field(..., alias='ufCrm81_1714102558')
    total_cost: Optional[float] = Field(..., alias='ufCrm81_1733206085')
    fabric_consumption_1: Optional[float] = Field(..., alias='ufCrm81_1714101977')
