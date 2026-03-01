from dataclasses import dataclass

from .value_objects.dimensions import Dimensions
from .value_objects.prices import Prices


class Furniture:
    def __init__(self, item_id: int, title: str, collection: str, dimensions: Dimensions, prices: Prices, fabric_consumption: float):
        self.id = item_id
        self.title = title
        self.collection = collection
        self.dimensions = dimensions
        self.prices = prices
        self.fabric_consumption = fabric_consumption
 
    def __str__(self):
        return f"{self.title} ({self.dimensions.width}x{self.dimensions.height}x{self.dimensions.depth})"
