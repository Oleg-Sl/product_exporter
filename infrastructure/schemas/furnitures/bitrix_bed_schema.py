from typing import Optional
from pydantic import BaseModel, Field

# 189
class BitrixBedSchema(BaseModel):
    item_id: int = Field(..., alias='id')
    title: str = Field(..., alias='ufCrm61_1713511268')
    collection: Optional[int]  = Field(..., alias='ufCrm61_1732096195') 
    width: Optional[int] = Field(..., alias='ufCrm61_1713511299')
    height: Optional[int] = Field(..., alias='ufCrm61_1713511318')
    depth: Optional[int] = Field(..., alias='ufCrm61_1713511307')

    spm: Optional[str] = Field(..., alias='ufCrm61_1713512412')
    mechanism: Optional[int] = Field(..., alias='ufCrm61_1713512597')
    box: Optional[int] = Field(..., alias='ufCrm61_1713512938')
