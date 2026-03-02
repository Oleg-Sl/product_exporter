from typing import Optional
from pydantic import BaseModel, Field

# 191
class BitrixCalculationArmchairSchema(BaseModel):
    material_cost: Optional[float] = Field(..., alias='ufCrm59_1713842348')
    total_cost: Optional[float] = Field(..., alias='ufCrm59_1733206000')
    fabric_consumption_1: Optional[float] = Field(..., alias='ufCrm59_1713841298')
    fabric_consumption_2: Optional[float] = Field(..., alias='ufCrm59_1713841593')
    fabric_consumption_3: Optional[float] = Field(..., alias='ufCrm59_1713841603')
