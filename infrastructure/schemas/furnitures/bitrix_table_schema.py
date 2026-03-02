from typing import Optional
from pydantic import BaseModel, Field

# 186
class BitrixTableSchema(BaseModel):
    item_id: int = Field(..., alias='id')
    title: str = Field(..., alias='ufCrm75_1714013792')
    collection: Optional[int]  = Field(..., alias='ufCrm75_1733553570') 
    width: Optional[int] = Field(..., alias='ufCrm75_1714014505')
    height: Optional[int] = Field(..., alias='ufCrm75_1714014534')
    depth: Optional[int] = Field(..., alias='ufCrm75_1714014521')
