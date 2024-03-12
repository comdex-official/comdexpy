import time
from typing import List

from grpclib.client import Channel

from .proto.cosmos.auth.v1beta1 import BaseAccount, QueryAccountRequest
from .proto.cosmos.auth.v1beta1 import QueryStub as AuthQueryStub
from .proto.cosmos.base.abci.v1beta1 import TxResponse
from .proto.cosmos.base.tendermint.v1beta1 import GetLatestBlockRequest, GetLatestBlockResponse
from .proto.cosmos.base.tendermint.v1beta1 import ServiceStub as TendermintServiceStub
from .proto.cosmos.crypto.secp256k1 import PubKey
from .proto.cosmos.tx.v1beta1 import GetTxRequest, BroadcastTxRequest, BroadcastMode, SimulateRequest, SimulateResponse
from .proto.cosmos.tx.v1beta1 import ServiceStub as TxServiceStub


class Client:
    """Class for instantiating a client side connection with Comdex chain."""

    def __init__(self, channel: Channel):
        self.__channel = channel
        self.stub_cosmos_tendermint = TendermintServiceStub(self.__channel)
        self.stub_auth = AuthQueryStub(self.__channel)
        self.stub_tx = TxServiceStub(self.__channel)

    def __del__(self) -> None:
        self.close()

    def close(self) -> None:
        """Closes the connection."""

        self.__channel.close()
    
    def channel(self) -> Channel:
        return self.__channel

    @classmethod
    def from_endpoint(cls, grpc_endpoint: str, port: int, ssl: bool = True):
        """Creates a client instance from a given endpoint and port.

        Args:
            grpc_endpoint: The GRPC endpoint to connect too.
            port: The endpoint port.
            ssl: If true, SSL context is used.

        Returns:
            A Client instance.
        """

        return cls(Channel(host=grpc_endpoint, port=port, ssl=ssl))


    async def get_latest_block(self) -> GetLatestBlockResponse:
        """Gets the latest block on chain.

        Returns:
            The details of the latest block.
        """

        return await self.stub_cosmos_tendermint.get_latest_block(GetLatestBlockRequest())

    async def get_account(self, address: str) -> BaseAccount:
        """Gets the account details of a specified address.

        Args:
            address: The address to retrieve the detail of.

        Returns:
            The account details.
        """

        try:
            resp = await self.stub_auth.account(QueryAccountRequest(address=address))
            account = BaseAccount()
            pub_key = PubKey()

            account.parse(resp.account.value)
            account.pub_key = pub_key.parse(account.pub_key.value)
        except Exception as e:
            raise e

        return account

    async def send_tx_sync_mode(self, tx_bytes: bytes) -> TxResponse:
        """Sends a transaction in sync mode.

        Sends a transaction and waits until the transaction has passed the CheckTx phase.

        Args:
            tx_bytes: A signed transaction in raw bytes.

        Returns:
            The transaction response.
        """

        resp = await self.stub_tx.broadcast_tx(
            BroadcastTxRequest(tx_bytes=tx_bytes, mode=BroadcastMode.BROADCAST_MODE_SYNC)
        )
        return resp.tx_response

    async def send_tx_async_mode(self, tx_bytes: bytes) -> TxResponse:
        """Sends a transaction in async mode.

        Sends a transaction and returns the response immediately, without waiting for the transaction process.

        Args:
            tx_bytes: A signed transaction in raw bytes.

        Returns:
            The transaction response.
        """

        resp = await self.stub_tx.broadcast_tx(
            BroadcastTxRequest(tx_bytes=tx_bytes, mode=BroadcastMode.BROADCAST_MODE_ASYNC)
        )
        return resp.tx_response

    async def send_tx_block_mode(self, tx_bytes: bytes) -> TxResponse:
        """Sends a transaction in block mode.

        Sends a transaction and waits until the transaction has been committed to a block before returning the response.

        Args:
            tx_bytes: A signed transaction in raw bytes.

        Returns:
            The transaction response.
        """

        resp = await self.stub_tx.broadcast_tx(
            BroadcastTxRequest(tx_bytes=tx_bytes, mode=BroadcastMode.BROADCAST_MODE_BLOCK)
        )
        return resp.tx_response

    async def get_chain_id(self) -> str:
        """Gets the chain ID.

        Returns:
            The chain ID.
        """

        latest_block = await self.get_latest_block()
        return latest_block.block.header.chain_id

    async def get_tx_response(self, tx_hash: str) -> TxResponse:
        """Gets the tx response from a tx hash.

        Args:
            tx_hash: The transaction hash to retrieve the tx response of.

        Returns:
            The tx response.
        """
        resp = await self.stub_tx.get_tx(GetTxRequest(hash=tx_hash))
        return resp.tx_response

    async def simulate_tx(self, tx_bytes: bytes) -> SimulateResponse:
        """Simulates a transaction from the tx_bytes.

        Args:
            tx_bytes: A signed transaction in raw bytes.

        Returns:
            The simulated response.
        """
        return await self.stub_tx.simulate(SimulateRequest(tx_bytes=tx_bytes))
