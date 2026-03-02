from typing import Optional
from pydantic import BaseModel, Field

# 151
class BitrixCalculationSofaSchema(BaseModel):
    material_cost: Optional[float] = Field(..., alias='ufCrm51_1713689697')
    total_cost: Optional[float] = Field(..., alias='ufCrm51_1733205956')
    fabric_consumption_1: Optional[float] = Field(..., alias='ufCrm51_1713686013')
    fabric_consumption_2: Optional[float] = Field(..., alias='ufCrm51_1713686119')
    fabric_consumption_3: Optional[float] = Field(..., alias='ufCrm51_1713686271')
    fabric_consumption_4: Optional[float] = Field(..., alias='ufCrm51_1713688409')
