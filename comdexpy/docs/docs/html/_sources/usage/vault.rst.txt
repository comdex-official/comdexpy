==========
Vault
==========

.. code:: python


 import asyncio
 from comdexpy.client import Client
 from comdexpy.wallet import Wallet

 from comdexpy.queries.comdex.vault import Query as VaultQueries

 from comdexpy.send_tx import SignAndBroadcastMessage

 from comdexpy.messages.comdex.vault import (
    MsgCreateRequest
 )

 async def get_connection():
    grpc_url = "comdex-grpc.lavenderfive.com"
    return Client.from_endpoint(grpc_url, 443)

 async def query(channel):
    vault = VaultQueries(channel)

    #Query vault info by vault id
    vault_info_by_vault_id = await vault.get_vault_info_by_vault_id(2)
    print(vault_info_by_vault_id)


 async def sample_tx(connection):

 #----MsgCreateRequest----

    wallet = Wallet.from_mnemonic("")
    sender = wallet.get_address().to_acc_bech32()
    msg_create_request = MsgCreateRequest(
        from_ = sender,
        app_id = 2,
        extended_pair_vault_id = 2,
        amount_in = "10000000",
        amount_out = "50385567"
    )
    response = await SignAndBroadcastMessage.send_tx(connection, wallet, msg_create_request)
    print(response)


 async def main():
    connection = await get_connection()
    await query(connection.channel())       # For Query
    await sample_tx(connection)             # For Transaction
    connection.close()


 if __name__ == "__main__":
    asyncio.run(main())