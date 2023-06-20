===========
Auction
===========


.. code:: python

 import asyncio
 from comdexpy.client import Client
 from comdexpy.wallet import Wallet

 from comdexpy.queries.comdex.auction import Query as AuctionQueries

 from comdexpy.proto.cosmos.base.v1beta1 import Coin

 from comdexpy.messages.comdex.auction import (
    MsgPlaceSurplusBidRequest
   )

 from comdexpy.send_tx import SignAndBroadcastMessage

 async def get_connection():
    grpc_url = "comdex-grpc.lavenderfive.com"
    return Client.from_endpoint(grpc_url, 443)

 async def query(channel):
    auction = AuctionQueries(channel)

    #Query surplus auction
    surplus_auction = await auction.get_surplus_auction(3, 1, 1, True)
    print(surplus_auction.to_dict())



 async def sample_tx(connection):

    #----MsgPlaceSurplusBidRequest----

    wallet = Wallet.from_mnemonic("")
    sender = wallet.get_address().to_acc_bech32()
    msg_place_surplus_bid_request = MsgPlaceSurplusBidRequest(
        auction_id = 20,
        bidder = sender,
        amount = Coin(amount = "10000000", denom = "ucmdx"),
        app_id = 3,
        auction_mapping_id = 3
    )
    response = await SignAndBroadcastMessage.send_tx(connection, wallet, msg_place_surplus_bid_request)
    print(response)   


 async def main():
    connection = await get_connection()
    await query(connection.channel())       # For Query
    await sample_tx(connection)             # For Transaction
    connection.close()


 if __name__ == "__main__":
    asyncio.run(main()) 