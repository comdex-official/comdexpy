from dataclasses import dataclass

from ...base import BaseMessageWrapper

from ....proto.comdex.lend.v1beta1 import (
    MsgLend as MsgLendProto,
    MsgCloseLend as MsgCloseLendProto,
    MsgBorrow as MsgBorrowProto,
    MsgDeposit as MsgDepositProto,
    MsgWithdraw as MsgWithdrawProto,
    MsgRepay as MsgRepayProto,
    MsgDepositBorrow as MsgDepositBorrowProto,
    MsgDraw as MsgDrawProto,
    MsgCloseBorrow as MsgCloseBorrowProto,
    MsgBorrowAlternate as MsgBorrowAlternateProto,
    MsgFundModuleAccounts as MsgFundModuleAccountsProto,
    MsgCalculateInterestAndRewards as MsgCalculateInterestAndRewardsProto,
    MsgFundReserveAccounts as MsgFundReserveAccountsProto
)

from comdexpy.proto.cosmos.base import v1beta1 as ___cosmos_base_v1_beta1__
from comdexpy.proto.cosmos.base.query import v1beta1 as ___cosmos_base_query_v1_beta1__


from ....proto.cosmos.base import v1beta1 as __base_v1_beta1__
from ....proto.cosmos.base.query import v1beta1 as __base_query_v1_beta1__

assert __base_v1_beta1__
assert __base_query_v1_beta1__


class MsgLend(BaseMessageWrapper, MsgLendProto):
    @property
    def type_url(self):
        return "/comdex.lend.v1beta1.MsgLend"

    @property
    def legacy_url(self):
        return "comdex/lend/MsgLend"



class MsgDeposit(BaseMessageWrapper, MsgDepositProto):
    @property
    def type_url(self):
        return "/comdex.lend.v1beta1.MsgDeposit"

    @property
    def legacy_url(self):
        return "comdex/lend/MsgDeposit"
    


class MsgWithdraw(BaseMessageWrapper, MsgWithdrawProto):
    @property
    def type_url(self):
        return "/comdex.lend.v1beta1.MsgWithdraw"

    @property
    def legacy_url(self):
        return "comdex/lend/MsgWithdraw"
    


class MsgCloseLend(BaseMessageWrapper, MsgCloseLendProto):
    @property
    def type_url(self):
        return "/comdex.lend.v1beta1.MsgCloseLend"

    @property
    def legacy_url(self):
        return "comdex/lend/MsgCloseLend"
    


class MsgBorrow(BaseMessageWrapper, MsgBorrowProto):
    @property
    def type_url(self):
        return "/comdex.lend.v1beta1.MsgBorrow"

    @property
    def legacy_url(self):
        return "comdex/lend/MsgBorrow"
    


class MsgRepay(BaseMessageWrapper, MsgRepayProto):
    @property
    def type_url(self):
        return "/comdex.lend.v1beta1.MsgRepay"

    @property
    def legacy_url(self):
        return "comdex/lend/MsgRepay"   
    


class MsgDepositBorrow(BaseMessageWrapper, MsgDepositBorrowProto):
    @property
    def type_url(self):
        return "/comdex.lend.v1beta1.MsgDepositBorrow"

    @property
    def legacy_url(self):
        return "comdex/lend/MsgDepositBorrow"



class MsgDraw(BaseMessageWrapper, MsgDrawProto):
    @property
    def type_url(self):
        return "/comdex.lend.v1beta1.MsgDraw"

    @property
    def legacy_url(self):
        return "comdex/lend/MsgDraw"
    


class MsgCloseBorrow(BaseMessageWrapper, MsgCloseBorrowProto):
    @property
    def type_url(self):
        return "/comdex.lend.v1beta1.MsgCloseBorrow"

    @property
    def legacy_url(self):
        return "comdex/lend/MsgCloseBorrow"
    


class MsgBorrowAlternate(BaseMessageWrapper, MsgBorrowAlternateProto):
    @property
    def type_url(self):
        return "/comdex.lend.v1beta1.MsgBorrowAlternate"

    @property
    def legacy_url(self):
        return "comdex/lend/MsgBorrowAlternate"
    


class MsgFundModuleAccounts(BaseMessageWrapper, MsgFundModuleAccountsProto):
    @property
    def type_url(self):
        return "/comdex.lend.v1beta1.MsgFundModuleAccounts"

    @property
    def legacy_url(self):
        return "comdex/lend/MsgFundModuleAccounts"
    


class MsgCalculateInterestAndRewards(BaseMessageWrapper, MsgCalculateInterestAndRewardsProto):
    @property
    def type_url(self):
        return "/comdex.lend.v1beta1.MsgCalculateInterestAndRewards"

    @property
    def legacy_url(self):
        return "comdex/lend/MsgCalculateInterestAndRewards"
    


class MsgFundReserveAccounts(BaseMessageWrapper, MsgFundReserveAccountsProto):
    @property
    def type_url(self):
        return "/comdex.lend.v1beta1.MsgFundReserveAccounts"

    @property
    def legacy_url(self):
        return "comdex/lend/MsgFundReserveAccounts"
    



