import asyncio
from comdexpy.client import Client

from comdexpy.queries.comdex.asset import Query as AssetQueries



async def get_connection():
    grpc_url = "comdex-grpc.lavenderfive.com"
    return Client.from_endpoint(grpc_url, 443)

async def query(channel):
    asset = AssetQueries(channel)

    #Query assets
    assets_info = await asset.get_assets()
    print(assets_info)
    
    #Query asset
    asset_info = await asset.get_asset(1)
    print(asset_info)
    
    #Query asset pairs
    pairs = await asset.get_asset_pairs()
    print(pairs)

    #Query asset pair
    pair = await asset.get_asset_pair(1)
    print(pair)

    #Query app
    app = await asset.get_app(1)
    print(app)

    #Query gov token by app
    gov_token_by_app = await asset.get_gov_token_by_app(1)
    print(gov_token_by_app)

    #Query apps
    apps = await asset.get_apps()
    print(apps)
    
    #Query extended pair vault
    extended_pair_vault = await asset.get_extended_pair_vault(1)
    print(extended_pair_vault)

    #Query all extended pair vaults
    all_extended_pair_vaults = await asset.get_all_extended_pair_vaults()
    print(all_extended_pair_vaults)
   
    #Query all extended pair vaults by app
    all_extended_pair_vaults_by_app = await asset.get_all_extended_pair_vaults_by_app(1)
    print(all_extended_pair_vaults_by_app)

    #Query all extended pair stable vaults id by app
    all_extended_pair_stable_vaults_id_by_app = await asset.get_all_extended_pair_stable_vaults_id_by_app(1)
    print(all_extended_pair_stable_vaults_id_by_app)

    #Query all extended pair stable vaults by app
    all_extended_pair_stable_vaults_by_app = await asset.get_all_extended_pair_stable_vaults_by_app(1)
    print(all_extended_pair_stable_vaults_by_app)

    #Query extended pair vaults by app without stable
    extended_pair_vaults_by_app_without_stable = await asset.get_extended_pair_vaults_by_app_without_stable(1)
    print(extended_pair_vaults_by_app_without_stable)

    
    

async def main():
    connection = await get_connection()
    await query(connection.channel())
    connection.close()


if __name__ == "__main__":
    asyncio.run(main())