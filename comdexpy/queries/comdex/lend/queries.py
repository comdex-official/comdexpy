from grpclib.client import Channel

from typing import List

from comdexpy.proto.cosmos.base.query.v1beta1 import PageRequest


from comdexpy.proto.comdex.lend.v1beta1 import (
    Params, 
    QueryParamsRequest, 
    QueryLendRequest,
    LendAsset,
    QueryLendsResponse,
    QueryLendsRequest,
    QueryAllLendByOwnerRequest,
    QueryAllLendByOwnerResponse,
    QueryAllLendByOwnerAndPoolRequest,
    QueryAllLendByOwnerAndPoolResponse,
    QueryPairsRequest,
    ExtendedPair,
    QueryPairRequest,
    QueryPairsResponse,
    QueryAssetRatesParamsRequest,
    QueryAssetRatesParamsResponse,
    QueryAssetRatesParamRequest,
    AssetRatesParams,
    QueryPoolsRequest,
    QueryPoolsResponse,
    QueryPoolRequest,
    Pool,
    QueryAssetToPairMappingsRequest,
    QueryAssetToPairMappingsResponse,
    QueryAssetToPairMappingRequest,
    AssetToPairMapping,
    QueryBorrowsRequest,
    QueryBorrowsResponse,
    QueryBorrowRequest,
    BorrowAsset,
    QueryAllBorrowByOwnerRequest,
    QueryAllBorrowByOwnerResponse,
    QueryAllBorrowByOwnerAndPoolRequest,
    QueryAllBorrowByOwnerAndPoolResponse,
    QueryPoolAssetLbMappingRequest,
    PoolAssetLbMapping,
    QueryReserveBuybackAssetDataRequest,
    ReserveBuybackAssetData,
    QueryAuctionParamRequest,
    AuctionParams,
    QueryModuleBalanceRequest,
    ModuleBalance,
    QueryFundModBalRequest,
    ModBal,
    QueryFundReserveBalRequest,
    ReserveBal,
    QueryAllReserveStatsRequest,
    AllReserveStats,
    QueryFundModBalByAssetPoolRequest,
    QueryFundModBalByAssetPoolResponse,
    QueryLendInterestRequest,
    PoolInterest,
    QueryBorrowInterestRequest,
    PoolInterestB


)
from comdexpy.proto.comdex.lend.v1beta1 import QueryStub as LendQueryStub


class Query():
    def __init__(self, channel: Channel) -> None:
        self.stub_lend = LendQueryStub(channel)

    async def get_params(self) -> Params:
        
        """Gets params of lend module.

        Args: None

        Returns: Lend Module's global Parameters
        """
        resp = await self.stub_lend.params(QueryParamsRequest())
        return resp.params
    



    async def get_lend(self, id: int) -> LendAsset:
        
        """Retrieves a LendAsset object associated with a given ID.

        Args:
              id (int): The unique identifier of the LendAsset to be retrieved.


        Returns:
              The LendAsset object corresponding to the specified ID.
        """
        resp = await self.stub_lend.query_lend(QueryLendRequest(id=id))
        return resp




    async def get_lends(self, pagination: PageRequest = None) -> QueryLendsResponse:
        
        """Retrieves a list of lends from the server, using the provided pagination settings if available.

        Args:
              pagination (PageRequest, optional): An instance of the PageRequest class, containing pagination settings such as the current page number and the number of items per page. Defaults to None.
        
        Returns:
              An instance of the QueryLendsResponse class, containing a list of lends and pagination information.
        """
        
        resp = await self.stub_lend.query_lends(QueryLendsRequest(pagination=pagination))
        return resp




    async def get_all_lend_by_owner(self, owner: str, pagination: PageRequest = None) -> QueryAllLendByOwnerResponse:
        
        """Retrieves all lend records associated with a specific owner, and returns the results with optional pagination support.

        Args:
             owner (str): The unique identifier of the owner whose lend records are to be fetched.
             pagination (PageRequest, optional): An optional pagination object to retrieve results in chunks, if desired. Defaults to None.

        Returns:
             A response object containing a list of lend records associated with the specified owner and the pagination details, if applicable.
        """
        
        resp = await self.stub_lend.query_all_lend_by_owner(QueryAllLendByOwnerRequest(owner=owner, pagination=pagination))
        return resp
    



    async def get_all_lend_by_owner_and_pool(self, owner: str, pool_id: int, pagination: PageRequest = None) -> QueryAllLendByOwnerAndPoolResponse:
        
        """Retrieves all the lending information associated with a specific owner and pool using the provided owner and pool ID.

        Args:
             owner (str): The owner's unique identifier (e.g. wallet address or user ID) for whom the lending information is to be fetched.
             pool_id (int): The unique identifier of the pool for which the lending information is to be fetched.
             pagination (PageRequest, optional): An optional pagination object to control the number of records retrieved and the starting point of the records. Defaults to None.
        
        Returns:
             A response object containing the lending information for the specified owner and pool, including any pagination details if provided.
        """
        
        resp = await self.stub_lend.query_all_lend_by_owner_and_pool(QueryAllLendByOwnerAndPoolRequest(owner=owner, pool_id=pool_id, pagination=pagination))
        return resp




    async def get_pairs(self, pagination: PageRequest = None) -> QueryPairsResponse:
        
        """Fetches the trading pairs from the server using pagination and returns the response as a QueryPairsResponse object.

        Args:
             pagination (PageRequest, optional): An instance of the PageRequest object containing pagination information such as the start key and limit. Default is None, which means no pagination is applied.
        
        Returns:
        An instance of the QueryPairsResponse object containing a list of trading pairs and pagination details, if applicable.
        """
        
        resp = await self.stub_lend.query_pairs(QueryPairsRequest(pagination=pagination))
        return resp




    async def get_pair(self, id: int) -> ExtendedPair:
        
        """Retrieve an ExtendedPair object associated with the given ID.

        Args:
             id (int): The unique identifier of the desired pair.


        Returns:
             An object containing information about the pair associated with the given ID.
        """
        
        resp = await self.stub_lend.query_pair(QueryPairRequest(id=id))
        return resp




    async def get_asset_rates_params(self, pagination: PageRequest = None) -> QueryAssetRatesParamsResponse:
        
        """Retrieves the asset rates parameters from the lending platform, allowing for optional pagination.

        Args:
             pagination (PageRequest, optional): An object containing pagination information, such as limit and offset, to control the number of results returned. Default is None, which retrieves all available data.
        
        Returns:
             A response object containing the asset rates parameters and any associated pagination metadata.
        """
        
        resp = await self.stub_lend.query_asset_rates_params(QueryAssetRatesParamsRequest(pagination=pagination))
        return resp




    async def get_asset_rates_param(self, id: int) -> AssetRatesParams:
        
        """Retrieves the asset rates parameters for a specified asset ID.

        Args:
             id (int): The unique identifier of the asset for which the rates parameters are to be fetched.

        Returns:
             An instance of the AssetRatesParams class containing the rates parameters for the specified asset.
        """
        
        resp = await self.stub_lend.query_asset_rates_param(QueryAssetRatesParamRequest(id=id))
        return resp




    async def get_pools(self, pagination: PageRequest = None) -> QueryPoolsResponse:
        
        """Queries the list of available lending pools and returns the results as a QueryPoolsResponse object.

        Args:
             pagination (PageRequest, optional): An object specifying the pagination options for the results.Defaults to None, which returns all results.

        Returns:
             An object containing the list of available lending pools and any relevant metadata
        """
        
        resp = await self.stub_lend.query_pools(QueryPoolsRequest(pagination=pagination))
        return resp




    async def get_pool(self, id: int) -> Pool:
        
        """Retrieves the pool information for a given pool ID. 

        Args:
             id (int): The ID of the pool for which the information is to be retrieved.

        Returns:
             An instance of the Pool class containing the retrieved pool information.

        """
        
        resp = await self.stub_lend.query_pool(QueryPoolRequest(id=id))
        return resp
    


   
    async def get_asset_to_pair_mappings(self, pagination: PageRequest = None) -> QueryAssetToPairMappingsResponse:
        
        """Retrieves the asset-to-pair mappings from the underlying service. It takes an optional pagination argument and returns the mappings as a response object.

        Args:
             pagination (PageRequest, optional): An optional pagination object containing the pagination details such as the limit and offset for the requested data.

        Returns:
             A response object containing the asset-to-pair mappings along with any associated metadata.
        """
        
        resp = await self.stub_lend.query_asset_to_pair_mappings(QueryAssetToPairMappingsRequest(pagination=pagination))
        return resp
    


   
    async def get_asset_to_pair_mapping(self, asset_id: int, pool_id: int) -> AssetToPairMapping:
        
        """Retrieves the mapping of a specific asset to a trading pair in a pool.


        Args:
             asset_id (int): The unique identifier of the asset.
             pool_id (int): The unique identifier of the liquidity pool.
       
        Returns:
             An instance of the AssetToPairMapping data structure containing the mapping information for the given asset and pool.
        """
        
        resp = await self.stub_lend.query_asset_to_pair_mapping(QueryAssetToPairMappingRequest(asset_id=asset_id, pool_id=pool_id))
        return resp
    


    
    async def get_borrows(self, pagination: PageRequest = None) -> QueryBorrowsResponse:
        
        """Retrieves a list of borrows from the lending service using the provided pagination information.


        Args:
             pagination (PageRequest, optional): An object containing pagination information (e.g., limit, offset) for querying the borrows. Default is None.

        Returns:  
             An object containing the list of borrows and additional pagination details
    
        """
        
        resp = await self.stub_lend.query_borrows(QueryBorrowsRequest(pagination=pagination))
        return resp



    
    async def get_borrow(self, id: int) -> BorrowAsset:
        
        """Fetch the borrow asset information using the given ID and return the corresponding BorrowAsset object.

        Args:
             id (int): The unique identifier of the borrow asset to be fetched.

        Returns:
             An instance of the BorrowAsset class containing the fetched borrow asset information.
        """
        
        resp = await self.stub_lend.query_borrow(QueryBorrowRequest(id=id))
        return resp




    async def get_all_borrow_by_owner(self, owner: str, pagination: PageRequest = None) -> QueryAllBorrowByOwnerResponse:
        
        """Retrieves all borrow records associated with a given owner, with optional pagination support.


        Args:
             owner (str): The owner for which to retrieve the borrow records.
             pagination (PageRequest, optional): A pagination object containing information for paginating the results. Defaults to None.
        
        Returns:
             A response object containing a list of borrow records associated with the specified owner and pagination information, if applicable.
        """
        
        resp = await self.stub_lend.query_all_borrow_by_owner(QueryAllBorrowByOwnerRequest(owner=owner, pagination=pagination))
        return resp
    



    async def get_all_borrow_by_owner_and_pool(self, owner: str, pool_id: int, pagination: PageRequest = None) -> QueryAllBorrowByOwnerAndPoolResponse:
        
        """Queries the lending service for all borrow records associated with a given owner and pool.The results can be paginated by providing an optional pagination parameter.
        
        Args:
             owner (str): The owner's address in string format.
             pool_id (int): The unique identifier of the pool.
             pagination (PageRequest, optional): A pagination object specifying the desired number of results per page and the key for the starting point. Defaults to None.

        Returns:
             A response object containing a list of borrow records and pagination information.

        """
        
        resp = await self.stub_lend.query_all_borrow_by_owner_and_pool(QueryAllBorrowByOwnerAndPoolRequest(owner=owner, pool_id=pool_id, pagination=pagination))
        return resp
    



    async def get_pool_asset_lb_mapping(self, asset_id: int, pool_id: int) -> PoolAssetLbMapping:
        
        """Get the mapping of pool assets to liquidity balances for a specific asset and pool.

        Args:
             asset_id (int): The unique identifier for the asset in the pool.
             pool_id (int): The unique identifier for the pool.

        Returns:
             An object containing the mapping of assets to liquidity balances for the specified asset and pool.
        """
        resp = await self.stub_lend.query_pool_asset_lb_mapping(QueryPoolAssetLbMappingRequest(asset_id=asset_id, pool_id=pool_id))
        return resp
    



    async def get_reserve_buyback_asset_data(self, asset_id: int) -> ReserveBuybackAssetData:
        
        """Retrieves the reserve buyback asset data for a given asset ID.

        Args:
             asset_id (int): The unique identifier of the asset for which the reserve buyback asset data is to be retrieved.
        
        Returns:
             An object containing the reserve buyback asset data for the specified asset ID.
        """
        resp = await self.stub_lend.query_reserve_buyback_asset_data(QueryReserveBuybackAssetDataRequest(asset_id=asset_id))
        return resp 
    



    async def get_auction_param(self, app_id: int) -> AuctionParams:
        
        """Retrieves the auction parameters for a given application ID.

        Args:
             app_id (int): The application ID for which to fetch the auction parameters.

        Returns:
             An instance of the AuctionParams class, containing the fetched auction parameters for the given application ID.
        """
        resp = await self.stub_lend.query_auction_params(QueryAuctionParamRequest(app_id=app_id))
        return resp
    



    async def get_module_balance(self, pool_id: int) -> ModuleBalance:
        
        """Retrieves the balance of a specific module in a lending pool by querying the module balance using the provided 'pool_id'.

        Args:
             pool_id (int): The unique identifier of the lending pool for which the module balance is to be retrieved.

        Returns:
             An instance of the ModuleBalance class representing the balance information for the specified module in the lending pool.
        """
        resp = await self.stub_lend.query_module_balance(QueryModuleBalanceRequest(pool_id=pool_id))
        return resp
    



    async def get_fund_mod_bal(self) -> ModBal:
        
        """Get the current modified balance of the fund.

        Args:
             None

        Returns:
             The modified balance of the fund as a ModBal object.
        """
        resp = await self.stub_lend.query_fund_mod_bal(QueryFundModBalRequest())
        return resp
    



    async def get_fund_reserve_bal(self) -> ReserveBal:
        
        """Retrieves the balance information of the fund reserve.

        Args:
             None

        Returns:
             An instance of the ReserveBal class containing the balance details of the fund reserve.
        """
        resp = await self.stub_lend.query_fund_reserve_bal(QueryFundReserveBalRequest())
        return resp
    



    async def get_all_reserve_stats(self, asset_id: int) -> AllReserveStats:
        
        """Fetches and returns all reserve statistics for the given asset ID.

        Args:
             asset_id (int): The unique identifier of the asset for which to retrieve reserve statistics.

        Returns:
             An object containing all reserve statistics related to the specified asset.
        """
        resp = await self.stub_lend.query_all_reserve_stats(QueryAllReserveStatsRequest(asset_id=asset_id))
        return resp
    



    async def get_fund_mod_bal_by_asset_pool(self, asset_id: int, pool_id: int) -> QueryFundModBalByAssetPoolResponse:
        
        """Retrieves the modified balance of a specific asset in a given asset pool from the lending platform.

        
        Args:
             asset_id (int): The unique identifier of the asset to query.
             pool_id (int): The unique identifier of the asset pool to query.

        Returns:
             A response object containing the modified balance of the specified asset in the given asset pool.
        """
        resp = await self.stub_lend.query_fund_mod_bal_by_asset_pool(QueryFundModBalByAssetPoolRequest(asset_id=asset_id, pool_id=pool_id))
        return resp
    



    async def get_lend_interest(self) -> PoolInterest:
        
        """Retrieves the current lending interest rate from the pool.

        Args:
             None
       
        Returns:
             An instance of the PoolInterest class containing the lending interest rate information from the pool.
        
        """
        resp = await self.stub_lend.query_lend_interest(QueryLendInterestRequest())
        return resp
    



    async def get_borrow_interest(self) -> PoolInterestB:
        
        """Retrieves the current borrow interest rate for a lending pool.

        Args:
             None

        Returns:
             An instance of the 'PoolInterestB' class containing the current borrow interest rate information.
        """
        resp = await self.stub_lend.query_borrow_interest(QueryBorrowInterestRequest())
        return resp
    


