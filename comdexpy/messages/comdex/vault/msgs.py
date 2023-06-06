from dataclasses import dataclass

from ...base import BaseMessageWrapper

from ....proto.comdex.vault.v1beta1 import (
    MsgCreateRequest as MsgCreateRequestProto,
    MsgDepositRequest as MsgDepositRequestProto,
    MsgWithdrawRequest as MsgWithdrawRequestProto,
    MsgDrawRequest as MsgDrawRequestProto,
    MsgRepayRequest as MsgRepayRequestProto,
    MsgCloseRequest as MsgCloseRequestProto,
    MsgDepositAndDrawRequest as MsgDepositAndDrawRequestProto,
    MsgCreateStableMintRequest as MsgCreateStableMintRequestProto,
    MsgDepositStableMintRequest as MsgDepositStableMintRequestProto,
    MsgWithdrawStableMintRequest as MsgWithdrawStableMintRequestProto,
    MsgVaultInterestCalcRequest as MsgVaultInterestCalcRequestProto
)




from ....proto.cosmos.base import v1beta1 as __base_v1_beta1__
from ....proto.cosmos.base.query import v1beta1 as __base_query_v1_beta1__

assert __base_v1_beta1__
assert __base_query_v1_beta1__


class MsgCreateRequest(BaseMessageWrapper, MsgCreateRequestProto):
    @property
    def type_url(self):
        return "/comdex.vault.v1beta1.MsgCreateRequest"

    @property
    def legacy_url(self):
        return "comdex/vault/MsgCreateRequest"



class MsgDepositRequest(BaseMessageWrapper, MsgDepositRequestProto):
    @property
    def type_url(self):
        return "/comdex.vault.v1beta1.MsgDepositRequest"

    @property
    def legacy_url(self):
        return "comdex/vault/MsgDepositRequest"
    


class MsgWithdrawRequest(BaseMessageWrapper, MsgWithdrawRequestProto):
    @property
    def type_url(self):
        return "/comdex.vault.v1beta1.MsgWithdrawRequest"

    @property
    def legacy_url(self):
        return "comdex/vault/MsgWithdrawRequest"
    


class MsgDrawRequest(BaseMessageWrapper, MsgDrawRequestProto):
    @property
    def type_url(self):
        return "/comdex.vault.v1beta1.MsgDrawRequest"

    @property
    def legacy_url(self):
        return "comdex/vault/MsgDrawRequest"
    


class MsgRepayRequest(BaseMessageWrapper, MsgRepayRequestProto):
    @property
    def type_url(self):
        return "/comdex.vault.v1beta1.MsgRepayRequest"

    @property
    def legacy_url(self):
        return "comdex/vault/MsgRepayRequest"
    


class MsgCloseRequest(BaseMessageWrapper, MsgCloseRequestProto):
    @property
    def type_url(self):
        return "/comdex.vault.v1beta1.MsgCloseRequest"

    @property
    def legacy_url(self):
        return "comdex/vault/MsgCloseRequest"   
    


class MsgDepositAndDrawRequest(BaseMessageWrapper, MsgDepositAndDrawRequestProto):
    @property
    def type_url(self):
        return "/comdex.vault.v1beta1.MsgDepositAndDrawRequest"

    @property
    def legacy_url(self):
        return "comdex/vault/MsgDepositAndDrawRequest"



class MsgCreateStableMintRequest(BaseMessageWrapper, MsgCreateStableMintRequestProto):
    @property
    def type_url(self):
        return "/comdex.vault.v1beta1.MsgCreateStableMintRequest"

    @property
    def legacy_url(self):
        return "comdex/vault/MsgCreateStableMintRequest"
    


class MsgDepositStableMintRequest(BaseMessageWrapper, MsgDepositStableMintRequestProto):
    @property
    def type_url(self):
        return "/comdex.vault.v1beta1.MsgDepositStableMintRequest"

    @property
    def legacy_url(self):
        return "comdex/vault/MsgDepositStableMintRequest"
    


class MsgWithdrawStableMintRequest(BaseMessageWrapper, MsgWithdrawStableMintRequestProto):
    @property
    def type_url(self):
        return "/comdex.vault.v1beta1.MsgWithdrawStableMintRequest"

    @property
    def legacy_url(self):
        return "comdex/vault/MsgWithdrawStableMintRequest"
    


class MsgVaultInterestCalcRequest(BaseMessageWrapper, MsgVaultInterestCalcRequestProto):
    @property
    def type_url(self):
        return "/comdex.vault.v1beta1.MsgVaultInterestCalcRequest"

    @property
    def legacy_url(self):
        return "comdex/vault/MsgVaultInterestCalcRequest"
    

