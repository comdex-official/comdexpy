import asyncio
from comdexpy.client import Client

from comdexpy.queries.comdex.esm import Query as ESMQueries



async def get_connection():
    grpc_url = "comdex-grpc.lavenderfive.com"
    return Client.from_endpoint(grpc_url, 443)

async def query(channel):
    esm = ESMQueries(channel)

    #Query params
    params = await esm.get_params()
    print(params)
    
    #Query esm trigger params
    esm_trigger_params = await esm.get_esm_trigger_params(1)
    print(esm_trigger_params)
    
    #Query esm status
    esm_status = await esm.get_esm_status(1)
    print(esm_status)

    #Query current deposit stats
    current_deposit_stats = await esm.get_current_deposit_stats(1)
    print(current_deposit_stats)

    #Query users deposit mapping
    users_deposit_mapping = await esm.get_users_deposit_mapping(1, "")
    print(users_deposit_mapping.to_dict())

    #Query data after cool off
    data_after_cool_off = await esm.get_data_after_cool_off(1)
    print(data_after_cool_off)

    #Query snapshot price
    snapshot_price = await esm.get_snapshot_price(2,3)
    print(snapshot_price.to_dict())

    #Query asset data after cool off
    asset_data_after_cool_off = await esm.get_asset_data_after_cool_off(1)
    print(asset_data_after_cool_off)

    
    

async def main():
    connection = await get_connection()
    await query(connection.channel())
    connection.close()


if __name__ == "__main__":
    asyncio.run(main())