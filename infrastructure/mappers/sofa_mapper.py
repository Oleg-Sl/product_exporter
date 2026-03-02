from domain.furnitures.sofa import Sofa
from domain.value_objects.dimensions import Dimensions
from domain.value_objects.prices import Prices
from ..schemas.furnitures.bitrix_sofa_schema import BitrixSofaSchema
from ..schemas.calculations.bitrix_calculation_sofa_schema import BitrixCalculationSofaSchema
from ..schemas.economy import BitrixEconomySchema
from ..schemas.fot import BitrixFotSchema


class SofaMapper:
    def __init__(self, collection_mapping: dict[str, str], shape_mapping: dict[str, str], decor_mapping: dict[str, str], mechanism_mapping: dict[str, str]):
        self.collection_mapping = collection_mapping
        self.shape_mapping = shape_mapping
        self.decor_mapping = decor_mapping
        self.mechanism_mapping = mechanism_mapping

    def map_bitrix_to_domain(
            self,
            data: BitrixSofaSchema,
            economy_data: BitrixEconomySchema,
            fot_data: BitrixFotSchema,
            calculation_data: BitrixCalculationSofaSchema
        ) -> Sofa:

        return Sofa(
            item_id=data.item_id,
            title=data.title,
            collection=self.collection_mapping.get(str(data.collection)) if data.collection is not None else None,
            dimensions=self._get_dimensions(data),
            fabric_consumption=self._calc_fabric_consumption(calculation_data),
            prices=self._get_prices(economy_data, fot_data, calculation_data),
            shape=self.shape_mapping.get(str(data.shape)) if data.shape is not None else None,
            decor=self.decor_mapping.get(str(data.decor)) if data.decor is not None else None,
            mechanism=self.mechanism_mapping.get(str(data.mechanism)) if data.mechanism is not None else None
        )

    def _calc_fabric_consumption(self, calculation_data: BitrixCalculationSofaSchema) -> float:
        fabric_consumption = 0
        if calculation_data.fabric_consumption_1 is not None:
            fabric_consumption += calculation_data.fabric_consumption_1
        if calculation_data.fabric_consumption_2 is not None:
            fabric_consumption += calculation_data.fabric_consumption_2
        if calculation_data.fabric_consumption_3 is not None:
            fabric_consumption += calculation_data.fabric_consumption_3
        if calculation_data.fabric_consumption_4 is not None:
            fabric_consumption += calculation_data.fabric_consumption_4
        return fabric_consumption

    def _get_dimensions(self, data: BitrixSofaSchema) -> Dimensions:
        return Dimensions(
            width=data.width,
            height=data.height,
            depth=data.depth
        )

    def _get_prices(self, economy_data: BitrixEconomySchema, fot_data: BitrixFotSchema, calculation_data: BitrixCalculationSofaSchema) -> Prices:
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
