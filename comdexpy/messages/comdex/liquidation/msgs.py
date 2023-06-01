from dataclasses import dataclass

from ...base import BaseMessageWrapper

from ....proto.comdex.liquidation.v1beta1 import (
    MsgLiquidateVaultRequest as MsgLiquidateVaultRequestProto,
    MsgLiquidateBorrowRequest as MsgLiquidateBorrowRequestProto
)




from ....proto.cosmos.base import v1beta1 as __base_v1_beta1__
from ....proto.cosmos.base.query import v1beta1 as __base_query_v1_beta1__

assert __base_v1_beta1__
assert __base_query_v1_beta1__


class MsgLiquidateVaultRequest(BaseMessageWrapper, MsgLiquidateVaultRequestProto):
    @property
    def type_url(self):
        return "/comdex.liquidation.v1beta1.MsgLiquidateVaultRequest"

    @property
    def legacy_url(self):
        return "comdex/liquidation/MsgLiquidateVaultRequest"



class MsgLiquidateBorrowRequest(BaseMessageWrapper, MsgLiquidateBorrowRequestProto):
    @property
    def type_url(self):
        return "/comdex.liquidation.v1beta1.MsgLiquidateBorrowRequest"

    @property
    def legacy_url(self):
        return "comdex/liquidation/MsgLiquidateBorrowRequest"
    





