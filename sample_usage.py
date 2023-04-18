import asyncio
from comdexpy.client import Client
from comdexpy.wallet import Wallet
from comdexpy.queries.comdex.liquidity import Query as LiquidityQueries
from comdexpy.queries.cosmos.bank import Query as BankQueries

from comdexpy.messages.cosmos.bank import MsgSend
from comdexpy.proto.cosmos.base.v1beta1 import Coin

from comdexpy.send_tx import SignAndBroadcastMessage

async def get_connection():
    grpc_url = "comdex-grpc.lavenderfive.com"
    return Client.from_endpoint(grpc_url, 443)

async def sample_query(channel):
    liquidity = LiquidityQueries(channel)
    params = await liquidity.get_generic_params(1)
    print(params.to_dict())
    
    pools = await liquidity.get_pools(1,"",1)
    print(pools.to_dict())
    
    pool = await liquidity.get_pool(1,1)
    print(pool.to_dict())

    pair = await liquidity.get_pool(1,1)
    print(pair.to_dict())

    pairs = await liquidity.get_pools([],1)
    print(pairs.to_dict())

    deposit_request = await liquidity.get_deposit_request(1,1,1)
    print(deposit_request.to_dict())

    deposit_requests = await liquidity.get_deposit_requests(1,1)
    print(deposit_requests.to_dict())
    
    withdraw_request = await liquidity.get_withdraw_request(1,1,1)
    print(withdraw_request.to_dict())

    withdraw_requests = await liquidity.get_withdraw_requests(1,1)
    print(withdraw_requests.to_dict())
   
    order = await liquidity.get_order(1,1,1)
    print(order.to_dict())

    orders = await liquidity.get_orders(1,1)
    print(orders.to_dict())

    orderbooks = await liquidity.get_orderbooks(1,[],[],1)
    print(orderbooks.to_dict())

    farmer = await liquidity.get_farmer(1,1,"")
    print(farmer.to_dict())

    deserialize_pool_coin = await liquidity.get_deserialize_pool_coin(1,1,1)
    print(deserialize_pool_coin.to_dict())

    pool_incentive = await liquidity.get_pool_incentives(1)
    print(pool_incentive.to_dict())    

    farmed_pool_coin = await liquidity.get_farmed_pool_coin(1,1)
    print(farmed_pool_coin.to_dict())  

    total_active_queued_pool_coin = await liquidity.get_total_active_queued_pool_coin(1)
    print(total_active_queued_pool_coin.to_dict()) 

    orders_by_orderer = await liquidity.get_orders_by_orderer("",1,1)
    print(orders_by_orderer.to_dict())

    

  #  bank = BankQueries(channel)
   # params = await bank.get_params()
   # print(params.to_dict())

async def sample_tx(connection):
    wallet = Wallet.from_mnemonic("home plate head toast deputy silent piece skate truth hold certain own")
    sender = wallet.get_address().to_acc_bech32()
    msg_send = MsgSend(
        from_address=sender,
        to_address="comdex",
        amount=[Coin(amount="1000000", denom="ucmdx")],
    )
    response = await SignAndBroadcastMessage.send_tx(connection, wallet, msg_send)
    print(response)


async def main():
    connection = await get_connection()
    await sample_query(connection.channel())
    # await sample_tx(connection)
    connection.close()


if __name__ == "__main__":
    asyncio.run(main())