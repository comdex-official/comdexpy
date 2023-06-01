import asyncio
from comdexpy.client import Client
from comdexpy.wallet import Wallet
from comdexpy.queries.comdex.liquidity import Query as LiquidityQueries


from comdexpy.proto.cosmos.base.v1beta1 import Coin
from comdexpy.proto.comdex.liquidity.v1beta1 import OrderDirection


from comdexpy.messages.comdex.liquidity import (
    MsgDeposit,
    MsgCreatePair,
    MsgCreatePool,
    MsgCreateRangedPool,
    MsgWithdraw,
    MsgLimitOrder,
    MsgMarketOrder,
    MsgMmOrder,
    MsgCancelOrder,
    MsgCancelAllOrders,
    MsgCancelMmOrder,
    MsgFarm,
    MsgUnfarm
)


from comdexpy.send_tx import SignAndBroadcastMessage

async def get_connection():
    grpc_url = "comdex-grpc.lavenderfive.com"
    return Client.from_endpoint(grpc_url, 443)

async def sample_query(channel):

    liquidity = LiquidityQueries(channel)
    
    #Query generic params
    params = await liquidity.get_generic_params(1)
    print(params.to_dict())
    
    #Query pools
    pools = await liquidity.get_pools(1, "", 1)
    print(pools.to_dict())
    
    #Query pool
    pool = await liquidity.get_pool(1, 1)
    print(pool.to_dict())

    #Query pair
    pair = await liquidity.get_pair(1, 1)
    print(pair.to_dict())

    #Query pairs
    pairs = await liquidity.get_pairs(["ucmdx"], 1)
    print(pairs.to_dict())

    #Query deposit request
    deposit_request = await liquidity.get_deposit_request(1, 3, 2)
    print(deposit_request.to_dict())

    #Query deposit requests
    deposit_requests = await liquidity.get_deposit_requests(1, 1)
    print(deposit_requests.to_dict())
    
    #Query withdraw request
    withdraw_request = await liquidity.get_withdraw_request(1, 1, 1)
    print(withdraw_request.to_dict())

    #Query withdraw requests
    withdraw_requests = await liquidity.get_withdraw_requests(1, 1)
    print(withdraw_requests.to_dict())
   
    #Query order
    order = await liquidity.get_order(1, 2, 1)
    print(order.to_dict())

    #Query orders
    orders = await liquidity.get_orders(1, 1)
    print(orders.to_dict())

    #Query orderbooks
    orderbooks = await liquidity.get_orderbooks(1, [3], [], 1)
    print(orderbooks.to_dict())

    #Query farmer
    farmer = await liquidity.get_farmer(1, 1, "")
    print(farmer.to_dict())

    #Query deserialize pool coin
    deserialize_pool_coin = await liquidity.get_deserialize_pool_coin(1, 1, 1)
    print(deserialize_pool_coin.to_dict())

    #Query pool incentives 
    pool_incentive = await liquidity.get_pool_incentives(1)
    print(pool_incentive)    

    #Query farmed pool coin 
    farmed_pool_coin = await liquidity.get_farmed_pool_coin(1, 1)
    print(farmed_pool_coin.to_dict())  

    #Query total active queued pool coin
    total_active_queued_pool_coin = await liquidity.get_total_active_queued_pool_coin(1)
    print(total_active_queued_pool_coin) 

    #Query orders by orderer
    orders_by_orderer = await liquidity.get_orders_by_orderer("", 1, 1)
    print(orders_by_orderer.to_dict())



    """
    Transactions
    """

async def sample_tx(connection):

#----MsgCreatePair----

    wallet = Wallet.from_mnemonic("")
    sender = wallet.get_address().to_acc_bech32()
    msg_create_pair = MsgCreatePair(
        creator = sender,
        base_coin_denom = "ucmdx",
        quote_coin_denom = "ucmst",
        app_id = 1
    )
    response = await SignAndBroadcastMessage.send_tx(connection, wallet, msg_create_pair)
    print(response)



#----MsgDeposit----

    wallet = Wallet.from_mnemonic("")
    sender = wallet.get_address().to_acc_bech32()
    msg_deposit = MsgDeposit(
        depositor = sender,
        pool_id = 1,
        deposit_coins = [Coin(amount = "1000000", denom = "ucmdx"),Coin(amount = "51360",denom = "ucmst")],
        app_id = 1
    )
    response = await SignAndBroadcastMessage.send_tx(connection, wallet, msg_deposit)
    print(response)



#----MsgCreatePool----

    wallet = Wallet.from_mnemonic("")
    msg_create_Pool = MsgCreatePool(
        creator = "",
        pair_id = 1,
        deposit_coins = [Coin(amount = "1000000", denom = "ucmdx"),Coin(amount = "51360",denom = "ucmst")],
        app_id = 2
    )
    response = await SignAndBroadcastMessage.send_tx(connection, wallet, msg_create_Pool)
    print(response)    


#----MsgCreateRangedPool----

    wallet = Wallet.from_mnemonic("")
    sender = wallet.get_address().to_acc_bech32()
    msg_create_ranged_pool = MsgCreateRangedPool(
        creator = sender,
        app_id = 2,
        pair_id = 1,
        deposit_coins = [Coin(amount="1000000", denom="ucmdx"),Coin(amount= "51360",denom="ucmst")],
        min_price = "50000",
        max_price = "2000000",
        initial_price = "51360"
    )
    response = await SignAndBroadcastMessage.send_tx(connection, wallet, msg_create_ranged_pool)
    print(response)       


#----MsgWithdraw----

    wallet = Wallet.from_mnemonic("")
    msg_withdraw = MsgWithdraw(
        withdrawer = "",
        pool_id = 1,
        pool_coin = Coin(amount="1000000", denom="ucmdx"),
        app_id = 2
    )
    response = await SignAndBroadcastMessage.send_tx(connection, wallet, msg_withdraw)
    print(response)    



#----MsgLimitOrder----

    wallet = Wallet.from_mnemonic("")
    print(OrderDirection.ORDER_DIRECTION_SELL)
    msg_limit_order = MsgLimitOrder(
        orderer = "",
        pair_id = 1,
        direction = OrderDirection.ORDER_DIRECTION_SELL,
        offer_coin = "ucmdx",
        demand_coin_denom = "ucmst",
        price = 1000000,
        amount = 500000,
        order_lifespan = 1,
        app_id = 2
    )
    response = await SignAndBroadcastMessage.send_tx(connection, wallet, msg_limit_order)
    print(response)


#----MsgMarketOrder----

    wallet = Wallet.from_mnemonic("")
    msg_market_order = MsgMarketOrder(
        orderer = "",
        pair_id = 1,
        direction = OrderDirection.ORDER_DIRECTION_SELL,
        offer_coin = "ucmdx",
        demand_coin_denom = "ucmst",
        amount = 500000,
        order_lifespan = 1,
        app_id = 2
    )
    response = await SignAndBroadcastMessage.send_tx(connection, wallet, msg_market_order)
    print(response)


#----MsgMmOrder----

    wallet = Wallet.from_mnemonic("")
    msg_Mm_order = MsgMmOrder(
        orderer = "",
        app_id = 2,
        pair_id = 1,
        max_sell_price = ,
        min_sell_price = ,
        sell_amount = ,
        max_buy_price = ,
        min_buy_price = ,
        buy_amount = ,
        order_lifespan = 1
    )
    response = await SignAndBroadcastMessage.send_tx(connection, wallet, msg_Mm_order)
    print(response)



#----MsgCancelOrder----

    wallet = Wallet.from_mnemonic("")
    msg_cancel_order = MsgCancelOrder(
        orderer = "",
        pair_id = 1,
        order_id = 3,
        app_id = 1
    )
    response = await SignAndBroadcastMessage.send_tx(connection, wallet, msg_cancel_order)
    print(response)


#----MsgCancelAllOrders----

    wallet = Wallet.from_mnemonic("")
    msg_cancel_all_orders = MsgCancelAllOrders(
        orderer = "",
        pair_ids = [1, 2],
        app_id = 2
    )
    response = await SignAndBroadcastMessage.send_tx(connection, wallet, msg_cancel_all_orders)
    print(response)    


#----MsgCancelMmOrder----

    wallet = Wallet.from_mnemonic("")
    msg_cancel_Mm_order = MsgCancelMmOrder(
        orderer = "",
        app_id = 2,
        pair_id = 1
    )
    response = await SignAndBroadcastMessage.send_tx(connection, wallet, msg_cancel_Mm_order)
    print(response)    
     

#----MsgFarm----

    wallet = Wallet.from_mnemonic("")
    msg_farm = MsgFarm(
        app_id = 1,
        pool_id = 3,
        farmer = "",
        farming_pool_coin = Coin(amount="1000000", denom="ucmdx")
    )
    response = await SignAndBroadcastMessage.send_tx(connection, wallet, msg_farm)
    print(response)


#----MsgUnfarm----

    wallet = Wallet.from_mnemonic("")
    msg_unfarm = MsgUnfarm(
        app_id = 1,
        pool_id = 3,
        farmer = "",
        unfarming_pool_coin = Coin(amount="1000000", denom="ucmdx")
    )
    response = await SignAndBroadcastMessage.send_tx(connection, wallet, msg_unfarm)
    print(response)



async def main():
    connection = await get_connection()
    await sample_query(connection.channel())    #For Query     
    await sample_tx(connection)                 #For Transaction
    connection.close()


if __name__ == "__main__":
    asyncio.run(main())