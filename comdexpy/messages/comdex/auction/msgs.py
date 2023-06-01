from dataclasses import dataclass

from ...base import BaseMessageWrapper

from ....proto.comdex.auction.v1beta1 import (
                    MsgPlaceSurplusBidRequest as MsgPlaceSurplusBidRequestProto,
                    MsgPlaceDebtBidRequest as MsgPlaceDebtBidRequestProto,
                    MsgPlaceDutchBidRequest as MsgPlaceDutchBidRequestProto,
                    MsgPlaceDutchLendBidRequest as MsgPlaceDutchLendBidRequestProto
)


from comdexpy.proto.cosmos.base import v1beta1 as ___cosmos_base_v1_beta1__
from comdexpy.proto.cosmos.base.query import v1beta1 as ___cosmos_base_query_v1_beta1__

from ....proto.cosmos.base import v1beta1 as __base_v1_beta1__
from ....proto.cosmos.base.query import v1beta1 as __base_query_v1_beta1__

assert __base_v1_beta1__
assert __base_query_v1_beta1__


class MsgPlaceSurplusBidRequest(BaseMessageWrapper, MsgPlaceSurplusBidRequestProto):
    @property
    def type_url(self):
        return "/comdex.auction.v1beta1.MsgPlaceSurplusBidRequest"

    @property
    def legacy_url(self):
        return "comdex/auction/MsgPlaceSurplusBidRequest"


    
class MsgPlaceDebtBidRequest(BaseMessageWrapper, MsgPlaceDebtBidRequestProto):
    @property
    def type_url(self):
        return "/comdex.auction.v1beta1.MsgPlaceDebtBidRequest"

    @property
    def legacy_url(self):
        return "comdex/auction/MsgPlaceDebtBidRequest"
    


class MsgPlaceDutchBidRequest(BaseMessageWrapper, MsgPlaceDutchBidRequestProto):
    @property
    def type_url(self):
        return "/comdex.auction.v1beta1.MsgPlaceDutchBidRequest"

    @property
    def legacy_url(self):
        return "comdex/auction/MsgPlaceDutchBidRequest"
    


class MsgPlaceDutchLendBidRequest(BaseMessageWrapper, MsgPlaceDutchLendBidRequestProto):
    @property
    def type_url(self):
        return "/comdex.auction.v1beta1.MsgPlaceDutchLendBidRequest"

    @property
    def legacy_url(self):
        return "comdex/auction/MsgPlaceDutchLendBidRequest"
    


    

