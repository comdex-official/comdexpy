==========
ESM
==========

.. code:: python


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


 async def main():
    connection = await get_connection()
    await query(connection.channel())
    connection.close()


 if __name__ == "__main__":
    asyncio.run(main())


