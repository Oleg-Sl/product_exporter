from typing import Optional
from pydantic import BaseModel, Field

# 167
class BitrixPoufSchema(BaseModel):
    item_id: int = Field(..., alias='id')
    title: str = Field(..., alias='ufCrm67_1713518136')
    collection: Optional[int]  = Field(..., alias='ufCrm67_1733553623')
    width: Optional[int] = Field(..., alias='ufCrm67_1713518148')
    height: Optional[int] = Field(..., alias='ufCrm67_1713518169')
    depth: Optional[int] = Field(..., alias='ufCrm67_1713518155')
    size: Optional[int] = Field(..., alias='ufCrm67_1745928494')
    mechanism: Optional[int] = Field(..., alias='ufCrm67_1713518623')
    box: Optional[int] = Field(..., alias='ufCrm67_1713518573')
