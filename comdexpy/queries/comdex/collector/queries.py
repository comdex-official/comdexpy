from grpclib.client import Channel

from comdexpy.proto.cosmos.base.query.v1beta1 import PageRequest

from comdexpy.proto.comdex.collector.v1beta1 import (
    QueryParamsRequest,
    Params,
    QueryCollectorLookupByAppRequest,
    CollectorData,
    QueryCollectorLookupByAppAndAssetRequest,
    CollectorLookupTableData,
    QueryCollectorDataByAppAndAssetRequest,
    QueryAuctionMappingForAppAndAssetRequest,
    QueryNetFeeCollectedForAppAndAssetRequest,
    AppAssetIdToFeeCollectedData,
    AppAssetIdToAuctionLookupTable

)
from comdexpy.proto.comdex.collector.v1beta1 import QueryStub as CollectorQueryStub


class Query():
    def __init__(self, channel: Channel) -> None:
        self.stub_collector = CollectorQueryStub(channel)

    async def get_params(self) -> Params:
        
        """Retrieve the parameters associated with the given ID.

        Args: 
             None

        Returns: 
             Params: The parameters associated with the given ID.
        """
        resp = await self.stub_collector.params(QueryParamsRequest())
        return resp



    async def get_collector_lookup_by_app(self, app_id: int, pagination: PageRequest = None) -> CollectorLookupTableData:
        
        """Retrieves collector lookup data based on the given app ID and pagination parameters.

        Args:
             app_id (int): an integer value representing the ID of the application for which the collector lookup data needs to be retrieved.
             pagination (PageRequest): an optional object of type "PageRequest" containing parameters for pagination, such as the page number and page size.

        Returns:
             An object of type "CollectorLookupTableData" containing the collector lookup data retrieved for the specified app ID and pagination parameters.
        """
        resp = await self.stub_collector.query_collector_lookup_by_app(QueryCollectorLookupByAppRequest(app_id=app_id, pagination=pagination))
        return resp




    async def get_collector_lookup_by_app_and_asset(self, app_id: int, asset_id: int) -> CollectorLookupTableData:
        
        """Retrieves a CollectorLookupTableData object based on the provided app_id and asset_id.

        Args:
             app_id: An integer representing the ID of the application.
             asset_id: An integer representing the ID of the asset.

        Returns:
             An object containing information about the collector lookup for the specified app and asset.
        """
        
        resp = await self.stub_collector.query_collector_lookup_by_app_and_asset(QueryCollectorLookupByAppAndAssetRequest(app_id=app_id, asset_id=asset_id))
        return resp




    async def get_collector_data_by_app_and_asset(self, app_id: int, asset_id: int) -> CollectorData:
        
        """Queries collector data by app ID and asset ID using gRPC stub and returns the response.

        Args:
             app_id: integer representing the ID of the application.
             asset_id: integer representing the ID of the asset.

        Returns:
             An object containing the data collected by the collector for the given app ID and asset ID.
        """
        
        resp = await self.stub_collector.query_collector_data_by_app_and_asset(QueryCollectorDataByAppAndAssetRequest(app_id=app_id, asset_id=asset_id))
        return resp
    



    async def get_auction_mapping_for_app_and_asset(self, app_id: int, asset_id: int) -> AppAssetIdToAuctionLookupTable:
        
        """Retrieves an auction mapping lookup table for a given app and asset.

        Args:
             app_id: an integer representing the ID of the app for which the auction mapping is requested.
             asset_id: an integer representing the ID of the asset for which the auction mapping is requested.

        Returns:
              An instance of the 'AppAssetIdToAuctionLookupTable' class, which contains a mapping of auction IDs to auction metadata for the specified app and asset.
        """
        
        resp = await self.stub_collector.query_auction_mapping_for_app_and_asset(QueryAuctionMappingForAppAndAssetRequest(app_id=app_id, asset_id=asset_id))
        return resp




    async def get_net_fee_collected_for_app_and_asset(self, app_id: int, asset_id: int) -> AppAssetIdToFeeCollectedData:
        
        """Queries the net fee collected for a given app and asset from the gRPC server using the collector stub.

        Args:
             app_id (int): The ID of the application for which the net fee collected is to be queried.
             asset_id (int): The ID of the asset for which the net fee collected is to be queried.


        Returns:
             An object that contains the net fee collected for the given app and asset.

        """
        
        resp = await self.stub_collector.query_net_fee_collected_for_app_and_asset(QueryNetFeeCollectedForAppAndAssetRequest(app_id=app_id, asset_id=asset_id))
        return resp



