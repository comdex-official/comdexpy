import asyncio
from comdexpy.client import Client
from comdexpy.wallet import Wallet

from comdexpy.queries.comdex.liquidation import Query as LiquidationQueries


from comdexpy.messages.comdex.liquidation import (
    MsgLiquidateVaultRequest,
    MsgLiquidateBorrowRequest
)
    
from comdexpy.send_tx import SignAndBroadcastMessage


async def get_connection():
    grpc_url = "comdex-grpc.lavenderfive.com"
    return Client.from_endpoint(grpc_url, 443)

async def query(channel):

    liquidation = LiquidationQueries(channel)

    #Query locked vault
    locked_vault = await liquidation.get_locked_vault(2 ,9)
    print(locked_vault.to_dict())
    
    #Query locked vaults
    locked_vaults = await liquidation.get_locked_vaults()
    print(locked_vaults)
    
    #Query liquidation params
    liquidation_params = await liquidation.get_liquidation_params()
    print(liquidation_params)
    
    #Query locked vaults history
    locked_vaults_history = await liquidation.get_locked_vaults_history()
    print(locked_vaults_history)

    #Query user locked vaults
    user_locked_vaults = await liquidation.get_user_locked_vaults("")
    print(user_locked_vaults)
 
    #Query user locked vaults history
    user_locked_vaults_history = await liquidation.get_user_locked_vaults_history("")
    print(user_locked_vaults_history)
 
    #Query locked vaults pair
    locked_vaults_pair = await liquidation.get_locked_vaults_pair(1)
    print(locked_vaults_pair)
 
    #Query app ids
    app_ids = await liquidation.get_app_ids()
    print(app_ids)

    


"""
    TRANSACTION
"""


async def sample_tx(connection):


#----MsgLiquidateVaultRequest----

    wallet = Wallet.from_mnemonic("")
    sender = wallet.get_address().to_acc_bech32()
    msg_liquidate_vault_request = MsgLiquidateVaultRequest(
        from_= sender,
        app_id = 2,
        vault_id = 20 
    )
    response = await SignAndBroadcastMessage.send_tx(connection, wallet, msg_liquidate_vault_request)
    print(response)


#----MsgLiquidateBorrowRequest----

    wallet = Wallet.from_mnemonic("")
    sender = wallet.get_address().to_acc_bech32()
    msg_liquidate_borrow_request = MsgLiquidateBorrowRequest(
        from_ = sender,
        borrow_id = 24
    )
    response = await SignAndBroadcastMessage.send_tx(connection, wallet, msg_liquidate_borrow_request)
    print(response)



async def main():
    connection = await get_connection()
    await query(connection.channel())      # For Query
    await sample_tx(connection)            # For Transaction
    connection.close()


if __name__ == "__main__":
    asyncio.run(main())