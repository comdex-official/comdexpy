from grpclib.client import Channel
from comdexpy.proto.comdex.liquidity.v1beta1 import (
    Params, 
    QueryParamsRequest, 
    GenericParams, 
    QueryGenericParamsRequest
)
from comdexpy.proto.comdex.liquidity.v1beta1 import QueryStub as LiquidityQueryStub


class Query():
    def __init__(self, channel: Channel) -> None:
        self.stub_liquidity = LiquidityQueryStub(channel)

    async def get_params(self) -> Params:
        """Gets params of liquidity module.

        Args: None

        Returns: Liquidity Module's global Parameters
        """
        resp = await self.stub_liquidity.params(QueryParamsRequest())
        return resp.params

    async def get_generic_params(self, app_id: int) -> GenericParams:
        """Gets generic params of liquidity module for specific App ID.

        Args: None

        Returns: Liquidity Module's App Parameters
        """
        resp = await self.stub_liquidity.generic_params(QueryGenericParamsRequest(app_id=app_id))
        return resp.params
