from typing import Optional
from dataclasses import dataclass


@dataclass(frozen=True)
class Dimensions:
    width: Optional[float]
    height: Optional[float]
    depth: Optional[float]
