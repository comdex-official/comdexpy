===========
VAULT
===========


Query
----------


1.get_vault_info
*****************

        "Queries information about a vault with the specified ID."

        Args: 
             id: An integer representing the ID of the vault to be queried.

        Returns: 
             QueryVaultResponse: An object representing the response from the query, which contains information about the requested vault.
        
--------


2.get_vault_info_by_vault_id
******************************
        
        "Queries information about a vault using a given vault ID."

        Args:
             id (int): The ID of the vault for which information needs to be queried.

        Returns:
             An object that contains the response from the server, including the requested vault information.
        
-------


3.get_vault_info_of_owner_by_app_id
*************************************
        
        "Queries the vault information of a specific owner for a given app ID, with an optional pagination parameter."

        Args:
             app_id (int): The ID of the app to query the vault information for.
             
             owner (str): The owner of the vault information to retrieve.
             
             pagination (PageRequest, optional): A PageRequest object specifying the pagination information, such as the page size and offset. Defaults to None.

        
        Returns:
             A response object that contains the requested vault information for the given app ID and owner, as well as the pagination information, such as the total number of results and the next page token.
        
        

--------


4.get_all_vaults
*****************

        "Retrieve a list of all vaults."

        Args:
             pagination (PageRequest, optional): pagination parameters for the query.

        Returns:
             A response object containing a list of Vault objects.
        
         
--------


5.get_all_vaults_by_app
************************

        "Queries all the vaults associated with a given app ID."

        Args:
             app_id (int): The ID of the application for which the vaults are being queried.

        Returns:
              The response object containing the list of vaults associated with the given app ID.
        
        
---------



6.get_all_vaults_by_app_and_extended_pair
*******************************************
        
        "Queries all vaults associated with a particular app and extended pair."

        Args:
             app_id (int): The ID of the app to which the vaults are associated.
             
             extended_pair_id (int): The ID of the extended pair to which the vaults are associated.
             
             pagination (PageRequest, optional): An optional pagination parameter to limit the number of results returned.


        Returns:
             A response object containing a list of vaults associated with the given app and extended pair, along with pagination information.

        
--------


7.get_vault_id_of_owner_by_extended_pair_and_app
**************************************************
        
        "Queries the vault ID of a particular owner based on the provided application ID, owner name, and extended pair ID." 

        Args:
             app_id (int): The application ID for which to query the vault ID.
             
             owner (str): The name of the owner for which to query the vault ID.
             
             extended_pair_id (int): The ID of the extended pair for which to query the vault ID.
             
             pagination (PageRequest, optional): An optional parameter used for pagination.


        Returns:
             A response object containing the vault ID of the owner and any pagination information.
    
        
-------



8.get_vault_ids_by_app_in_all_extended_pairs
*********************************************
        
        "Retrieves the IDs of all vaults associated with a given app ID in all extended pairs." 

        Args:
             app_id: an integer representing the ID of the app for which vault IDs need to be retrieved.
             
             pagination: an optional PageRequest object representing the pagination information.


        Returns:
             An Object containing the list of vault IDs and the pagination information.
        
        
---------



9.get_all_vault_ids_by_an_owner
*********************************
        
        "Queries all vault IDs owned by a specific owner."

        Args:
             owner: An integer representing the ID of the owner whose vault IDs are being queried.

        Returns:
             An object that contains the response of the query, which includes a list of all vault IDs owned by the specified owner.
        
        
---------



10.get_token_minted_by_app_and_extended_pair
*********************************************
        
        "Retrieve a list of tokens minted by a given app and extended pair."

        Args:
             app_id (int): The ID of the app.
             
             extended_pair_id (int): The ID of the extended pair.
             
             pagination (PageRequest, optional): An optional pagination request to limit the number of results. Defaults to None.


        Returns:
             A response containing a list of tokens minted by the given app and extended pair.


--------


11.get_token_minted_asset_wise_by_app
**************************************
        
        "Retrieves information about tokens minted asset-wise by a particular application (identified by app_id) from a remote server."

        Args:
             app_id (int): An integer value representing the ID of the application for which the token minting data is to be fetched.
             
             pagination (PageRequest): An optional object of PageRequest class representing pagination details (e.g., page number and page size) for the query. Default is None.


        Returns:
             Returns the list of token minting data, total count of records, and pagination details (if pagination is requested).
        
     
----------

   
12.get_vault_count_by_app
**************************

        "Queries the count of vaults for a specific application."

        Args:
             app_id (int): The ID of the application for which the count of vaults is to be queried.

        Returns:
             An object that contains the response from the gRPC server after querying the count of vaults for the specified application ID.
        
        
--------    

   
13.get_vault_count_by_app_and_extended_pair
*********************************************

        "Queries the count of vaults by application and extended pair ID."


        Args:
             app_id (int): ID of the application to query for vault count.
             
             extended_pair_id (int): ID of the extended pair to query for vault count.
             
             pagination (PageRequest): (Optional) Page request object for pagination of results.


        Returns:
             An object containing the count of vaults that match the given application and extended pair ID.
       
    
-------

    
14.get_total_value_locked_by_app_and_extended_pair
****************************************************
        
        "Queries the total value locked by an app and an extended pair."

        Args:
             app_id (int): An integer representing the ID of the app.
             
             extended_pair_id (int): An integer representing the ID of the extended pair.
             
             pagination (PageRequest, optional): An optional PageRequest object representing the pagination settings for the query.


        Returns:  
             A response object that contains the total value locked by the specified app and extended pair.
    
---------

    
15.get_extended_pair_ids_by_app
*********************************
        
        "Retrieves extended pair IDs by application ID."

        Args:
             app_id: an integer representing the ID of the application to retrieve extended pair IDs for.
             
             pagination: (optional) a PageRequest object containing pagination parameters such as the number of results to return and the page token to use for fetching subsequent pages.


        Returns:
              An object containing the extended pair IDs associated with the specified application ID. 
        
    
--------


16.get_stable_vault_by_vault_id
**********************************
        
        "Queries a stable vault by its ID and returns the response."


        Args:
             stable_vault_id: An integer representing the ID of the stable vault to be queried.

        Returns:
             An object representing the response received from the query to the stable vault with the given ID.
        
        
-----------    


17.get_stable_vault_by_app
***************************

        "Queries a stable vault by the given app ID, with an optional pagination parameter."

        Args:
             app_id (int): The ID of the app for which the stable vault is being queried.
             
             pagination (PageRequest, optional): An optional pagination object specifying the page size and number of items to skip. If not provided, the default page size will be used.  


        Returns:
             An object containing the result of the query, including a list of StableVault objects and a token for fetching the next page of results (if applicable).
        
    
----------


18.get_stable_vault_by_app_and_extended_pair
**********************************************
        
        "Retrieves a stable vault given an app ID and an extended pair ID."

        Args:
             app_id (int): The ID of the app associated with the stable vault to retrieve.
             
             extended_pair_id (int): The ID of the extended pair associated with the stable vault to retrieve.


        Returns:
             The response containing the stable vault associated with the given app and extended pair.

    
---------


19.get_extended_pair_vault_mapping_by_app_and_extended_pair
*************************************************************

        
        "Queries the extended pair vault mapping by app ID and extended pair ID and returns the response."

        Args:
             app_id (int): The ID of the application to query for the extended pair mapping.
             
             extended_pair_id (int): The ID of the extended pair to query for.


        Returns:
             The response object that contains the extended pair vault mapping information.

    
----------


20.get_extended_pair_vault_mapping_by_app
*******************************************

        "Retrieves extended pair-vault mapping information by an application ID."

        Args:
             app_id (int): The ID of the application for which the extended pair-vault mapping information is to be retrieved.
             
             pagination (PageRequest, optional): The pagination information to be used for the query. Defaults to None.


        Returns:
             A response object containing the extended pair-vault mapping information for the specified application ID.
        
---------    



21.get_tvl_by_app_of_all_extended_pairs
*****************************************
        
        "Queries the Total Value Locked (TVL) for all extended pairs of a given application ID."

        Args:
             app_id (int): The ID of the application to query the TVL for all its extended pairs.
             
             pagination (PageRequest): An optional parameter that represents the pagination settings for the query results.


        Returns:
             A response object containing the queried TVL for all extended pairs of the given application ID.
        

---------    



22.get_tvl_by_app
******************

        "Retrieves the Total Value Locked (TVL) for a given app ID using the Vault service."

        Args:
             app_id (int): The ID of the app for which TVL is being queried.

        Returns:
             The response object containing TVL data for the requested app.
        

-------------


    
23.get_user_my_position_by_app
********************************
        
        "Gets the user's position by a specified app ID and owner."

        Args:
             app_id (int): The ID of the app to query for the user's position.
             
             owner (str): The name of the owner of the app.


        Returns:
             An object representing the user's position for the specified app.

    
----------

    
24.get_pairs_locked_and_minted_statistic_by_app
*************************************************
        
        "Retrieves statistics on pairs that have been locked and minted by a specific app."

        Args:
             app_id (int): the ID of the app for which statistics are being retrieved.
             
             pagination (PageRequest): an optional object that specifies the pagination parameters for the query. If not provided, all results will be returned.    
        

        Returns:
             An object containing the statistics for pairs that have been locked and minted by the specified app

    
------------


25.get_all_stable_mint_vault_rewards
**************************************
        
        "Retrieves all the stablecoin mint vault rewards."

        Args:
             pagination (optional): an instance of the PageRequest class that contains pagination information such as page number and page size.

        Returns:
             An instance of the QueryAllStableMintVaultRewardsResponse class containing all the stablecoin mint vault rewards.
----------


Messages
---------------

1.MsgCreateRequest
*******************
         Users can create a vault for an app and extended_pair_vault id with an initial amount_in (collateral) and amount_out(debt).

                 MsgCreateRequest {
                     string from  
                     
                     uint64 app_id   
                     
                     uint64 extended_pair_vault_id 
                     
                     string amount_in 
                     
                     string amount_out 
                 
                 }

------------

2.MsgDepositRequest
*********************
         
         Vault owners can deposit extra collateral which inturn increases vault collateralization ratio.

                 MsgDepositRequest {
                     string from 
                     
                     uint64 app_id  
                     
                     uint64 extended_pair_vault_id 
                     
                     uint64 user_vault_id 
                     
                     string amount 
                 
                 }

------------

3.MsgWithdrawRequest
*********************
         
         Vault owners can withdraw their collateral from the vault.

                 MsgWithdrawRequest {
                     string from 
                     
                     uint64 app_id  
                     
                     uint64 extended_pair_vault_id 
                     
                     uint64 user_vault_id  
                     
                     string amount 
                 
                 } 

-------------


4.MsgDrawRequest
*****************

         Get more borrowed asset from the vault

                 MsgDrawRequest {
                     string from 
                     
                     uint64 app_id   
                     
                     uint64 extended_pair_vault_id 
                     
                     uint64 user_vault_id  
                     
                     string amount 
                 
                 }

------------

5.MsgRepayRequest
*******************

         Vault owners can repay their debt which will increase the collateralization ratio

                 MsgRepayRequest {
                     string from 
                     
                     uint64 app_id  
                     
                     uint64 extended_pair_vault_id 
                     
                     uint64 user_vault_id  
                     
                     string amount 
                 
                 }

------------

6.MsgCloseRequest
******************

         Vault owner can close the vault by paying the entire debt

                 MsgCloseRequest {
                     string from 
                     
                     uint64 app_id   
                     
                     uint64 extended_pair_vault_id 
                     
                     uint64 user_vault_id  
                 
                 }

--------------

7.MsgCreateStableMintRequest
*****************************

         Create Stable Mint Vault by depositing a stable token and then minting other stable token

                 MsgCreateStableMintRequest {
                     string from  
                     
                     uint64 app_id  
                     
                     uint64 extended_pair_vault_id 
                     
                     string amount 
                 
                 }

--------------

8.MsgDepositStableMintRequest
******************************
         Users can deposit the collateral to mint the borrowed asset at 1:1 ratio.

                 MsgDepositStableMintRequest {
                     string from  
                     
                     uint64 app_id   
                     
                     uint64 extended_pair_vault_id 
                     
                     string amount 
                     
                     uint64 stable_vault_id  
                 
                 }

-----------

9.MsgWithdrawStableMintRequest
*******************************

         Users can withdraw their collateral by burning the borrowed asset at 1:1 ratio.

                 MsgWithdrawStableMintRequest {
                     string from  
                     
                     uint64 app_id  
                     
                     uint64 extended_pair_vault_id
                     
                     string amount 
                     
                     uint64 stable_vault_id  
                 
                 }






