import asyncio
from comdexpy.client import Client
from comdexpy.wallet import Wallet
from comdexpy.queries.comdex.liquidity import Query as LiquidityQueries
from comdexpy.queries.cosmos.bank import Query as BankQueries

from comdexpy.messages.cosmos.bank import MsgSend
from comdexpy.proto.cosmos.base.v1beta1 import Coin

from comdexpy.send_tx import SignAndBroadcastMessage

async def get_connection():
    grpc_url = "comdex-grpc.lavenderfive.com"
    return Client.from_endpoint(grpc_url, 443)

async def sample_query(channel):
    liquidity = LiquidityQueries(channel)
    params = await liquidity.get_generic_params(1)
    print(params.to_dict())

    bank = BankQueries(channel)
    params = await bank.get_params()
    print(params.to_dict())

async def sample_tx(connection):
    wallet = Wallet.from_mnemonic("seeds here")
    sender = wallet.get_address().to_acc_bech32()
    msg_send = MsgSend(
        from_address=sender,
        to_address="comdex",
        amount=[Coin(amount="1000000", denom="ucmdx")],
    )
    response = await SignAndBroadcastMessage.send_tx(connection, wallet, msg_send)
    print(response)


async def main():
    connection = await get_connection()
    await sample_query(connection.channel())
    await sample_tx(connection)
    connection.close()


if __name__ == "__main__":
    asyncio.run(main())