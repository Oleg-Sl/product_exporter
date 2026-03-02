from typing import Optional
from pydantic import BaseModel, Field

# 188
class BitrixNightstandSchema(BaseModel):
    item_id: int = Field(..., alias='id')
    title: str = Field(..., alias='ufCrm73_1714011680')
    collection: Optional[int]  = Field(..., alias='ufCrm73_1733553453') 
    width: Optional[int] = Field(..., alias='ufCrm73_1714011692')
    height: Optional[int] = Field(..., alias='ufCrm73_1714011726')
    depth: Optional[int] = Field(..., alias='ufCrm73_1714011704')
    size: Optional[int] = Field(..., alias='ufCrm73_1735451104')
    top: Optional[int] = Field(..., alias='ufCrm73_1736099439')
