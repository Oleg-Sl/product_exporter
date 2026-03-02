from typing import Optional
from pydantic import BaseModel, Field

# 150
class BitrixChairSchema(BaseModel):
    item_id: int = Field(..., alias='id')
    title: str = Field(..., alias='ufCrm77_1714055263')
    collection: Optional[int]  = Field(..., alias='ufCrm77_1733553532') 
    width: Optional[int] = Field(..., alias='ufCrm77_1714055274')
    height: Optional[int] = Field(..., alias='ufCrm77_1714055303')
    depth: Optional[int] = Field(..., alias='ufCrm77_1714055293')
