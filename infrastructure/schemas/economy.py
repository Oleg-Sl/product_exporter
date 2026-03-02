from typing import Optional
from pydantic import BaseModel, Field

# 1074
class BitrixEconomySchema(BaseModel):
    base_margin: Optional[float] = Field(..., alias='ufCrm105_1732552401')
    base_price: Optional[float] = Field(..., alias='ufCrm105_1732553260')
    
    base_plus_margin: Optional[float] = Field(..., alias='ufCrm105_1732553141')
    base_plus_price: Optional[float] = Field(..., alias='ufCrm105_1732553289')
    
    premium_margin: Optional[float] = Field(..., alias='ufCrm105_1732553153')
    premium_price: Optional[float] = Field(..., alias='ufCrm105_1732553302')
    
    premium_plus_margin: Optional[float] = Field(..., alias='ufCrm105_1732553175')
    premium_plus_price: Optional[float] = Field(..., alias='ufCrm105_1732553328')
    
    limited_margin: Optional[float] = Field(..., alias='ufCrm105_1732553214')
    limited_price: Optional[float] = Field(..., alias='ufCrm105_1732553340')
