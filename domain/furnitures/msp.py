from domain.value_objects.dimensions import Dimensions
from domain.value_objects.prices import Prices
from ..furniture import Furniture


class Msp(Furniture):
    def __init__(self, item_id: int, title: str, collection: str, dimensions: Dimensions, prices: Prices, fabric_consumption: float):
        super().__init__(item_id, title, collection, dimensions, prices, fabric_consumption)

