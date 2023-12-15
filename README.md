
![](comdexpy/docs/images/imgcomdex.png)



# comdexpy


The comdexpy is a comprehensive Python library designed to provide developers with easy access to the Comdex blockchain and its ecosystem. 
This library enables developers to interact with the blockchain, query data, and perform various operations within the Comdex ecosystem.




## Installation


```bash
  pip3 install comdexpy
```
    

## Usage

### Creating a connection

```python

import asyncio
from comdexpy.client import Client

async def get_connection():
    grpc_url = "comdex-grpc.lavenderfive.com"
    return Client.from_endpoint(grpc_url, 443)

async def main():
    connection = await get_connection()
    connection.close()

if __name__ == "__main__":
    asyncio.run(main())

```

### Querying on comdex node using connection

```python

import asyncio
from comdexpy.client import Client
from comdexpy.queries.comdex.liquidity import Query as LiquidityQueries

async def get_connection():
    grpc_url = "comdex-grpc.lavenderfive.com"
    return Client.from_endpoint(grpc_url, 443)

async def sample_query(channel):
    liquidity = LiquidityQueries(channel)
    params = await liquidity.get_generic_params(1)
    print(params.to_dict())

async def main():
    connection = await get_connection()
    await sample_query(connection.channel())
    connection.close()

if __name__ == "__main__":
    asyncio.run(main())

```

### Sending transaction on comdex node

```python
import asyncio
from comdexpy.client import Client
from comdexpy.wallet import Wallet

from comdexpy.messages.cosmos.bank import MsgSend
from comdexpy.proto.cosmos.base.v1beta1 import Coin

from comdexpy.send_tx import SignAndBroadcastMessage

async def get_connection():
    grpc_url = "comdex-grpc.lavenderfive.com"
    return Client.from_endpoint(grpc_url, 443)

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
    await sample_tx(connection)
    connection.close()


if __name__ == "__main__":
    asyncio.run(main())

```

### Complete Usage

![](https://github-production-user-asset-6210df.s3.amazonaws.com/43311385/245070505-bd499173-2d64-4ab5-8b60-e5254affeec1.png)

## Documentation

You can read the documentation [here.](https://comdex-official.github.io/comdexpy/comdexpy/docs/docs/html/index.html)


## Feedback

If you have any feedback, please reach out to us at https://forum.comdex.one/


## License

This software is licensed under the GPL-3.0 license. See [LICENSE](https://comdex-official.github.io/comdexpy/LICENSE) for full disclosure.



[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)







