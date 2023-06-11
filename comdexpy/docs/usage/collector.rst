============
Collector
============

.. code:: python


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


    async def main():
    connection = await get_connection()
    await query(connection.channel())
    connection.close()


 if __name__ == "__main__":
    asyncio.run(main())