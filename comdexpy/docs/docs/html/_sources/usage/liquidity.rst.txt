=============
Liquidity
=============

.. code:: python


 import asyncio
 from comdexpy.client import Client
 from comdexpy.wallet import Wallet
 from comdexpy.queries.comdex.liquidity import Query as LiquidityQueries


 from comdexpy.proto.cosmos.base.v1beta1 import Coin
 from comdexpy.proto.comdex.liquidity.v1beta1 import OrderDirection


 from comdexpy.messages.comdex.liquidity import (
    MsgDeposit
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


 async def main():
    connection = await get_connection()
    await sample_query(connection.channel())    #For Query     
    await sample_tx(connection)                 #For Transaction
    connection.close()


 if __name__ == "__main__":
    asyncio.run(main())  