from grpclib.client import Channel


from comdexpy.proto.cosmos.base.query.v1beta1 import PageRequest
from comdexpy.proto.comdex.asset.v1beta1 import (
    QueryAssetsRequest,
    QueryAssetsResponse,
    QueryAssetRequest,
    Asset,
    QueryAssetPairsRequest,
    QueryAssetPairsResponse,
    QueryAssetPairRequest,
    PairInfo,
    QueryAppRequest,
    AppData,
    QueryGovTokenByAppRequest,
    QueryGovTokenByAppResponse,
    QueryAppsRequest,
    QueryAppsResponse,
    QueryExtendedPairVaultRequest,
    ExtendedPairVault,
    QueryAllExtendedPairVaultsRequest,
    QueryAllExtendedPairVaultsResponse,
    QueryAllExtendedPairVaultsByAppRequest,
    QueryAllExtendedPairVaultsByAppResponse,
    QueryAllExtendedPairStableVaultsIDByAppRequest,
    QueryAllExtendedPairStableVaultsIDByAppResponse,
    QueryAllExtendedPairStableVaultsByAppRequest,
    QueryAllExtendedPairStableVaultsByAppResponse,
    QueryExtendedPairVaultsByAppWithoutStableRequest,
    QueryExtendedPairVaultsByAppWithoutStableResponse

)
from comdexpy.proto.comdex.asset.v1beta1 import QueryStub as AssetQueryStub


class Query():
    def __init__(self, channel: Channel) -> None:
        self.stub_asset = AssetQueryStub(channel)


    async def get_assets(self, pagination: PageRequest = None) -> QueryAssetsResponse:

        """Retrieve a list of assets from the server with optional pagination.

        Args: 
                pagination (PageRequest, optional): A pagination object specifying the desired page and page size for the response. Defaults to None, which means no pagination

        Returns: 
                A response object containing a list of assets and any associated metadata, such as total number of assets and pagination info.
        """

        resp = await self.stub_asset.query_assets(QueryAssetsRequest(pagination=pagination))
        return resp




    async def get_asset(self, id: int) -> Asset:

        """Retrieves the asset information for a given asset ID asynchronously.


        Args:
                id (int): The unique identifier of the asset to retrieve.

        Returns:
                An instance of the 'Asset' class containing the asset information.
        """
        resp = await self.stub_asset.query_asset(QueryAssetRequest(id=id))
        return resp




    async def get_asset_pairs(self, pagination: PageRequest = None) -> QueryAssetPairsResponse:

        """Fetches and returns the asset pairs from the server using the provided pagination request.

        Args:
                pagination (PageRequest, optional): An object containing pagination parameters such as limit and offset for the asset pairs query. Defaults to None.


        Returns:
                An object containing the requested asset pairs and any related metadata.

        """
        
        resp = await self.stub_asset.query_asset_pairs(QueryAssetPairsRequest(pagination=pagination))
        return resp
        



    async def get_asset_pair(self, id: int) -> PairInfo:

        """Retrieves asset pair information for a given ID.

        Args:
                id (int): The unique identifier for the asset pair.

        Returns:
                An object containing information about the asset pair corresponding to the provided ID.
        """
        
        resp = await self.stub_asset.query_asset_pair(QueryAssetPairRequest(id=id))
        return resp
    



    async def get_app(self, id: int) -> AppData:

        """Retrieve application data based on the given ID.

        Args:
                id (int): The unique identifier for the application to retrieve.

        Returns:
                An AppData object containing the application's information.
        """
        
        resp = await self.stub_asset.query_app(QueryAppRequest(id=id))
        return resp




    async def get_gov_token_by_app(self, app_id: int) -> QueryGovTokenByAppResponse:

        """Retrieves the government token associated with a specific app by querying the asset.

        Args:
                app_id (int): The unique identifier of the app for which the government token is to be retrieved.

        Returns:
                An object containing the government token details for the specified app.

        """
        
        resp = await self.stub_asset.query_gov_token_by_app(QueryGovTokenByAppRequest(app_id=app_id))
        return resp




    async def get_apps(self, pagination: PageRequest = None) -> QueryAppsResponse:

        """Queries a list of applications from the server using the provided pagination parameters.

        Args:    
                pagination (PageRequest, optional): An object containing pagination parameters such as the page number and the number of items per page.
       
        Returns:
                An object containing the list of applications and pagination information.
        """
        
        resp = await self.stub_asset.query_apps(QueryAppsRequest(pagination=pagination))
        return resp




    async def get_extended_pair_vault(self, id: int) -> ExtendedPairVault:

        """Retrieves the details of an ExtendedPairVault with the given ID.

        Args:
                id (int): The unique identifier for the ExtendedPairVault to be fetched.

        Returns:
                An object containing the details of the requested ExtendedPairVault.
        """
        
        resp = await self.stub_asset.query_extended_pair_vault(QueryExtendedPairVaultRequest(id=id))
        return resp




    async def get_all_extended_pair_vaults(self, pagination: PageRequest = None) -> QueryAllExtendedPairVaultsResponse:

        """Retrieve all extended pair vaults from the data source.

        Args:
                pagination (PageRequest, optional): An instance of PageRequest containing pagination parameters such as offset and limit. Defaults to None.

        Returns:
                An instance of QueryAllExtendedPairVaultsResponse containing a list of extended pair vaults and pagination details.
        """
        
        resp = await self.stub_asset.query_all_extended_pair_vaults(QueryAllExtendedPairVaultsRequest(pagination=pagination))
        return resp




    async def get_all_extended_pair_vaults_by_app(self, app_id: int, pagination: PageRequest = None) -> QueryAllExtendedPairVaultsByAppResponse:

        """Retrieves all extended pair vaults associated with a given application ID.

        Args:
                app_id (int): The unique identifier for the application whose extended pair vaults are to be fetched.
                pagination (PageRequest, optional): An optional parameter to specify pagination details for the results. Defaults to None.

        Returns:
                A response object containing the extended pair vaults associated with the specified application ID, along with any relevant pagination information.
        """
        
        resp = await self.stub_asset.query_all_extended_pair_vaults_by_app(QueryAllExtendedPairVaultsByAppRequest(app_id=app_id, pagination=pagination))
        return resp



   
    async def get_all_extended_pair_stable_vaults_id_by_app(self, app_id: int, pagination: PageRequest = None) -> QueryAllExtendedPairStableVaultsIDByAppResponse:

        """Retrieves all the extended pair stable vault IDs associated with a given app_id. It supports pagination to enable efficient retrieval of large datasets.


        Args:
                app_id (int): The ID of the application for which the extended pair stable vault IDs are to be retrieved.
                pagination (PageRequest, optional): A pagination object containing information about the desired page size and the starting point for the results. Defaults to None.

        Returns:
                 An object containing the response with a list of extended pair stable vault IDs and the pagination information.
        """
        
        resp = await self.stub_asset.query_all_extended_pair_stable_vaults_id_by_app(QueryAllExtendedPairStableVaultsIDByAppRequest(app_id=app_id, pagination=pagination))
        return resp
    


   
    async def get_all_extended_pair_stable_vaults_by_app(self, app_id: int, pagination: PageRequest = None) -> QueryAllExtendedPairStableVaultsByAppResponse:

        """Retrieves all extended pair stable vaults associated with the specified app ID.


        Args:
                app_id (int): The unique identifier of the application for which to retrieve the extended pair stable vaults.
                pagination (PageRequest, optional): An optional pagination object for limiting the results. Defaults to None.

        Returns:
                A response object containing a list of extended pair stable vaults associated with the given app ID and pagination details.
        """
        
        resp = await self.stub_asset.query_all_extended_pair_stable_vaults_by_app(QueryAllExtendedPairStableVaultsByAppRequest(app_id=app_id, pagination=pagination))
        return resp
    


    
    async def get_extended_pair_vaults_by_app_without_stable(self, app_id: int, pagination: PageRequest = None) -> QueryExtendedPairVaultsByAppWithoutStableResponse:

        """Retrieves extended pair vaults associated with a given app_id, excluding stable vaults. It also supports pagination for the results.

        Args:
                app_id (int): The unique identifier of the application for which the extended pair vaults are to be fetched.
                pagination (PageRequest, optional): An optional pagination object to navigate through the results. Defaults to None.
        
        Returns:  
                An object containing the extended pair vaults information and any relevant pagination details.
    
        """
        
        resp = await self.stub_asset.query_extended_pair_vaults_by_app_without_stable(QueryExtendedPairVaultsByAppWithoutStableRequest(app_id=app_id, pagination=pagination))
        return resp

       