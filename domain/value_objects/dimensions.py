from dataclasses import dataclass


@dataclass(frozen=True)
class Dimensions:
    width: float
    height: float
    depth: float
