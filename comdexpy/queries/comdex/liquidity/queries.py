from grpclib.client import Channel
from typing import List
from comdexpy.proto.cosmos.base.query.v1beta1 import PageRequest
from comdexpy.proto.comdex.liquidity.v1beta1 import (
    Params, 
    QueryParamsRequest, 
    GenericParams, 
    QueryGenericParamsRequest,
    Pool,
    QueryPoolRequest,
    QueryPoolsRequest,
    Pair,
    QueryPairRequest,
    QueryPairsRequest,
    DepositRequest,
    QueryDepositRequestRequest,
    QueryDepositRequestsRequest,
    QueryWithdrawRequestRequest,
    WithdrawRequest,
    QueryWithdrawRequestsRequest,
    QueryOrderRequest,
    Order,
    QueryOrdersRequest,
    QueryOrderBooksRequest,
    QueryFarmerRequest,
    QueryDeserializePoolCoinRequest,
    PoolIncentive,
    QueryPoolsIncentivesRequest,
    QueryFarmedPoolCoinRequest,
    TotalActiveAndQueuedPoolCoins,
    QueryAllFarmedPoolCoinsRequest,
    QueryOrdersByOrdererRequest,
    QueryOrdersResponse,
    QueryPoolsResponse,
    QueryPairsResponse,
    QueryDepositRequestsResponse,
    QueryWithdrawRequestsResponse,
    QueryOrderBooksResponse,
    QueryFarmerResponse,
    QueryDeserializePoolCoinResponse,
    QueryFarmedPoolCoinResponse

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

        Args:
        app_id (int): The unique identifier of the App for which the liquidity module parameters are to be fetched.

        Returns:
        GenericParams: An object containing the generic parameters of the liquidity module for the specified App ID.
        """
        resp = await self.stub_liquidity.generic_params(QueryGenericParamsRequest(app_id=app_id))
        return resp




    async def get_pools(self, pair_id: int, disabled: str, app_id: int,pagination: PageRequest = None) -> QueryPoolsResponse:

        """This function retrieves the pools data of the liquidity module for a given pair ID and App ID.

        Args:
        pair_id (int): The unique identifier for the trading pair.
        disabled (bool): A flag to filter pools based on whether they are disabled or not.
        app_id (int): The unique identifier for the application requesting the data.

        Returns:
        pools: A collection of pools data from the liquidity module that match the given parameters.
        """
        
        resp = await self.stub_liquidity.pools(QueryPoolsRequest(pair_id=pair_id, disabled=disabled, app_id=app_id,pagination=pagination))
        return resp




    async def get_pool(self, pool_id: int, app_id: int) -> Pool:

        """This function retrieves the pool data of the liquidity module for a given pair ID and App ID.

        Args:
        pair_id (int): The unique identifier of the trading pair.
        app_id (int): The unique identifier of the application using the liquidity module.

        Returns:
        Pool: An instance of the Pool class containing the relevant liquidity pool data.
        """
        
        resp = await self.stub_liquidity.pool(QueryPoolRequest(pool_id=pool_id, app_id=app_id))
        return resp
    



    async def get_pair(self, pair_id: int, app_id: int) -> Pair:

        """This function retrieves the pool data of the liquidity module for a given pair ID and App ID.

        Args:
        pair_id (int): The unique identifier for the liquidity pair.
        app_id (int): The unique identifier for the app.

        Returns:
        Pair: An instance of the Pair class containing relevant liquidity pool data.
        """
        
        resp = await self.stub_liquidity.pair(QueryPairRequest(pair_id=pair_id,app_id=app_id))
        return resp




    async def get_pairs(self, denoms: List[str], app_id: int, pagination: PageRequest = None) -> QueryPairsResponse:

        """This function retrieves the pool data of the liquidity module for a given denom and App ID.

        Args:
        denom: The pair ID (denomination) for which to fetch pool data.
        app_id (int): The unique identifier of the application for which pool data is needed.

        Returns:
        Pairs: The pool data of the liquidity module corresponding to the given pair ID and App ID.
        """
        
        resp = await self.stub_liquidity.pairs(QueryPairsRequest(denoms=denoms, app_id=app_id, pagination=pagination))
        return resp




    async def get_deposit_request(self,  pool_id: int, id: int, app_id: int) -> DepositRequest:

        """Gets deposit request details for a specific pool ID, request ID, and App ID in the liquidity module.

        Args:
        pool_id (int): The unique identifier of the pool for which deposit request details are to be fetched.
        id (int): The unique identifier of the deposit request to be fetched.
        app_id (int): The unique identifier of the application associated with the deposit request.

        Returns:
        DepositRequest: An instance of the DepositRequest class containing the deposit request details.
        """
        
        resp = await self.stub_liquidity.deposit_request(QueryDepositRequestRequest(pool_id=pool_id, id=id, app_id=app_id))
        return resp




    async def get_deposit_requests(self, pool_id: int, app_id: int,pagination: PageRequest = None) -> QueryDepositRequestsResponse:

        """Gets deposit requests details for a specific pool ID and App ID in the liquidity module.

        Args:
        pool_id (int): The unique identifier for the liquidity pool.
        app_id (int): The unique identifier for the application using the liquidity module.

        Returns:
        Pair: A pair object containing the deposit request details for the specified pool and application.
        """
        
        resp = await self.stub_liquidity.deposit_requests(QueryDepositRequestsRequest(pool_id=pool_id, app_id=app_id, pagination=pagination))
        return resp




    async def get_withdraw_request(self, pool_id: int, id: int, app_id: int) -> WithdrawRequest:

        """Retrieves a withdraw request with the given pool ID, request ID, and App ID in the liquidity module.

        Args:
        pool_id (int): The unique identifier of the liquidity pool.
        id (int): The unique identifier of the withdraw request.
        app_id (int): The unique identifier of the application interacting with the liquidity module.

        Returns:
        WithdrawRequest: An instance of the WithdrawRequest class containing the details of the requested withdrawal.
        """
        
        resp = await self.stub_liquidity.withdraw_request(QueryWithdrawRequestRequest(pool_id=pool_id, id=id, app_id=app_id))
        return resp




    async def get_withdraw_requests(self, pool_id: int, app_id: int,pagination: PageRequest = None) -> QueryWithdrawRequestsResponse:

        """Retrieves a withdraw requests with the given pool ID and App ID in the liquidity module.

        Args:
        pool_id (int): The unique identifier for the liquidity pool.
        app_id (int): The unique identifier for the application.

        Returns:
        WithdrawRequests: A collection of withdraw requests related to the specified pool and app.
        """
        
        resp = await self.stub_liquidity.withdraw_requests(QueryWithdrawRequestsRequest(pool_id=pool_id, app_id=app_id,pagination=pagination))
        return resp




    async def get_order(self, pair_id: int, id: int, app_id: int) -> Order:

        """Retrieves the order details for a given pair ID, order ID, and app ID in the liquidity module.

        Args:
        pair_id (int): The unique identifier of the trading pair.
        id (int): The unique identifier of the order within the trading pair.
        app_id (int): The unique identifier of the application in the liquidity module.

        Returns:
        Order: An Order object containing the details of the specified order.
        """
        
        resp = await self.stub_liquidity.order(QueryOrderRequest(pair_id=pair_id, id=id, app_id=app_id))
        return resp
    


   
    async def get_orders(self, pair_id: int, app_id: int, pagination: PageRequest = None) -> QueryOrdersResponse:

        """Retrieves the order details for a specified trading pair and application ID in the liquidity module.

        Args:
        pair_id (int): The trading pair ID for which to fetch order details.
        app_id (int): The application ID associated with the liquidity module.

        Returns:
        Orders: A collection of orders related to the specified trading pair and application ID.
        """
        
        resp = await self.stub_liquidity.orders(QueryOrdersRequest(pair_id=pair_id, app_id=app_id,pagination=pagination))
        return resp
    


   
    async def get_orderbooks(self, app_id: int, pair_ids:List[int], price_unit_powers:List[int], num_ticks: int) -> QueryOrderBooksResponse:

        """Retrieves orderbook data for the given app ID, pair IDs, price unit powers, and number of ticks in the liquidity module.


        Args:
        app_id (int): The application ID to fetch orderbook data for.
        pair_ids (List[int]): A list of pair IDs to fetch orderbook data for.
        price_unit_powers (List[int]): A list of price unit powers for the orderbooks.
        num_ticks (int): The number of ticks (price levels) to retrieve for each orderbook.

        Returns:
        Orderbooks: A collection of orderbook data for the specified parameters.
        """
        
        resp = await self.stub_liquidity.order_books(QueryOrderBooksRequest(app_id=app_id, pair_ids=pair_ids, price_unit_powers=price_unit_powers, num_ticks=num_ticks))
        return resp
    


    
    async def get_farmer(self, app_id: int, pool_id: int,farmer: str) -> QueryFarmerResponse:

        """Retrieves the details for a given app ID, pool ID, and farmer in the liquidity module.

        Args:
              app_id (int): Application ID
              pool_id (int): Pool ID
              farmer (str): Farmer identifier

        Returns:  OrderbookDetails: The orderbook details containing active_pool_coin and queued_pool_coin.
    
        """
        
        resp = await self.stub_liquidity.farmer(QueryFarmerRequest(app_id=app_id, pool_id=pool_id, farmer=farmer))
        return resp



    
    async def get_deserialize_pool_coin(self, pool_id: int,pool_coin_amount: int ,app_id: int) -> QueryDeserializePoolCoinResponse:

        """Retrieves the orders details for a given pair ID and app ID in the liquidity module.

        Args:
             pool_id (int): The pool ID.
             pool_coin_amount (int): The pool coin amount.
             app_id (int): The app ID.

        Returns:
              DeserializePoolCoin: The deserialized pool coin object for the specified query.
        """
        
        resp = await self.stub_liquidity.deserialize_pool_coin(QueryDeserializePoolCoinRequest(pool_id=pool_id,pool_coin_amount=pool_coin_amount ,app_id=app_id))
        return resp




    async def get_pool_incentives(self, app_id: int) -> PoolIncentive:

        """Retrieves the pool incentives for a given app ID in the liquidity module.

        Args:
        app_id (int): The ID of the app for which to retrieve pool incentives.

        Returns:
        PoolIncentive: An object containing information about the pool incentives for the specified app ID.
        """
        
        resp = await self.stub_liquidity.pool_incentives(QueryPoolsIncentivesRequest(app_id=app_id))
        return resp
    



    async def get_farmed_pool_coin(self, pool_id: int, app_id: int) -> QueryFarmedPoolCoinResponse:

        """Retrieves the details of a specific farmed pool coin associated with a given pool ID and app ID from the liquidity module.

        Args:
        pool_id (int): The unique identifier of the pool.
        app_id (int): The unique identifier of the application.

        Returns:
        FarmedPoolCoin: An instance of the FarmedPoolCoin class containing the details of the farmed pool coin.
        """
        
        resp = await self.stub_liquidity.farmed_pool_coin(QueryFarmedPoolCoinRequest(pool_id=pool_id, app_id=app_id))
        return resp
    



    async def get_total_active_queued_pool_coin(self, app_id: int) -> TotalActiveAndQueuedPoolCoins:

        """This asynchronous function retrieves the total active and queued pool coins associated with a specific app ID in the liquidity module.

        Args:
        app_id (int): The unique identifier for the application in the liquidity module.

        Returns:
        TotalActiveAndQueuedPoolCoins: An object containing the total active and queued pool coins related to the given app ID.
        """
        resp = await self.stub_liquidity.total_active_and_queued_pool_coin(QueryAllFarmedPoolCoinsRequest(app_id=app_id))
        return resp
    



    async def get_orders_by_orderer(self,orderer:str ,pair_id: int, app_id: int) -> QueryOrdersResponse:
    
        """
        Asynchronously retrieves the order details associated with a specific orderer, pair ID, and app ID
        in the liquidity module.

        Args:
        orderer (str): The orderer's identifier, typically an account address.
        pair_id (int): The unique identifier of the trading pair.
        app_id (int): The application ID associated with the liquidity module.

        Returns:
        OrdersByOrderer: An object containing the order details for the given inputs.
        """
        resp = await self.stub_liquidity.orders_by_orderer(QueryOrdersByOrdererRequest(orderer=orderer, pair_id=pair_id, app_id=app_id))
        return resp 
    




    