import asyncio

from comdexpy.client import Client
from comdexpy.wallet import Wallet

from comdexpy.queries.comdex.lend import Query as LendQueries

from comdexpy.proto.cosmos.base.v1beta1 import Coin

from comdexpy.messages.comdex.lend import (
    MsgLend,
    MsgWithdraw,
    MsgDeposit,
    MsgCloseLend,
    MsgBorrow,
    MsgRepay,
    MsgDraw,
    MsgCloseBorrow,
    MsgBorrowAlternate,
    MsgFundModuleAccounts,
    MsgFundReserveAccounts,
    MsgCalculateInterestAndRewards
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
    
    #Query lend
    lend_asset = await lend.get_lend(1)
    print(lend_asset)
    
    #Query lends
    lends_asset = await lend.get_lends()
    print(lends_asset)

    #Query all lend by owner
    all_lend_by_owner = await lend.get_all_lend_by_owner("")
    print(all_lend_by_owner)

    #Query all lend by owner and pool
    all_lend_by_owner_and_pool = await lend.get_all_lend_by_owner_and_pool("", 1)
    print(all_lend_by_owner_and_pool.to_dict())

    #Query pairs
    pairs = await lend.get_pairs()
    print(pairs)

    #Query pair 
    pair = await lend.get_pair(1)
    print(pair)
    
    #Query asset rates params
    asset_rates_params = await lend.get_asset_rates_params()
    print(asset_rates_params)

    #Query asset rates param
    asset_rates_param = await lend.get_asset_rates_param(1)
    print(asset_rates_param)
   
    #Query pools
    pools = await lend.get_pools()
    print(pools)

    #Query pool
    pool = await lend.get_pool(1)
    print(pool)

    #Query asset to pair mappings
    asset_to_pair_mappings = await lend.get_asset_to_pair_mappings()
    print(asset_to_pair_mappings)

    #Query asset to pair mapping
    asset_to_pair_mapping = await lend.get_asset_to_pair_mapping(1, 1)
    print(asset_to_pair_mapping.to_dict())

    #Query borrows
    borrows = await lend.get_borrows()
    print(borrows)

    #Query borrow
    borrow = await lend.get_borrow(1)
    print(borrow)    

    #Query all borrow by owner
    all_borrow_by_owner = await lend.get_all_borrow_by_owner("")
    print(all_borrow_by_owner)  

    #Query all borrow by owner and pool
    all_borrow_by_owner_and_pool = await lend.get_all_borrow_by_owner_and_pool("",1)
    print(all_borrow_by_owner_and_pool.to_dict()) 

    #Query pool asset lb mapping
    pool_asset_lb_mapping = await lend.get_pool_asset_lb_mapping(1, 1)
    print(pool_asset_lb_mapping.to_dict())

    #Query reserve buyback asset data
    reserve_buyback_asset_data = await lend.get_reserve_buyback_asset_data(1)
    print(reserve_buyback_asset_data)

    #Query auction param
    auction_param = await lend.get_auction_param(3)
    print(auction_param)

    #Query module balance
    module_balance = await lend.get_module_balance(1)
    print(module_balance)

    #Query fund module balance
    fund_mod_bal = await lend.get_fund_mod_bal()
    print(fund_mod_bal)

    #Query fund reserve balance
    fund_reserve_bal = await lend.get_fund_reserve_bal()
    print(fund_reserve_bal)

    #Query all reserve stats
    all_reserve_stats = await lend.get_all_reserve_stats(1)
    print(all_reserve_stats)

    #Query fund module balance by asset pool
    fund_mod_bal_by_asset_pool = await lend.get_fund_mod_bal_by_asset_pool(1, 1)
    print(fund_mod_bal_by_asset_pool.to_dict())

    #Query lend interest
    lend_interest = await lend.get_lend_interest()
    print(lend_interest)

    #Query borrow interest
    borrow_interest = await lend.get_borrow_interest()
    print(borrow_interest)




"""
    TRANSACTION
"""


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


#----MsgWithdraw----

    wallet = Wallet.from_mnemonic("")
    msg_withdraw = MsgWithdraw(
        lender = "",
        lend_id = 24,
        amount = Coin(amount="100000000", denom="ucmdx")
    )
    response = await SignAndBroadcastMessage.send_tx(connection, wallet, msg_withdraw)
    print(response)


#----MsgDeposit----

    wallet = Wallet.from_mnemonic("")
    msg_deposit = MsgDeposit(
        lender = "",
        lend_id = 24,
        amount = Coin(amount="10000000", denom="ucmdx")
    )
    response = await SignAndBroadcastMessage.send_tx(connection, wallet, msg_deposit)
    print(response)   


#----MsgCloseLend----

    wallet = Wallet.from_mnemonic("")
    msg_close_lend = MsgCloseLend(
        lender = "",
        lend_id = 24
    )
    response = await SignAndBroadcastMessage.send_tx(connection, wallet, msg_close_lend)
    print(response)


#----MsgBorrow----

    wallet = Wallet.from_mnemonic("")
    msg_borrow = MsgBorrow(
        borrower = "",
        lend_id = 24,
        pair_id = 1,
        is_stable_borrow = False,
        amount_in = Coin(amount="100000000", denom="ucmdx"),
        amount_out = Coin(amount="3000000", denom="ucmst")
    )
    response = await SignAndBroadcastMessage.send_tx(connection, wallet, msg_borrow)
    print(response)


#----MsgRepay----

    wallet = Wallet.from_mnemonic("")
    msg_repay = MsgRepay(
        borrower = "",
        borrow_id = 24,
        amount = Coin(amount="2000000", denom="ucmst")
    )
    response = await SignAndBroadcastMessage.send_tx(connection, wallet, msg_repay)
    print(response)


#----MsgDraw----

    wallet = Wallet.from_mnemonic("")
    msg_draw = MsgDraw(
        borrower = "",
        borrow_id = 24,
        amount = Coin(amount="1000000", denom="ucmdx")
    )
    response = await SignAndBroadcastMessage.send_tx(connection, wallet, msg_draw)
    print(response)


#----MsgCloseBorrow----

    wallet = Wallet.from_mnemonic("")
    sender = wallet.get_address().to_acc_bech32()
    msg_close_borrow = MsgCloseBorrow(
        borrower = sender,
        borrow_id = 24
    )
    response = await SignAndBroadcastMessage.send_tx(connection, wallet, msg_close_borrow)
    print(response)


#----MsgBorrowAlternate----

    wallet = Wallet.from_mnemonic("")
    msg_borrow_alternate = MsgBorrowAlternate(
        lender = "",
        asset_id = 2,
        pool_id=1,
        amount_in = Coin(amount="100000000", denom="ucmdx"),
        pair_id=1,
        is_stable_borrow=False,
        amount_out=Coin(amount="3000000", denom="ucmst"),
        app_id=3
    )
    response = await SignAndBroadcastMessage.send_tx(connection, wallet, msg_borrow_alternate)
    print(response)


#----MsgFundModuleAccounts----
#  
    wallet = Wallet.from_mnemonic("")
    sender = wallet.get_address().to_acc_bech32()
    msg_fund_module_accounts = MsgFundModuleAccounts(
        lender = sender,
        amount = Coin(amount="1000000", denom="ucmdx"),
        pool_id = 2,
        asset_id = 2  
    )
    response = await SignAndBroadcastMessage.send_tx(connection, wallet, msg_fund_module_accounts)
    print(response)


#----MsgFundReserveAccounts----

    wallet = Wallet.from_mnemonic("")
    sender = wallet.get_address().to_acc_bech32()
    msg_fund_reserve_accounts = MsgFundReserveAccounts(
        lender = sender,
        amount = Coin(amount="1000000", denom="ucmdx"),
        asset_id = 2
    )
    response = await SignAndBroadcastMessage.send_tx(connection, wallet, msg_fund_reserve_accounts)
    print(response)


#----MsgCalculateInterestAndRewards----

    wallet = Wallet.from_mnemonic("")
    msg_calculate_interest_and_rewards = MsgCalculateInterestAndRewards(
        borrower = ""
    )
    response = await SignAndBroadcastMessage.send_tx(connection, wallet, msg_calculate_interest_and_rewards)
    print(response)




async def main():
    connection = await get_connection()
    await sample_query(connection.channel())    # For Query
    await sample_tx(connection)                 # For Transaction
    connection.close()


if __name__ == "__main__":
    asyncio.run(main())