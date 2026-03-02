from typing import Optional
from pydantic import BaseModel, Field

# 158
class BitrixSofaSchema(BaseModel):
    item_id: int = Field(..., alias='id')
    title: str = Field(..., alias='ufCrm53_1713497057')
    collection: Optional[int]  = Field(..., alias='ufCrm53_1732093381')
    width: Optional[int] = Field(..., alias='ufCrm53_1713497093')
    height: Optional[int] = Field(..., alias='ufCrm53_1713497130')
    depth: Optional[int] = Field(..., alias='ufCrm53_1713497114')
    shape: Optional[int] = Field(..., alias='ufCrm53_1713497257')
    decor: Optional[int] = Field(..., alias='ufCrm53_1759650077')
    mechanism: Optional[int] = Field(..., alias='ufCrm53_1713497717')

