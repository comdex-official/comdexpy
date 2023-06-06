from grpclib.client import Channel

from comdexpy.proto.cosmos.base.query.v1beta1 import PageRequest

from comdexpy.proto.comdex.esm.v1beta1 import (
    QueryParamsRequest,
    Params,
    QueryEsmTriggerParamsRequest,
    EsmTriggerParams,
    QueryEsmStatusRequest,
    EsmStatus,
    QueryCurrentDepositStatsRequest,
    CurrentDepositStats,
    QueryUsersDepositMappingRequest,
    UsersDepositMapping,
    QueryDataAfterCoolOffRequest,
    DataAfterCoolOff,
    QuerySnapshotPriceRequest,
    QuerySnapshotPriceResponse,
    QueryAssetDataAfterCoolOffRequest,
    AssetToAmount
)
from comdexpy.proto.comdex.esm.v1beta1 import QueryStub as ESMQueryStub


class Query():
    def __init__(self, channel: Channel) -> None:
        self.stub_esm = ESMQueryStub(channel)

    async def get_params(self) -> Params:
        
        """Get the parameters for a specific entity.

        Args: 
             The instance of the class.

        Returns: 
             The parameters for the entity.
        """
        resp = await self.stub_esm.params(QueryParamsRequest())
        return resp.params



    async def get_esm_trigger_params(self, id: int) -> EsmTriggerParams:
        
        """Get the trigger parameters for a specific ESM trigger.


        Args:
             id (int): The ID of the ESM trigger to retrieve the parameters for.

        Returns:
             EsmTriggerParams: The trigger parameters for the specified ESM trigger.
        """
        resp = await self.stub_esm.query_esm_trigger_params(QueryEsmTriggerParamsRequest(id=id))
        return resp




    async def get_esm_status(self, id: int) -> EsmStatus:
        
        """Get the status of an ESM with a given ID.

        Args:
             id (int): The ID of the ESM to query.

        Returns:
             EsmStatus: The status of the ESM.
        """
        
        resp = await self.stub_esm.query_esm_status(QueryEsmStatusRequest(id=id))
        return resp




    async def get_current_deposit_stats(self, id: int) -> CurrentDepositStats:
        
        """Get the current deposit statistics for a given ID.

        Args:
             id (int): The ID of the entity to retrieve deposit statistics for.

        Returns:
             CurrentDepositStats: The current deposit statistics for the specified ID.
        """
        
        resp = await self.stub_esm.query_current_deposit_stats(QueryCurrentDepositStatsRequest(id=id))
        return resp
    



    async def get_users_deposit_mapping(self, id: int, depositor: str) -> UsersDepositMapping:
        
        """Get the deposit mapping for the specified user.

        Args:
             id (int): The ID of the user.
             depositor (str): The name of the depositor.

        Returns:
              UsersDepositMapping: The deposit mapping information for the specified user.
        """
        
        resp = await self.stub_esm.query_users_deposit_mapping(QueryUsersDepositMappingRequest(id=id, depositor=depositor))
        return resp




    async def get_data_after_cool_off(self, id: int) -> DataAfterCoolOff:
        
        """Get data after cool off period for a given id.

        Args:
             id (int): The id of the data to retrieve.


        Returns:
             DataAfterCoolOff: The data after the cool off period for the given id.

        """
        
        resp = await self.stub_esm.query_data_after_cool_off(QueryDataAfterCoolOffRequest(id=id))
        return resp



    
    async def get_snapshot_price(self, app_id: int, asset_id: int) -> QuerySnapshotPriceResponse:
        
        """Get the snapshot price for a given ID and asset ID.

        Args:
             id (int): The ID of the snapshot.
             asset_id (int): The ID of the asset.


        Returns:
             QuerySnapshotPriceResponse: The response object containing the snapshot price information.

        """
        
        resp = await self.stub_esm.query_snapshot_price(QuerySnapshotPriceRequest(app_id=app_id, asset_id=asset_id))
        return resp
    



    async def get_asset_data_after_cool_off(self, app_id: int) -> AssetToAmount:
        
        """Retrieve asset data after cool-off period.

        Args:
             app_id (int): The ID of the application to retrieve data for.


        Returns:
             AssetToAmount: A named tuple containing the asset data.

        """
        
        resp = await self.stub_esm.query_asset_data_after_cool_off(QueryAssetDataAfterCoolOffRequest(app_id=app_id))
        return resp
    

