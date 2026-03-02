from typing import Optional

from domain.value_objects.dimensions import Dimensions
from domain.value_objects.prices import Prices
from ..furniture import Furniture


class Bed(Furniture):
    def __init__(
            self,
            item_id: int,
            title: str,
            collection: Optional[str],
            dimensions: Dimensions,
            prices: Prices,
            fabric_consumption: float,
            spm: Optional[str],
            mechanism: Optional[str],
            box: Optional[str]
        ):
        super().__init__(item_id, title, collection, dimensions, prices, fabric_consumption)
        self.spm = spm
        self.mechanism = mechanism
        self.box = box
