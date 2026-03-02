from typing import Optional

from domain.value_objects.dimensions import Dimensions
from domain.value_objects.prices import Prices
from ..furniture import Furniture


class Sofa(Furniture):
    def __init__(
            self,
            item_id: int,
            title: str,
            collection: Optional[str],
            dimensions: Dimensions,
            prices: Prices,
            fabric_consumption: float,
            shape: Optional[str],
            decor: Optional[str],
            mechanism: Optional[str]
        ):
        super().__init__(item_id, title, collection, dimensions, prices, fabric_consumption)
        self.shape = shape
        self.decor = decor
        self.mechanism = mechanism
