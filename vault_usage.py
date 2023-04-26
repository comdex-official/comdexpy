import asyncio
from comdexpy.client import Client

from comdexpy.queries.comdex.vault import Query as VaultQueries



async def get_connection():
    grpc_url = "comdex-grpc.lavenderfive.com"
    return Client.from_endpoint(grpc_url, 443)

async def query(channel):
    vault = VaultQueries(channel)

    vault_info = await vault.get_vault_info(1)
    print(vault_info)
    
    vault_info_by_vault_id = await vault.get_vault_info_by_vault_id(1)
    print(vault_info_by_vault_id)
    
    vault_info_of_owner_by_app_id = await vault.get_vault_info_of_owner_by_app_id(1, "")
    print(vault_info_of_owner_by_app_id.to_dict())

    all_vaults = await vault.get_all_vaults()
    print(all_vaults)

    all_vaults_by_app = await vault.get_all_vaults_by_app(1)
    print(all_vaults_by_app)

    all_vaults_by_app_and_extended_pair = await vault.get_all_vaults_by_app_and_extended_pair(1, 1)
    print(all_vaults_by_app_and_extended_pair.to_dict())

    vault_id_of_owner_by_extended_pair_and_app = await vault.get_vault_id_of_owner_by_extended_pair_and_app(1, "", 1)
    print(vault_id_of_owner_by_extended_pair_and_app.to_dict())
    
    vault_ids_by_app_in_all_extended_pairs = await vault.get_vault_ids_by_app_in_all_extended_pairs(1)
    print(vault_ids_by_app_in_all_extended_pairs)

    all_vault_ids_by_an_owner = await vault.get_all_vault_ids_by_an_owner("")
    print(all_vault_ids_by_an_owner)
   
    token_minted_by_app_and_extended_pair = await vault.get_token_minted_by_app_and_extended_pair(1, 1)
    print(token_minted_by_app_and_extended_pair.to_dict())

    token_minted_asset_wise_by_app = await vault.get_token_minted_asset_wise_by_app(1)
    print(token_minted_asset_wise_by_app)

    vault_count_by_app = await vault.get_vault_count_by_app(1)
    print(vault_count_by_app)

    vault_count_by_app_and_extended_pair = await vault.get_vault_count_by_app_and_extended_pair(1, 1)
    print(vault_count_by_app_and_extended_pair.to_dict())

    total_value_locked_by_app_and_extended_pair = await vault.get_total_value_locked_by_app_and_extended_pair(1, 1)
    print(total_value_locked_by_app_and_extended_pair.to_dict())

    extended_pair_ids_by_app = await vault.get_extended_pair_ids_by_app(1)
    print(extended_pair_ids_by_app)    

    stable_vault_by_vault_id = await vault.get_stable_vault_by_vault_id(1)
    print(stable_vault_by_vault_id)  

    stable_vault_by_app = await vault.get_stable_vault_by_app(1)
    print(stable_vault_by_app) 

    stable_vault_by_app_and_extended_pair = await vault.get_stable_vault_by_app_and_extended_pair(1)
    print(stable_vault_by_app_and_extended_pair)

    extended_pair_vault_mapping_by_app_and_extended_pair = await vault.get_extended_pair_vault_mapping_by_app_and_extended_pair(1,1)
    print(extended_pair_vault_mapping_by_app_and_extended_pair.to_dict())

    extended_pair_vault_mapping_by_app = await vault.get_extended_pair_vault_mapping_by_app(1)
    print(extended_pair_vault_mapping_by_app)

    tvl_by_app_of_all_extended_pairs = await vault.get_tvl_by_app_of_all_extended_pairs(1)
    print(tvl_by_app_of_all_extended_pairs)

    tvl_by_app = await vault.get_tvl_by_app(1)
    print(tvl_by_app)

    user_my_position_by_app = await vault.get_user_my_position_by_app(1,"")
    print(user_my_position_by_app.to_dict())

    pairs_locked_and_minted_statistic_by_app = await vault.get_pairs_locked_and_minted_statistic_by_app(1)
    print(pairs_locked_and_minted_statistic_by_app)

    all_stable_mint_vault_rewards = await vault.get_all_stable_mint_vault_rewards()
    print(all_stable_mint_vault_rewards)

    user_extended_pair_total_data = await vault.get_user_extended_pair_total_data("")
    print(user_extended_pair_total_data)






    


    

async def main():
    connection = await get_connection()
    await query(connection.channel())
    #await sample_tx_deposit(connection)
    connection.close()


if __name__ == "__main__":
    asyncio.run(main())