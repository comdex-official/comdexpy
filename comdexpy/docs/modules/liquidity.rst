==============
LIQUIDITY
==============


Query
-----------

1.get_params
*************

        "Gets params of liquidity module."

        Args: 
             None

        Returns: 
             Liquidity Module's global Parameters
        

---------


2.get_generic_params
*********************

        "Gets generic params of liquidity module for specific App ID."

        Args:
             app_id (int): The unique identifier of the App for which the liquidity module parameters are to be fetched.

        Returns:
             GenericParams: An object containing the generic parameters of the liquidity module for the specified App ID.
        

--------


3.get_pools
*************

        "This function retrieves the pools data of the liquidity module for a given pair ID and App ID."

        Args:
             pair_id (int): The unique identifier for the trading pair.
             
             disabled (bool): A flag to filter pools based on whether they are disabled or not.
             
             app_id (int): The unique identifier for the application requesting the data.

        
        Returns:
             pools: A collection of pools data from the liquidity module that match the given parameters.
        
        
-------



4.get_pool
***********

        "This function retrieves the pool data of the liquidity module for a given pair ID and App ID."

        Args:
             pair_id (int): The unique identifier of the trading pair.
             
             app_id (int): The unique identifier of the application using the liquidity module.

        
        Returns:
             Pool: An instance of the Pool class containing the relevant liquidity pool data.
        
--------        


5.get_pair
***********

        "This function retrieves the pool data of the liquidity module for a given pair ID and App ID."

        Args:
             pair_id (int): The unique identifier for the liquidity pair.
             
             app_id (int): The unique identifier for the app.

        
        Returns:
             Pair: An instance of the Pair class containing relevant liquidity pool data.
        
        
--------


6.get_pairs
*************

        "This function retrieves the pool data of the liquidity module for a given denom and App ID."

        Args:
             denom: The pair ID (denomination) for which to fetch pool data.
             
             app_id (int): The unique identifier of the application for which pool data is needed.

        
        Returns:
             Pairs: The pool data of the liquidity module corresponding to the given pair ID and App ID.
        
        
-------


7.get_deposit_request
**********************

        "Gets deposit request details for a specific pool ID, request ID, and App ID in the liquidity module."

        Args:
              pool_id (int): The unique identifier of the pool for which deposit request details are to be fetched.
              
              id (int): The unique identifier of the deposit request to be fetched.
              
              app_id (int): The unique identifier of the application associated with the deposit request.

        
        Returns:
              DepositRequest: An instance of the DepositRequest class containing the deposit request details.
        
        
--------


8.get_deposit_requests
***********************

        "Gets deposit requests details for a specific pool ID and App ID in the liquidity module."

        Args:
              pool_id (int): The unique identifier for the liquidity pool.
              
              app_id (int): The unique identifier for the application using the liquidity module.

        
        Returns:
        
              Pair: A pair object containing the deposit request details for the specified pool and application.
        
        
-------


9.get_withdraw_request
***********************

        "Retrieves a withdraw request with the given pool ID, request ID, and App ID in the liquidity module."

        Args:
              pool_id (int): The unique identifier of the liquidity pool.
              
              id (int): The unique identifier of the withdraw request.
              
              app_id (int): The unique identifier of the application interacting with the liquidity module.

        
        Returns:
              WithdrawRequest: An instance of the WithdrawRequest class containing the details of the requested withdrawal.
        
        
--------



10.get_withdraw_requests
*************************

        "Retrieves a withdraw requests with the given pool ID and App ID in the liquidity module."

        Args:
              pool_id (int): The unique identifier for the liquidity pool.
              
              app_id (int): The unique identifier for the application.

        
        Returns:
              WithdrawRequests: A collection of withdraw requests related to the specified pool and app.
        
        
--------


11.get_order
*************

        "Retrieves the order details for a given pair ID, order ID, and app ID in the liquidity module."

        Args:
             pair_id (int): The unique identifier of the trading pair.
             
             id (int): The unique identifier of the order within the trading pair.
             
             app_id (int): The unique identifier of the application in the liquidity module.

        
        Returns:
        
             Order: An Order object containing the details of the specified order.
        
-------        
    

   
12.get_orders
**************

        "Retrieves the order details for a specified trading pair and application ID in the liquidity module."

        Args:
              pair_id (int): The trading pair ID for which to fetch order details.
              
              app_id (int): The application ID associated with the liquidity module.

        
        Returns:
             Orders: A collection of orders related to the specified trading pair and application ID.
        
            
--------

   
13.get_orderbooks
******************

        "Retrieves orderbook data for the given app ID, pair IDs, price unit powers, and number of ticks in the liquidity module."


        Args:
             app_id (int): The application ID to fetch orderbook data for.
             
             pair_ids (List[int]): A list of pair IDs to fetch orderbook data for.
             
             price_unit_powers (List[int]): A list of price unit powers for the orderbooks.
             
             num_ticks (int): The number of ticks (price levels) to retrieve for each orderbook.

        
        Returns:
             Orderbooks: A collection of orderbook data for the specified parameters.
        
-------        


    
14.get_farmer
**************

        "Retrieves the details for a given app ID, pool ID, and farmer in the liquidity module."

        Args:
              app_id (int): Application ID
              
              pool_id (int): Pool ID
              
              farmer (str): Farmer identifier

        
        Returns:  
              OrderbookDetails: The orderbook details containing active_pool_coin and queued_pool_coin.
    
        
-------


    
15.get_deserialize_pool_coin
*****************************

        "Retrieves the orders details for a given pair ID and app ID in the liquidity module."

        Args:
             pool_id (int): The pool ID.
             
             pool_coin_amount (int): The pool coin amount.
             
             app_id (int): The app ID.


        Returns:
              DeserializePoolCoin: The deserialized pool coin object for the specified query.
        
----------        



16.get_pool_incentives
***********************

        "Retrieves the pool incentives for a given app ID in the liquidity module."

        Args:
             app_id (int): The ID of the app for which to retrieve pool incentives.

        Returns:
             PoolIncentive: An object containing information about the pool incentives for the specified app ID.
        

----------            


17.get_farmed_pool_coin
************************

        "Retrieves the details of a specific farmed pool coin associated with a given pool ID and app ID from the liquidity module."

        Args:
             pool_id (int): The unique identifier of the pool.
             
             app_id (int): The unique identifier of the application.

        
        Returns:
             FarmedPoolCoin: An instance of the FarmedPoolCoin class containing the details of the farmed pool coin.
        
        
-------



18.get_total_active_queued_pool_coin
*************************************

        "This asynchronous function retrieves the total active and queued pool coins associated with a specific app ID in the liquidity module."

        Args:
             app_id (int): The unique identifier for the application in the liquidity module.

        Returns:
             TotalActiveAndQueuedPoolCoins: An object containing the total active and queued pool coins related to the given app ID.
        

--------    



19.get_orders_by_orderer
*************************
    
        
        "Asynchronously retrieves the order details associated with a specific orderer, pair ID, and app ID
        in the liquidity module."

        Args:
             orderer (str): The orderer's identifier, typically an account address.
             
             pair_id (int): The unique identifier of the trading pair.
             
             app_id (int): The application ID associated with the liquidity module.

        
        Returns:
             OrdersByOrderer: An object containing the order details for the given inputs.
        
----------


Messages
-----------

1.MsgCreatePair
*****************
            Create a pair (market) for trading A Pair can be created in two ways,

-Permission Less:
                A certain amount of fees need to be paid for creating pair. The fee paid is non-refundable. A pair can be launched instantly with this method.

-Governance:
                A proposal needs to be raised for creating pair via the governance module.


            A pair consists of a base coin and a quote coin and you can think of a pair in an order book. An orderer can request a limit or market order once a pair is created
            For creating a new pair, demons mentioned in base_coin_denom and quote_coin_denom should be allowed by the asset module.
            Pair can be created only with the demons that exist/are whitelisted in the asset module.
                         
                         MsgCreatePair {
                             string creator
                 
                             string base_coin_denom
                 
                             string quote_coin_denom
                 
                             uint64 app_id
             
                         }
            
            Validation checks that are being done before running pair creation logic -
                    Check that app_id is valid and that an app with this ID exists in the asset module.
                    
                    Check that base_coin_denom is valid and exists in the asset module.
                    
                    Check that quote_coin_denom is valid and exists in the asset module.
                    
                    Check that pair isn't already existed with the given app_id, base_coin_denom, and quote_coin_denom
            Transfers the pair creation fee from the creator account to the fee collector address of the app.
            
            Create a new Pair with existing + 1.

---------

2.MsgCreatePool
*****************

             Create a liquidity pool in the existing pair.

             Pool(s) belong to a pair. Therefore, a pair must exist in order to create a pool
             For pool creation, a certain amount of fees needs to be paid (default 200 CMDX). Each pool is unique. 
             At the initial creation of the pool, a fixed amount of max(deposit_coins.Amount) pool tokens is minted and sent to the creator of the pool’s account. The pool coin denom is in the form of pool{app_id}-{pool_id}.


                         MsgCreatePool {
                             string creator
                             
                             uint64 pair_id
                             
                             cosmos.base.v1beta1.Coin deposit_coins
                             
                             uint64 app_id
                         
                         }
             Validation checks that are being done before running pool creation logic -
                     Check that app_id is valid and that the app with this ID exists in the asset module.
                     
                     Check that pair_id is valid and pair_id and there exists a pair for it.
                     
                     Check that param exists for the given app_id, if not then the error is returned.
                     
                     Check that denoms of the coins in deposit_coins match with the pair’s base_coin_denom and quote_coin_denom.
                     
                     Check that deposit coins are >= minimum initial deposit amount
                     
                     Check that the pool with the same pair_id doesn't already exist.
             
             Create and save the new pool with ID as existingPoolID + 1
             
             Transfer deposit coins from the creator’s account to the pool reserve address.
             
             Transfer pool creation fee from creator’s account to app’s fee collector address
             
             Mint new pool tokens and transfer them to the creator’s account.
             
             Create a new gauge in the rewards module for swap fee distribution.

--------

3.MsgDeposit
**************

             Deposit coins to a liquidity pool. Deposit uses a batch execution methodology.

             Deposit requests are accumulated in a batch for a predefined period (default is 1 block) and they are executed at the end of the batch. A minimum deposit amount is 1000000 for each denomination.
             Note that in an order book system, a pool is considered an order. Liquidity in the pool places orders conservatively. What that means is that it places buy orders lower than the pool price and places sell orders higher than the pool price.

                         MsgDeposit {
                             string depositor
                             
                             uint64 pool_id
                             
                             cosmos.base.v1beta1.Coin deposit_coins 
                             
                             uint64 app_id
                         
                         }

             Validation checks that are being done before running deposit logic -
                     
                     Check that app_id is valid and that the app with this ID exists in the asset module.
                     
                     Check that pool_id is valid and the pool exists with the given pool_id and is not disabled.
                     
                     Check that deposit coins are valid and their denom matches with the denoms of a pair in the pool.
             
             Transfer deposit coins from depositor account to module’s global escrow address.
             
             Create a new deposit request with ID as existingDepositRequest + 1.

--------

4.MsgWithdraw 
***************

             Withdraw coins from the liquidity pool.

             Withdraw uses a batch execution methodology. Withdraw requests are accumulated in a batch for a predefined period (default is 1 block) and they are executed at the end of the batch.

                     MsgWithdraw {
                         string withdrawer
                         
                         uint64 pool_id
                         
                         cosmos.base.v1beta1.Coin pool_coin
                         
                         uint64 app_id
                     
                     }

             Validation checks that are being done before running withdraw logic -
                     Check that app_id is valid and the app with this ID exists in the asset module.
                     
                     Check that pool_id is valid and the pool exists with the given pool_id and is not disabled.
                     
                     Check that pool_coins denom are equal to the pool denom.
             
             Transfer pool coins from withdrawal account to module’s global escrow address.
             
             Create a new withdraw request with ID as existingWithdrawRequest + 1.

--------

5.MsgLimitOrder
****************

             Make a limit order.

             The buy limit order will be matched at lower than or equal to the defined order price whereas the sell limit order will be matched at higher than or equal to the defined order price.
             The order uses a batch execution methodology. Order requests are accumulated in a batch for a predefined period (default is 1 block) and they are executed at the end of the batch.

                     MsgLimitOrder {
                         string orderer
                             
                         uint64 pair_id
                             
                         OrderDirection direction
                             
                         cosmos.base.v1beta1.Coin offer_coin
                             
                         string demand_coin_denom
                             
                         string price 
                             
                         string amount 
                             
                         timedelta order_lifespan
                             
                         uint64 app_id
                         
                     }

             Validation checks that are being done before running limit order logic -
                     Check that param exists for the given app_id, if not then the error is returned.
                     
                     Check that app_id is valid and that an app with this ID exists in the asset module.
                     
                     Check that order_lifespan isn’t greater than max order lifespan.
                     
                     Check that pair_id is valid and pair_id and there exists a pair for it.
                     
                     Check that offer_coin is sufficient for the demanding coin for the given price and amount including the calculated swap fee based on the direction of order (buy/sell).
                     
                     Check that order isn’t too small.
             
             Transfer calculated offer coin from the orderer's account to the pair's escrow address.
             
             Create new order with ID as existing orderID + 1.      

-------

6.MsgMarketOrder
*****************

             Make a market order.

             Unlike a limit order, there is no need to input the order price.
             
             Buy market order uses MaxPriceLimitRatio of the list price, which is LastPrice * (1+MaxPriceLimitRatio).
             
             Sell market order uses negative MaxPriceLimitRatio of the last price, which is LastPrice * (1-MaxPriceLimitRatio).
             
             The order uses a batch execution methodology. Order requests are accumulated in a batch for a predefined period (default is 1 block) and they are executed at the end of the batch.


                     MsgMarketOrder {
                         string orderer
                         
                         uint64 pair_id
                         
                         OrderDirection direction
                         
                         cosmos.base.v1beta1.Coin offer_coin
                         
                         string demand_coin_denom
                         
                         string amount
                         
                         timedelta order_lifespan
   
                         uint64 app_id
                     }
             Validation checks that are being done before running market order logic -
                     Check that param exists for the given app_id, if not then the error is returned.
                     
                     Check that app_id is valid and an app with this ID exists in the asset module.
                     
                     Check that order_lifespan isn’t greater than max order lifespan.
                     
                     Check that pair_id is valid and pair_id and there exists a pair for it.
                     
                     Check that offer_coin is sufficient for the demanding coin for the given amount including the calculated swap fee based on the direction of order (buy/sell).
                     
                     Check that order isn’t too small.
             
             Transfer calculated offer coin from the orderer's account to the pair's escrow address.
             
             Create new order with ID as existing orderID + 1.


-------

7.MsgCancelOrder 
******************
             Cancel an order.

                     MsgCancelOrder {
                         string orderer
                         
                         uint64 pair_id
                         
                         uint64 order_id
                         
                         uint64 app_id
                     
                     }
             Validation checks that are being done before running cancel order logic -
                     Check that app_id is valid and that an app with this ID exists in the asset module.
                     
                     Check that order_id is valid and that order exists with the given order_id.
                     
                     Check that the orderer is the same as the order request creator.
                     
                     Check that the order with the given ID is not already canceled.
                     
                     Check that the order batch ID and pair’s current batch ID are not the same.
                     
                     Check if the order is not already completed.
             
             If the remaining offer coin is positive, the following conditions are checked actions are performed accordingly-
                     
                     If the remaining offer coin is the same as offered coin -
                     
                             Refund the full amount to the order including the swap fee collected amount.
                     
                     Recalculate the swap fee for swapped amount i.e (swapped amount = offer coin - remaining_offercoin)
                     
                     Refund the remaining amount + excess collected swap_fee back to the orderer
                     
                     Transfer accumulated swap fee amount from pair’s escrow address to pair’s swap fee collector address
             
             Set order status as canceled.


--------

8.MsgCancelAllOrders
*********************

             Cancel all orders.

                     MsgCancelAllOrders {
                         string orderer
                         
                         uint64 pair_id
                         
                         uint64 app_id
                     
                     }
             Validation checks that are being done before running cancel order logic -
                     
                     Check that app_id is valid and an app with this ID exists in the asset module.
             
             Get all the orders of the order from the given pair ID.
             
             Same actions are performed on each order as of cancel single order.

---------

9.MsgFarm
************
             Farm pool tokens to receive farming rewards.

                     MsgFarm {
                         uint64 app_id   
                         
                         uint64 pool_id
                         
                         string farmer
                         
                         cosmos.base.v1beta1.Coin farming_pool_coin
 
                     }

             Validation checks that are being done before running farm logic -
                     Check that the depositor address is a valid Bech32 address string.
                     
                     Check that app_id is valid and that an app with this ID exists in the asset module.
                     
                     Check that pool_id is valid and the pool exists with the given pool_id and is not disabled.
                     
                     Check that farming_pool_coin.denom is equal to the given pool_id’s pool denom.
             
             Transfer pool tokens from farmer’s account to liquidity modules’ account.
             
             Create a new queued farmer position with the current timestamp and store it.

-------

10.MsgUnfarm
**************
             Unfarm pool token from the network

                     MsgUnfarm {
                         uint64 app_id   
                         
                         uint64 pool_id
                         
                         string farmer
                         
                         cosmos.base.v1beta1.Coin unfarming_pool_coin
                     
                     }
             Validation checks that are being done before running unfarmlogic -
                     Check that the farmer's address is a valid Bech32 address string.
                     
                     Check that app_id is valid and that an app with this ID exists in the asset module.
                     
                     Check that pool_id is valid and the pool exists with the given pool_id and is not disabled.
                     
                     Check that unfarming_pool_coin.denom is equal to the given pool_id’s pool denom.
                     
                     Check that pool tokens are already farmed for the given farmer.
                     
                     Check that available farmed tokens (queued farm position + active farming position) >= unfarming_pool_coin
             
             Delete the queued farming position if queued coins are less than equal to unfarming_pool_coin, else update the queued farming position i.e (queued-coins = queued-coins - soft_unlock_coin).
             
             If queued coins are not sufficient enough for the unfarming_pool_coin coins then queued farming position is deleted after fulfilling a partial amount of unfarming_pool_coin and the remaining coins are being deducted from the active farming position of a farmer.


