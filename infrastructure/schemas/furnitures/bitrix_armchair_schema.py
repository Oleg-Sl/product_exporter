from typing import Optional
from pydantic import BaseModel, Field

# 165
class BitrixArmchairSchema(BaseModel):
    item_id: int = Field(..., alias='id')
    title: str = Field(..., alias='ufCrm57_1713504224')
    collection: Optional[int]  = Field(..., alias='ufCrm57_1733553271') 
    width: Optional[int] = Field(..., alias='ufCrm57_1713504591')
    height: Optional[int] = Field(..., alias='ufCrm57_1713504631')
    depth: Optional[int] = Field(..., alias='ufCrm57_1713504619')
