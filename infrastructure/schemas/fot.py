from pydantic import BaseModel, Field

# 1048
class BitrixFotSchema(BaseModel):
    fot_summary: float = Field(..., alias='ufCrm93_1750821799')
