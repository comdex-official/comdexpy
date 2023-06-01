import asyncio
from comdexpy.client import Client
from comdexpy.wallet import Wallet

from comdexpy.queries.comdex.vault import Query as VaultQueries

from comdexpy.send_tx import SignAndBroadcastMessage

from comdexpy.messages.comdex.vault import (
    MsgCreateRequest,
    MsgDepositRequest,
    MsgWithdrawRequest,
    MsgDrawRequest,
    MsgRepayRequest,
    MsgCloseRequest,
    MsgDepositAndDrawRequest,
    MsgCreateStableMintRequest,
    MsgDepositStableMintRequest,
    MsgWithdrawStableMintRequest,
    MsgVaultInterestCalcRequest
)

async def get_connection():
    grpc_url = "comdex-grpc.lavenderfive.com"
    return Client.from_endpoint(grpc_url, 443)

async def query(channel):
    vault = VaultQueries(channel)

    #Query vault info by vault id
    vault_info_by_vault_id = await vault.get_vault_info_by_vault_id(2)
    print(vault_info_by_vault_id)

    #Query vault info
    vault_info = await vault.get_vault_info(2)
    print(vault_info)
    
    #Query vault info of owner by app id
    vault_info_of_owner_by_app_id = await vault.get_vault_info_of_owner_by_app_id(1, "")
    print(vault_info_of_owner_by_app_id.to_dict())

    #Query all vaults
    all_vaults = await vault.get_all_vaults()
    print(all_vaults)

    #Query all vaults by app
    all_vaults_by_app = await vault.get_all_vaults_by_app(2)
    print(all_vaults_by_app)

    #Query all vaults by app and extended pair
    all_vaults_by_app_and_extended_pair = await vault.get_all_vaults_by_app_and_extended_pair(2, 3)
    print(all_vaults_by_app_and_extended_pair.to_dict())

    #Query vault id of owner by extended pair and app
    vault_id_of_owner_by_extended_pair_and_app = await vault.get_vault_id_of_owner_by_extended_pair_and_app(2, "", 3)
    print(vault_id_of_owner_by_extended_pair_and_app.to_dict())
    
    #Query vault ids by app in all extended pairs
    vault_ids_by_app_in_all_extended_pairs = await vault.get_vault_ids_by_app_in_all_extended_pairs(2)
    print(vault_ids_by_app_in_all_extended_pairs)

    #Query all vault ids by an owner
    all_vault_ids_by_an_owner = await vault.get_all_vault_ids_by_an_owner("")
    print(all_vault_ids_by_an_owner)
   
    #Query token minted by app and extended pair
    token_minted_by_app_and_extended_pair = await vault.get_token_minted_by_app_and_extended_pair(2, 3)
    print(token_minted_by_app_and_extended_pair.to_dict())

    #Query token minted asset wise by app
    token_minted_asset_wise_by_app = await vault.get_token_minted_asset_wise_by_app(2)
    print(token_minted_asset_wise_by_app)

    #Query vault count by app
    vault_count_by_app = await vault.get_vault_count_by_app(2)
    print(vault_count_by_app)

    #Query vault count by app and extended pair
    vault_count_by_app_and_extended_pair = await vault.get_vault_count_by_app_and_extended_pair(2, 3)
    print(vault_count_by_app_and_extended_pair.to_dict())

    #Query total value locked by app and extended pair
    total_value_locked_by_app_and_extended_pair = await vault.get_total_value_locked_by_app_and_extended_pair(2, 3)
    print(total_value_locked_by_app_and_extended_pair.to_dict())

    #Query extended pair ids by app
    extended_pair_ids_by_app = await vault.get_extended_pair_ids_by_app(2)
    print(extended_pair_ids_by_app)    

    #Query stable vault by vault id
    stable_vault_by_vault_id = await vault.get_stable_vault_by_vault_id(1)
    print(stable_vault_by_vault_id)  

    #Query stable vault by app
    stable_vault_by_app = await vault.get_stable_vault_by_app(2)
    print(stable_vault_by_app) 

    #Query stable vault by app and extended pair
    stable_vault_by_app_and_extended_pair = await vault.get_stable_vault_by_app_and_extended_pair(2,1)
    print(stable_vault_by_app_and_extended_pair)

    #Query extended pair vault mapping by app and extended pair
    extended_pair_vault_mapping_by_app_and_extended_pair = await vault.get_extended_pair_vault_mapping_by_app_and_extended_pair(2,3)
    print(extended_pair_vault_mapping_by_app_and_extended_pair.to_dict())

    #Query extended pair vault mapping by app
    extended_pair_vault_mapping_by_app = await vault.get_extended_pair_vault_mapping_by_app(2)
    print(extended_pair_vault_mapping_by_app)

    #Query tvl by app of all extended pairs
    tvl_by_app_of_all_extended_pairs = await vault.get_tvl_by_app_of_all_extended_pairs(2)
    print(tvl_by_app_of_all_extended_pairs)

    #Query tvl by app
    tvl_by_app = await vault.get_tvl_by_app(1)
    print(tvl_by_app)

    #Query user my position by app
    user_my_position_by_app = await vault.get_user_my_position_by_app(2,"")
    print(user_my_position_by_app.to_dict())

    #Query pairs locked and minted statistics by app
    pairs_locked_and_minted_statistic_by_app = await vault.get_pairs_locked_and_minted_statistic_by_app(2)
    print(pairs_locked_and_minted_statistic_by_app)

    #Query all stable mint vault rewards
    all_stable_mint_vault_rewards = await vault.get_all_stable_mint_vault_rewards()
    print(all_stable_mint_vault_rewards)

    #Query user extended pair total data
    user_extended_pair_total_data = await vault.get_user_extended_pair_total_data("")
    print(user_extended_pair_total_data)



"""
    TRANSACTIONS
"""

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


#----MsgDepositRequest----

    wallet = Wallet.from_mnemonic("")
    sender = wallet.get_address().to_acc_bech32()
    msg_deposit_request = MsgDepositRequest(
        from_ = sender,
        app_id = 2,
        extended_pair_vault_id = 2,
        user_vault_id = 23,
        amount="2000000"
    )
    response = await SignAndBroadcastMessage.send_tx(connection, wallet, msg_deposit_request)
    print(response)


#----MsgWithdrawRequest----

    wallet = Wallet.from_mnemonic("")
    sender = wallet.get_address().to_acc_bech32()
    msg_withdraw_request = MsgWithdrawRequest(
        from_ = sender,
        app_id = 2,
        extended_pair_vault_id = 2,
        user_vault_id = 23,
        amount="2000000"
    )
    response = await SignAndBroadcastMessage.send_tx(connection, wallet, msg_withdraw_request)
    print(response)


#----MsgDrawRequest----

    wallet = Wallet.from_mnemonic("")
    sender = wallet.get_address().to_acc_bech32()
    msg_draw_request = MsgDrawRequest(
        from_ = sender,
        app_id = 2,
        extended_pair_vault_id = 2,
        user_vault_id = 22,
        amount="1000000"
    )
    response = await SignAndBroadcastMessage.send_tx(connection, wallet, msg_draw_request)
    print(response)


#----MsgRepayRequest----

    wallet = Wallet.from_mnemonic("")
    sender = wallet.get_address().to_acc_bech32()
    msg_repay_request = MsgRepayRequest(
        from_=sender,
        app_id = 2,
        extended_pair_vault_id = 5,
        user_vault_id = 5,
        amount="2000"
    )
    response = await SignAndBroadcastMessage.send_tx(connection, wallet, msg_repay_request)
    print(response)


#----MsgCloseRequest----

    wallet = Wallet.from_mnemonic("")
    sender = wallet.get_address().to_acc_bech32()
    msg_close_request = MsgCloseRequest(
        from_ = sender,
        app_id = 2,
        extended_pair_vault_id = 2,
        user_vault_id = 22
    )
    response = await SignAndBroadcastMessage.send_tx(connection, wallet, msg_close_request)
    print(response)


#----MsgDepositAndDrawRequest----

    wallet = Wallet.from_mnemonic("")
    sender = wallet.get_address().to_acc_bech32()
    msg_deposit_and_draw_request = MsgDepositAndDrawRequest(
        from_ = sender,
        app_id = 2,
        extended_pair_vault_id = 2,
        user_vault_id = 23,
        amount="5000000"
    )
    response = await SignAndBroadcastMessage.send_tx(connection, wallet, msg_deposit_and_draw_request)
    print(response)


#----MsgCreateStableMintRequest----

    wallet = Wallet.from_mnemonic("")
    sender = wallet.get_address().to_acc_bech32()
    msg_create_stable_mint_request = MsgCreateStableMintRequest(
        from_ = sender,
        app_id = 2,
        extended_pair_vault_id = 2,
        amount="1000000"
    )
    response = await SignAndBroadcastMessage.send_tx(connection, wallet, msg_create_stable_mint_request)
    print(response)


#----MsgDepositStableMintRequest----

    wallet = Wallet.from_mnemonic("")
    sender = wallet.get_address().to_acc_bech32()
    msg_deposit_stable_mint_request = MsgDepositStableMintRequest(
        from_ = sender,
        app_id = 2,
        extended_pair_vault_id = 1,
        amount = "5000000",
        stable_vault_id = 1
    )
    response = await SignAndBroadcastMessage.send_tx(connection, wallet, msg_deposit_stable_mint_request)
    print(response)


#----MsgWithdrawStableMintRequest----

    wallet = Wallet.from_mnemonic("")
    sender = wallet.get_address().to_acc_bech32()
    msg_withdraw_stable_mint_request = MsgWithdrawStableMintRequest(
        from_ = sender,
        app_id = 2,
        extended_pair_vault_id = 1,
        amount = "5000000",
        stable_vault_id = 1
    )
    response = await SignAndBroadcastMessage.send_tx(connection, wallet, msg_withdraw_stable_mint_request)
    print(response)


#----MsgVaultInterestCalcRequest----

    wallet = Wallet.from_mnemonic("")
    sender = wallet.get_address().to_acc_bech32()
    msg_vault_interest_calc_request = MsgVaultInterestCalcRequest(
        from_ = sender,
        app_id = 2,
        user_vault_id = 2
    )
    response = await SignAndBroadcastMessage.send_tx(connection, wallet, msg_vault_interest_calc_request)
    print(response)



  

async def main():
    connection = await get_connection()
    await query(connection.channel())       # For Query
    await sample_tx(connection)             # For Transaction
    connection.close()


if __name__ == "__main__":
    asyncio.run(main())
    