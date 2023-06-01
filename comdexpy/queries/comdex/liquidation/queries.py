from grpclib.client import Channel

from comdexpy.proto.cosmos.base.query.v1beta1 import PageRequest

from comdexpy.proto.comdex.liquidation.v1beta1 import (
    QueryLockedVaultRequest,
    LockedVault,
    QueryLockedVaultsRequest,
    QueryLockedVaultsResponse,
    QueryLiquidationParamsRequest,
    Params,
    QueryLockedVaultsHistoryRequest,
    QueryLockedVaultsHistoryResponse,
    QueryUserLockedVaultsRequest,
    QueryUserLockedVaultsResponse,
    QueryUserLockedVaultsHistoryRequest,
    QueryUserLockedVaultsHistoryResponse,
    QueryLockedVaultsPairRequest,
    QueryLockedVaultsPairResponse,
    QueryAppIdsRequest,
    QueryAppIdsResponse

)
from comdexpy.proto.comdex.liquidation.v1beta1 import QueryStub as LiquidationQueryStub


class Query():
    def __init__(self, channel: Channel) -> None:
        self.stub_liquidation = LiquidationQueryStub(channel)

    async def get_locked_vault(self, app_id: int, id: int) -> LockedVault:

        """Retrieves the locked vault information for a given app ID and vault ID.

        Args: 
                app_id (int): The application ID to filter the locked vault.
                id (int): The unique identifier of the locked vault to be retrieved.

        Returns: 
                An instance of the LockedVault class containing the locked vault information.

        """
        resp = await self.stub_liquidation.query_locked_vault(QueryLockedVaultRequest(app_id=app_id, id=id))
        return resp



    async def get_locked_vaults(self, pagination: PageRequest = None) -> QueryLockedVaultsResponse:

        """Retrieves locked vaults information with optional pagination support.

        Args:
                An object containing pagination information such as start index and page size. Defaults to None.

        Returns:
                An object containing a list of locked vaults and their details, along with pagination information if applicable.
        """
        resp = await self.stub_liquidation.query_locked_vaults(QueryLockedVaultsRequest(pagination=pagination))
        return resp




    async def get_liquidation_params(self) -> Params:

        """This asynchronous function retrieves the liquidation parameters.

        Args:
                None

        Returns:
                An instance of the Params class containing the liquidation parameters.

        """
        
        resp = await self.stub_liquidation.query_liquidation_params(QueryLiquidationParamsRequest())
        return resp




    async def get_locked_vaults_history(self, pagination: PageRequest = None) -> QueryLockedVaultsHistoryResponse:

        """Retrieves the history of locked vaults with support for pagination.

        Args:
                An object containing pagination-related parameters, such as page number and items per page. Default is None.

        Returns:
                An object containing the locked vaults history.
        """
        
        resp = await self.stub_liquidation.query_locked_vaults_history(QueryLockedVaultsHistoryRequest(pagination=pagination))
        return resp
    



    async def get_user_locked_vaults(self, user_address: str, pagination: PageRequest = None) -> QueryUserLockedVaultsResponse:

        """Retrieves the locked vaults associated with a given user address, and supports pagination to limit the number of results returned.

        Args:
                user_address (str): The user's blockchain address for which locked vaults should be fetched.
                pagination (PageRequest, optional): An optional pagination object to limit the number of results returned. Defaults to None.

        Returns:
                An object containing the list of locked vaults for the specified user address, along with any relevant pagination details.
        """
        
        resp = await self.stub_liquidation.query_user_locked_vaults(QueryUserLockedVaultsRequest(user_address=user_address, pagination=pagination))
        return resp




    async def get_user_locked_vaults_history(self, user_address: str, pagination: PageRequest = None) -> QueryUserLockedVaultsHistoryResponse:

        """Retrieves the history of locked vaults for a specific user address, with optional pagination support.

        Args:
                user_address (str): The user's Ethereum address to query the locked vaults history for.
                pagination (PageRequest, optional): An optional pagination object to control the number of records returned and the starting point of the results.


        Returns:
                A response object containing the user's locked vaults history with information such as vault IDs, locked amounts, and timestamps.

        """
        
        resp = await self.stub_liquidation.query_user_locked_vaults_history(QueryUserLockedVaultsHistoryRequest(user_address=user_address, pagination=pagination))
        return resp
    




    async def get_locked_vaults_pair(self, pair_id: int, pagination: PageRequest = None) -> QueryLockedVaultsPairResponse:

        """Retrieves the locked vaults information for a given pair ID and returns the result as a QueryLockedVaultsPairResponse object.

        Args:
                pair_id (int): The ID of the pair for which to query locked vaults.
                pagination (PageRequest, optional): An optional pagination object to control the number of results returned.


        Returns:
                An object containing the locked vaults information for the given pair ID, along with any associated pagination details.
        """
        
        resp = await self.stub_liquidation.query_locked_vaults_pair(QueryLockedVaultsPairRequest(pair_id=pair_id, pagination=pagination))
        return resp
    




    async def get_app_ids(self) -> QueryAppIdsResponse:
        
        """Queries the application IDs from the liquidation system and returns a QueryAppIdsResponse containing the list of IDs.

        Args:
                None


        Returns:
                An object containing the list of application IDs.
        """
        
        resp = await self.stub_liquidation.query_app_ids(QueryAppIdsRequest())
        return resp






