from domain.furnitures.armchair import Armchair
from domain.value_objects.dimensions import Dimensions
from domain.value_objects.prices import Prices
from ..schemas.furnitures.bitrix_armchair_schema import BitrixArmchairSchema
from ..schemas.calculations.bitrix_calculation_armchair_schema import BitrixCalculationArmchairSchema
from ..schemas.economy import BitrixEconomySchema
from ..schemas.fot import BitrixFotSchema


class ArmchairMapper:
    def __init__(self, collection_mapping: dict[str, str]):
        self.collection_mapping = collection_mapping

    def map_bitrix_to_domain(
            self,
            data: BitrixArmchairSchema,
            economy_data: BitrixEconomySchema,
            fot_data: BitrixFotSchema,
            calculation_data: BitrixCalculationArmchairSchema
        ) -> Armchair:

        return Armchair(
            item_id=data.item_id,
            title=data.title,
            collection=self.collection_mapping.get(str(data.collection)) if data.collection is not None else None,
            dimensions=self._get_dimensions(data),
            fabric_consumption=self._calc_fabric_consumption(calculation_data),
            prices=self._get_prices(economy_data, fot_data, calculation_data)
        )

    def _calc_fabric_consumption(self, calculation_data: BitrixCalculationArmchairSchema) -> float:
        fabric_consumption = 0
        if calculation_data.fabric_consumption_1 is not None:
            fabric_consumption += calculation_data.fabric_consumption_1
        if calculation_data.fabric_consumption_2 is not None:
            fabric_consumption += calculation_data.fabric_consumption_2
        if calculation_data.fabric_consumption_3 is not None:
            fabric_consumption += calculation_data.fabric_consumption_3
        return fabric_consumption

    def _get_dimensions(self, data: BitrixArmchairSchema) -> Dimensions:
        return Dimensions(
            width=data.width,
            height=data.height,
            depth=data.depth
        )

    def _get_prices(self, economy_data: BitrixEconomySchema, fot_data: BitrixFotSchema, calculation_data: BitrixCalculationArmchairSchema) -> Prices:
        return Prices(
            material_cost=calculation_data.material_cost,
            fot_cost=fot_data.fot_summary,
            total_cost=calculation_data.total_cost,

            base_cost=economy_data.base_price,
            base_percent=economy_data.base_margin,
            
            base_plus_cost=economy_data.base_plus_price,
            base_plus_percent=economy_data.base_plus_margin,
            
            premium_cost=economy_data.premium_price,
            premium_percent=economy_data.premium_margin,

            premium_plus_cost=economy_data.premium_plus_price,
            premium_plus_percent=economy_data.premium_plus_margin,

            limited_cost=economy_data.limited_price,
            limited_percent=economy_data.limited_margin
        )
