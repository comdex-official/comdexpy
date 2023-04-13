from grpclib.client import Channel
from comdexpy.proto.cosmos.bank.v1beta1 import (
    Params,
    QueryParamsRequest, 
)
from comdexpy.proto.cosmos.bank.v1beta1 import QueryStub as BankQueryStub


class Query():
    def __init__(self, channel: Channel) -> None:
        self.stub_bank = BankQueryStub(channel)

    async def get_params(self) -> Params:
        """Get params of bank module.

        Args: None

        Returns: Bnak Module's Parameters
        """
        resp = await self.stub_bank.params(QueryParamsRequest())
        return resp.params
