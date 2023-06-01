from grpclib.client import Channel
from typing import List

from comdexpy.proto.cosmos.base.query.v1beta1 import PageRequest

from comdexpy.proto.comdex.auction.v1beta1 import (
    QuerySurplusAuctionRequest,
    SurplusAuction,
    QuerySurplusAuctionsRequest,
    QuerySurplusAuctionsResponse,
    QuerySurplusBiddingsRequest,
    SurplusBiddings,
    QueryDebtAuctionRequest,
    DebtAuction,
    QueryDebtAuctionsRequest,
    QueryDebtAuctionsResponse,
    QueryDebtBiddingsRequest,
    DebtBiddings,
    QueryDutchAuctionRequest,
    DutchAuction,
    QueryDutchAuctionsRequest,
    QueryDutchAuctionsResponse,
    QueryDutchBiddingsRequest,
    DutchBiddings,
    QueryProtocolStatisticsRequest,
    ProtocolStatistics,
    QueryGenericAuctionParamRequest,
    AuctionParams,
    QueryDutchLendAuctionRequest,
    QueryDutchLendAuctionResponse,
    QueryDutchLendAuctionsRequest,
    QueryDutchLendAuctionsResponse,
    QueryDutchLendBiddingsRequest,
    QueryDutchLendBiddingsResponse,
    QueryFilterDutchAuctionsRequest,
    QueryFilterDutchAuctionsResponse,
    QueryBiddingsForSurplusAuctionRequest,
    QueryBiddingsForSurplusAuctionResponse

)
from comdexpy.proto.comdex.auction.v1beta1 import QueryStub as AuctionQueryStub


class Query():
    def __init__(self, channel: Channel) -> None:
        self.stub_auction = AuctionQueryStub(channel)


    async def get_surplus_auction(self, app_id: int, auction_mapping_id: int, auction_id: int, history:bool) -> SurplusAuction:

        """Retrieves a specific surplus auction based on the given parameters

        Args: 
                app_id (int): The application ID associated with the surplus auction.
                auction_mapping_id (int): The auction mapping ID used to map the auction.
                auction_id (int): The unique identifier of the surplus auction.
                history (bool): A flag indicating whether to include auction history in the response.

        Returns: 
                An instance of the SurplusAuction class, containing information about the requested surplus auction.
        """
        resp = await self.stub_auction.query_surplus_auction(QuerySurplusAuctionRequest(app_id=app_id, auction_mapping_id=auction_mapping_id, auction_id=auction_id, history=history))
        return resp.auction



    async def get_surplus_auctions(self, app_id: int, history: bool, pagination: PageRequest = None) -> QuerySurplusAuctionsResponse:

        """Retrieves surplus auctions data based on the given parameters.

        Args:
                app_id (int): The application ID for which to fetch surplus auction data.
                history (bool): A flag to determine if historical surplus auctions should be retrieved (True) or only active surplus auctions (False).
                pagination (PageRequest, optional): An object containing pagination information, such as page number and page size. Defaults to None.

        Returns:
                An object containing the surplus auctions data.
        """
        resp = await self.stub_auction.query_surplus_auctions(QuerySurplusAuctionsRequest(app_id=app_id, history=history, pagination=pagination))
        return resp




    async def get_surplus_biddings(self, bidder: str, app_id: int, history: bool, pagination: PageRequest = None) -> SurplusBiddings:

        """Retrieves surplus biddings for a specific bidder and application ID.

        Args:
                bidder (str): The identifier of the bidder.
                app_id (int): The identifier of the application.
                history (bool): A flag to include historical surplus biddings if set to True, otherwise only returns active surplus biddings.
                pagination (PageRequest, optional): An instance of PageRequest class for pagination. Defaults to None.



        Returns:
                An instance of the SurplusBiddings class, containing a list of surplus bidding objects and pagination information.
        """
        
        resp = await self.stub_auction.query_surplus_biddings(QuerySurplusBiddingsRequest(bidder=bidder, app_id=app_id, history=history, pagination=pagination))
        return resp
        



    async def get_debt_auction(self, app_id: int, auction_mapping_id: int, auction_id: int, history:bool) -> DebtAuction:

        """Retrieves the details of a specific debt auction using its associated identifiers.

        Args:
                app_id (int): The application ID associated with the debt auction.
                auction_mapping_id (int): The auction mapping ID used to identify the particular auction instance.
                auction_id (int): The unique ID of the debt auction.
                history (bool): A flag to include the auction's historical data if set to True.


        Returns:
                An instance of the DebtAuction class containing the auction details.
        """
        
        resp = await self.stub_auction.query_debt_auction(QueryDebtAuctionRequest(app_id=app_id, auction_mapping_id=auction_mapping_id, auction_id=auction_id, history=history))
        return resp
    



    async def get_debt_auctions(self, app_id: int, history: bool, pagination: PageRequest = None) -> QueryDebtAuctionsResponse:

        """Retrieves debt auction information based on the given parameters

        Args:
                app_id (int): The application ID for which debt auction information is to be retrieved.
                history (bool): If True, retrieves past debt auctions; otherwise, retrieves ongoing debt auctions.
                pagination (PageRequest, optional): An optional pagination object to limit the number of results and fetch results in a paginated manner.

        Returns:
                A response object containing the requested debt auction information based on the provided parameters.
        """
        
        resp = await self.stub_auction.query_debt_auctions(QueryDebtAuctionsRequest(app_id=app_id, history=history, pagination=pagination))
        return resp




    async def get_debt_biddings(self, bidder: str, app_id: int, history: bool, pagination: PageRequest = None) -> DebtBiddings:

        """Retrieves the debt biddings associated with a specific bidder and application ID

        Args:
                bidder (str): The identifier of the bidder whose debt biddings are to be fetched.
                app_id (int): The identifier of the application associated with the debt biddings.
                history (bool): If True, includes historical debt biddings; otherwise, returns only active debt biddings.
                pagination (PageRequest, optional): Pagination parameters for handling large result sets. Defaults to None.


        Returns:
                An object containing a list of debt biddings and pagination details, if applicable.

        """
        
        resp = await self.stub_auction.query_debt_biddings(QueryDebtBiddingsRequest(bidder=bidder, app_id=app_id, history=history, pagination=pagination))
        return resp




    async def get_dutch_auction(self, app_id: int, auction_mapping_id: int, auction_id: int, history:bool) -> DutchAuction:

        """Retrieves the information of a Dutch auction based on the provided parameters.

        Args:    
                app_id (int): The application ID associated with the auction.
                auction_mapping_id (int): The ID that maps to the specific auction instance.
                auction_id (int): The unique ID of the Dutch auction to be retrieved.
                history (bool): If True, includes the auction's history; otherwise, returns only the current state.

        Returns:
                An instance of the DutchAuction class, containing the requested auction information.
        """
        
        resp = await self.stub_auction.query_dutch_auction(QueryDutchAuctionRequest(app_id=app_id, auction_mapping_id=auction_mapping_id, auction_id=auction_id, history=history))
        return resp




    async def get_dutch_auctions(self, app_id: int, history: bool, pagination: PageRequest = None) -> QueryDutchAuctionsResponse:

        """Retrieves Dutch auction information from the server using the provided app_id, history flag, and optional pagination.

        Args:
                app_id (int): The application ID associated with the Dutch auctions.
                history (bool): If True, retrieves historical Dutch auctions; otherwise, retrieves active Dutch auctions.
                pagination (PageRequest, optional): An optional pagination object to fetch specific pages or limit the number of results.
        Returns:
                An object containing information about the queried Dutch auctions.
        """
        
        resp = await self.stub_auction.query_dutch_auctions(QueryDutchAuctionsRequest(app_id=app_id, history=history, pagination=pagination))
        return resp




    async def get_dutch_biddings(self, bidder: str, app_id: int, history: bool, pagination: PageRequest = None) -> DutchBiddings:

        """Retrieves Dutch auction biddings based on the given parameters.

        Args:
                bidder (str): The bidder's unique identifier.
                app_id (int): The application's unique identifier.
                history (bool): Flag to determine whether to retrieve historical biddings (True) or only active ones (False).
                pagination (PageRequest, optional): An optional pagination object to limit the number of results and specify the starting point for the query

        Returns:
                An object containing the Dutch auction biddings that match the provided criteria.
        """
        
        resp = await self.stub_auction.query_dutch_biddings(QueryDutchBiddingsRequest(bidder=bidder, app_id=app_id, history=history, pagination=pagination))
        return resp




    async def get_protocol_statistics(self, app_id: int, pagination: PageRequest = None) -> ProtocolStatistics:

        """Retrieves the protocol statistics for a given application ID, with optional pagination support.

        Args:
                app_id (int): The application ID for which the protocol statistics are to be fetched.
                pagination (PageRequest, optional): Pagination parameters to limit the number of results returned.

        Returns:
                An object containing the protocol statistics for the specified application ID.
        """
        
        resp = await self.stub_auction.query_protocol_statistics(QueryProtocolStatisticsRequest(app_id=app_id, pagination=pagination))
        return resp




    async def get_biddings_for_surplus_auction(self, app_id: int, auction_mapping_id: int, auction_id: int, history:bool, pagination: PageRequest = None) -> QueryBiddingsForSurplusAuctionResponse:

        """Retrieves the biddings for a surplus auction based on the provided parameter.

        Args:
                app_id (int): The application ID for which the surplus auction is being queried.
                auction_mapping_id (int): The auction mapping ID to identify the specific surplus auction.
                auction_id (int): The unique identifier for the surplus auction.
                history (bool): A boolean flag indicating whether to include historical data for the surplus auction.
                pagination (PageRequest, optional): An optional pagination object to control the number of results returned per page.

        Returns:
                A response object containing the queried biddings for the surplus auction, along with any additional metadata as per the request parameters.
        """
        
        resp = await self.stub_auction.query_biddings_for_surplus_auction(QueryBiddingsForSurplusAuctionRequest(app_id=app_id, auction_mapping_id=auction_mapping_id, auction_id=auction_id, history=history, pagination=pagination))
        return resp
    


   
    async def get_generic_auction_param(self, app_id: int) -> AuctionParams:

        """Retrieve the generic auction parameters for a specific app.

        Args:
                app_id (int): The unique identifier for the app for which the auction parameters are to be fetched.

        Returns:
                An object containing the generic auction parameters for the specified app.
        """
        
        resp = await self.stub_auction.query_generic_auction_params(QueryGenericAuctionParamRequest(app_id=app_id))
        return resp
    


   
    async def get_dutch_lend_auction(self, app_id: int, auction_mapping_id: int, auction_id: int, history:bool) -> QueryDutchLendAuctionResponse:

        """Retrieves information about a Dutch lend auction based on the provided parameters.


        Args:
                app_id (int): The application identifier.
                auction_mapping_id (int): The identifier for the auction mapping.
                auction_id (int): The identifier for the auction.
                history (bool): Whether to include auction history in the response.

        Returns:
                An object containing the queried Dutch lend auction information, including auction details and history if requested.
        """
        
        resp = await self.stub_auction.query_dutch_lend_auction(QueryDutchLendAuctionRequest(app_id=app_id, auction_mapping_id=auction_mapping_id, auction_id=auction_id, history=history))
        return resp
    


    
    async def get_dutch_lend_auctions(self, app_id: int, history: bool, pagination: PageRequest = None) -> QueryDutchLendAuctionsResponse:

        """Retrieves a list of Dutch lend auctions based on the given app_id, history flag, and optional pagination parameters.

        Args:
                app_id (int): The application ID for which to retrieve the Dutch lend auctions.
                history (bool): If True, includes past auctions in the response; if False, only returns ongoing auctions.
                pagination (PageRequest, optional): An object containing pagination parameters, such as limit and offset. Defaults to None.
        
        Returns:  
                An object containing the list of Dutch lend auctions matching the provided parameters.
    
        """
        
        resp = await self.stub_auction.query_dutch_lend_auctions(QueryDutchLendAuctionsRequest(app_id=app_id, history=history, pagination=pagination))
        return resp



    
    async def get_dutch_lend_biddings(self, bidder: str, app_id: int, history: bool, pagination: PageRequest = None) -> QueryDutchLendBiddingsResponse:

        """Fetches Dutch lend biddings for a specific bidder and app.

        Args:
                bidder (str): The identifier of the bidder.
                app_id (int): The identifier of the application.
                history (bool): A flag indicating whether to include historical biddings.
                pagination (PageRequest, optional): An object containing pagination information.

        Returns:
                A response object containing the list of Dutch lend biddings.

        """
        
        resp = await self.stub_auction.query_dutch_lend_biddings(QueryDutchLendBiddingsRequest(bidder=bidder, app_id=app_id, history=history, pagination=pagination))
        return resp




    async def get_filter_dutch_auctions(self, app_id: int, denom: List[str], history: bool, pagination: PageRequest = None) -> QueryFilterDutchAuctionsResponse:
        
        """Retrieve Dutch auction details based on given filters.


        Args:
                app_id (int): The application ID to filter Dutch auctions by.
                denom (List[str]): A list of denominations (currencies) to filter Dutch auctions by.
                history (bool): If True, include the history of Dutch auctions; if False, return only ongoing auctions.
                pagination (PageRequest, optional): Pagination options for the filtered results.


        Returns:
                An object containing the filtered Dutch auction details and pagination information.
        """
        
        resp = await self.stub_auction.query_filter_dutch_auctions(QueryFilterDutchAuctionsRequest(app_id=app_id, denom=denom, history=history, pagination=pagination))
        return resp
    



    
       