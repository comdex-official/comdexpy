===========
Lend
===========

.. code:: python


 import asyncio

 from comdexpy.client import Client
 from comdexpy.wallet import Wallet

 from comdexpy.queries.comdex.lend import Query as LendQueries

 from comdexpy.proto.cosmos.base.v1beta1 import Coin

 from comdexpy.messages.comdex.lend import (
    MsgLend
   )

 from comdexpy.send_tx import SignAndBroadcastMessage

 async def get_connection():
    grpc_url = "comdex-grpc.lavenderfive.com"
    return Client.from_endpoint(grpc_url, 443)

 async def sample_query(channel):
    lend = LendQueries(channel)

    #Query params
    params = await lend.get_params()
    print(params)


 async def sample_tx(connection):

  #----MsgLend----

    wallet = Wallet.from_mnemonic("")
    msg_lend = MsgLend(
        lender = "",
        asset_id = 2,
        amount = [Coin(amount="100000000", denom="ucmdx")],
        pool_id = 1,
        app_id = 3
    )
    response = await SignAndBroadcastMessage.send_tx(connection, wallet, msg_lend)
    print(response)


 async def main():
    connection = await get_connection()
    await sample_query(connection.channel())    # For Query
    await sample_tx(connection)                 # For Transaction
    connection.close()


 if __name__ == "__main__":
    asyncio.run(main())