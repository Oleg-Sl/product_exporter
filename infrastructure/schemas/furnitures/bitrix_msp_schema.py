from typing import Optional
from pydantic import BaseModel, Field

# 172
class BitrixMspSchema(BaseModel):
    item_id: int = Field(..., alias='id')
    title: str = Field(..., alias='ufCrm23_1707374226')
    collection: Optional[int]  = Field(..., alias='ufCrm23_1733553184')
    width: Optional[int] = Field(..., alias='ufCrm23_1706603192')
    height: Optional[int] = Field(..., alias='ufCrm23_1712408686')
    depth: Optional[int] = None
