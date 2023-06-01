import asyncio
from comdexpy.client import Client
from comdexpy.wallet import Wallet

from comdexpy.queries.comdex.auction import Query as AuctionQueries

from comdexpy.proto.cosmos.base.v1beta1 import Coin

from comdexpy.messages.comdex.auction import (
    MsgPlaceSurplusBidRequest,
    MsgPlaceDebtBidRequest,
    MsgPlaceDutchBidRequest,
    MsgPlaceDutchLendBidRequest
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
    
    #Query surplus auctions
    surplus_auctions = await auction.get_surplus_auctions(1, True)
    print(surplus_auctions.to_dict())
    
    #Query surplus biddings
    surplus_biddings = await auction.get_surplus_biddings("", 1, True)
    print(surplus_biddings.to_dict())

    #Query debt auction
    debt_auction = await auction.get_debt_auction(2, 1, 1, True)
    print(debt_auction.to_dict())

    #Query debt auctions
    debt_auctions = await auction.get_debt_auctions(1, True)
    print(debt_auctions.to_dict())

    #Query debt biddings
    debt_biddings = await auction.get_debt_biddings("", 1, True)
    print(debt_biddings.to_dict())

    #Query dutch auction
    dutch_auction = await auction.get_dutch_auction(1, 1, 1, True)
    print(dutch_auction.to_dict())
    
    #Query dutch auctions
    dutch_auctions = await auction.get_dutch_auctions(1, True)
    print(dutch_auctions.to_dict())

    #Query dutch biddings
    dutch_biddings = await auction.get_dutch_biddings("", 1, True)
    print(dutch_biddings.to_dict())
   
    #Query protocol statistics
    protocol_statistics = await auction.get_protocol_statistics(1)
    print(protocol_statistics)

    #Query biddings for surplus auction
    biddings_for_surplus_auction = await auction.get_biddings_for_surplus_auction(1, 1, 1, True)
    print(biddings_for_surplus_auction.to_dict())

    #Query generic auction param
    generic_auction_param = await auction.get_generic_auction_param(1)
    print(generic_auction_param)

    #Query dutch lend auction
    dutch_lend_auction = await auction.get_dutch_lend_auction(1, 1, 1, True)
    print(dutch_lend_auction.to_dict())

    #Query dutch lend auctions
    dutch_lend_auctions = await auction.get_dutch_lend_auctions(1, True)
    print(dutch_lend_auctions.to_dict())
 
    #Query dutch lend biddings
    dutch_lend_biddings = await auction.get_dutch_lend_biddings("", 1, True)
    print(dutch_lend_biddings.to_dict())

    #Query filter dutch auctions
    filter_dutch_auctions = await auction.get_filter_dutch_auctions(1, [""], True)
    print(filter_dutch_auctions.to_dict())

    

"""
    TRANSACTION
"""

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


#----MsgPlaceDebtBidRequest----

    wallet = Wallet.from_mnemonic("")
    sender = wallet.get_address().to_acc_bech32()
    msg_place_debt_bid_request = MsgPlaceDebtBidRequest(
        auction_id = 20,
        bidder = sender,
        bid = ,
        expected_user_token = ,
        app_id = 3,
        auction_mapping_id = 3
    )
    response = await SignAndBroadcastMessage.send_tx(connection, wallet, msg_place_debt_bid_request)
    print(response)   


#----MsgPlaceDutchBidRequest----

    wallet = Wallet.from_mnemonic("")
    msg_place_dutch_bid_request = MsgPlaceDutchBidRequest(
        auction_id = 5,
        bidder = "",
        amount = Coin(amount="", denom=""),
        app_id = 2,
        auction_mapping_id = 3
    )
    response = await SignAndBroadcastMessage.send_tx(connection, wallet, msg_place_dutch_bid_request)
    print(response)


#----MsgPlaceDutchLendBidRequest----

    wallet = Wallet.from_mnemonic("")
    msg_place_dutch_lend_bid_request = MsgPlaceDutchLendBidRequest(
        auction_id = 20,
        bidder = "",
        amount = Coin(amount = "10000000", denom = "ucmdx"),
        app_id = 3,
        auction_mapping_id = 3
    )
    response = await SignAndBroadcastMessage.send_tx(connection, wallet, msg_place_dutch_lend_bid_request)
    print(response)    



async def main():
    connection = await get_connection()
    await query(connection.channel())       # For Query
    await sample_tx(connection)             # For Transaction
    connection.close()


if __name__ == "__main__":
    asyncio.run(main())