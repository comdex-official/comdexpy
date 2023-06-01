from dataclasses import dataclass

from ...base import BaseMessageWrapper

from ....proto.comdex.liquidity.v1beta1 import (
    MsgCreatePair as MsgCreatePairProto,
    MsgCreatePool as MsgCreatePoolProto,
    MsgCreateRangedPool as MsgCreateRangedPoolProto,
    MsgDeposit as MsgDepositProto,
    MsgWithdraw as MsgWithdrawProto,
    MsgLimitOrder as MsgLimitOrderProto,
    MsgMarketOrder as MsgMarketOrderProto,
    MsgMmOrder as MsgMmOrderProto,
    MsgCancelOrder as MsgCancelOrderProto,
    MsgCancelAllOrders as MsgCancelAllOrdersProto,
    MsgCancelMmOrder as MsgCancelMmOrderProto,
    MsgFarm as MsgFarmProto,
    MsgUnfarm as MsgUnfarmProto
)

from comdexpy.proto.cosmos.base import v1beta1 as ___cosmos_base_v1_beta1__
from comdexpy.proto.cosmos.base.query import v1beta1 as ___cosmos_base_query_v1_beta1__

from ....proto.cosmos.base import v1beta1 as __base_v1_beta1__
from ....proto.cosmos.base.query import v1beta1 as __base_query_v1_beta1__

assert __base_v1_beta1__
assert __base_query_v1_beta1__


class MsgCreatePair(BaseMessageWrapper, MsgCreatePairProto):
    @property
    def type_url(self):
        return "/comdex.liquidity.v1beta1.MsgCreatePair"

    @property
    def legacy_url(self):
        return "comdex/liquidity/MsgCreatePair"



class MsgCreatePool(BaseMessageWrapper, MsgCreatePoolProto):
    @property
    def type_url(self):
        return "/comdex.liquidity.v1beta1.MsgCreatePool"

    @property
    def legacy_url(self):
        return "comdex/liquidity/MsgCreatePool"
    


class MsgCreateRangedPool(BaseMessageWrapper, MsgCreateRangedPoolProto):
    @property
    def type_url(self):
        return "/comdex.liquidity.v1beta1.MsgCreateRangedPool"

    @property
    def legacy_url(self):
        return "comdex/liquidity/MsgCreateRangedPool"
    


class MsgDeposit(BaseMessageWrapper, MsgDepositProto):
    @property
    def type_url(self):
        return "/comdex.liquidity.v1beta1.MsgDeposit"

    @property
    def legacy_url(self):
        return "comdex/liquidity/MsgDeposit"
    


class MsgWithdraw(BaseMessageWrapper, MsgWithdrawProto):
    @property
    def type_url(self):
        return "/comdex.liquidity.v1beta1.MsgWithdraw"

    @property
    def legacy_url(self):
        return "comdex/liquidity/MsgWithdraw"
    


class MsgLimitOrder(BaseMessageWrapper, MsgLimitOrderProto):
    @property
    def type_url(self):
        return "/comdex.liquidity.v1beta1.MsgLimitOrder"

    @property
    def legacy_url(self):
        return "comdex/liquidity/MsgLimitOrder"   
    


class MsgMarketOrder(BaseMessageWrapper, MsgMarketOrderProto):
    @property
    def type_url(self):
        return "/comdex.liquidity.v1beta1.MsgMarketOrder"

    @property
    def legacy_url(self):
        return "comdex/liquidity/MsgMarketOrder"



class MsgMmOrder(BaseMessageWrapper, MsgMmOrderProto):
    @property
    def type_url(self):
        return "/comdex.liquidity.v1beta1.MsgMMOrder"

    @property
    def legacy_url(self):
        return "comdex/liquidity/MsgMMOrder"
    


class MsgCancelOrder(BaseMessageWrapper, MsgCancelOrderProto):
    @property
    def type_url(self):
        return "/comdex.liquidity.v1beta1.MsgCancelOrder"

    @property
    def legacy_url(self):
        return "comdex/liquidity/MsgCancelOrder"
    


class MsgCancelAllOrders(BaseMessageWrapper, MsgCancelAllOrdersProto):
    @property
    def type_url(self):
        return "/comdex.liquidity.v1beta1.MsgCancelAllOrders"

    @property
    def legacy_url(self):
        return "comdex/liquidity/MsgCancelAllOrders"
    


class MsgCancelMmOrder(BaseMessageWrapper, MsgCancelMmOrderProto):
    @property
    def type_url(self):
        return "/comdex.liquidity.v1beta1.MsgCancelMMOrder"

    @property
    def legacy_url(self):
        return "comdex/liquidity/MsgCancelMMOrder"
    


class MsgFarm(BaseMessageWrapper, MsgFarmProto):
    @property
    def type_url(self):
        return "/comdex.liquidity.v1beta1.MsgFarm"

    @property
    def legacy_url(self):
        return "comdex/liquidity/MsgFarm"
    


class MsgUnfarm(BaseMessageWrapper, MsgUnfarmProto):
    @property
    def type_url(self):
        return "/comdex.liquidity.v1beta1.MsgUnfarm"

    @property
    def legacy_url(self):
        return "comdex/liquidity/MsgUnfarm"