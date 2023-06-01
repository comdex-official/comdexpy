import asyncio
from comdexpy.client import Client

from comdexpy.queries.comdex.collector import Query as CollectorQueries



async def get_connection():
    grpc_url = "comdex-grpc.lavenderfive.com"
    return Client.from_endpoint(grpc_url, 443)

async def query(channel):
    collector = CollectorQueries(channel)

    #Query params
    params = await collector.get_params()
    print(params)
    
    #Query collector lookup by app
    collector_lookup_by_app = await collector.get_collector_lookup_by_app(1)
    print(collector_lookup_by_app)
    
    #Query collector lookup by app and asset
    collector_lookup_by_app_and_asset = await collector.get_collector_lookup_by_app_and_asset(1, 1)
    print(collector_lookup_by_app_and_asset.to_dict())

    #Query collector data by app and asset
    collector_data_by_app_and_asset = await collector.get_collector_data_by_app_and_asset(2, 3)
    print(collector_data_by_app_and_asset.to_dict())

    #Query auction mapping for app and asset
    auction_mapping_for_app_and_asset = await collector.get_auction_mapping_for_app_and_asset(1, 1)
    print(auction_mapping_for_app_and_asset.to_dict())

    #Query net fee collected for app and asset
    net_fee_collected_for_app_and_asset = await collector.get_net_fee_collected_for_app_and_asset(1, 1)
    print(net_fee_collected_for_app_and_asset.to_dict())

    
    

async def main():
    connection = await get_connection()
    await query(connection.channel())
    connection.close()


if __name__ == "__main__":
    asyncio.run(main())