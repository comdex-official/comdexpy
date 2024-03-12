
from .client import Client
from .messages.base import BaseMessageWrapper
from .wallet import Wallet
from .transaction import Transaction
from .proto.cosmos.tx.v1beta1 import BroadcastMode

class SignAndBroadcastMessage():
    def __init__(self) -> None:
        pass

    @classmethod
    async def send_tx(self,
        connection: Client,
        wallet: Wallet,
        message: BaseMessageWrapper,
        gas_price: float = 0.0025,
        gas_limit: int = 2000000,
        memo = "Message Signed And Broadcasted Using Comdex's Python SDK",
        mode = BroadcastMode.BROADCAST_MODE_SYNC
    ):
        sender = wallet.get_address().to_acc_bech32()
        account = await connection.get_account(sender)
        account_num = account.account_number
        sequence = account.sequence
        chain_id = await connection.get_chain_id()

        # cosnstructing a transaction
        txn = (
            Transaction()
            .with_messages(message)
            .with_sequence(sequence)
            .with_account_num(account_num)
            .with_chain_id(chain_id)
            .with_gas_price(gas_price)
            .with_gas_limit(gas_limit)
            .with_memo(memo)
        )

        # Sign and broadcast a transaction
        if mode == BroadcastMode.BROADCAST_MODE_SYNC:
            tx_block = await connection.send_tx_sync_mode(wallet.sign_and_build(txn))
        elif mode == BroadcastMode.BROADCAST_MODE_ASYNC:
            tx_block = await connection.send_tx_async_mode(wallet.sign_and_build(txn))
        else:
            tx_block = await connection.send_tx_block_mode(wallet.sign_and_build(txn))


        # Converting to dict for readability
        response = tx_block.to_dict()
        return response