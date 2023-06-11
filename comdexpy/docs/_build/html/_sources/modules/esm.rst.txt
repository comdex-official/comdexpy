===========
ESM
===========



Query
-----------

1.get_params
*************
        
        "Get the parameters for a specific entity."

        Args: 
             The instance of the class.

        Returns: 
             The parameters for the entity.
        

-----

2.get_esm_trigger_params
*************************

        "Get the trigger parameters for a specific ESM trigger."


        Args:
             id (int): The ID of the ESM trigger to retrieve the parameters for.

        Returns:
             EsmTriggerParams: The trigger parameters for the specified ESM trigger.
        

-----


3.get_esm_status
******************
        
        "Get the status of an ESM with a given ID."


        Args:
             id (int): The ID of the ESM to query.

        Returns:
             EsmStatus: The status of the ESM.

        
-----




4.get_current_deposit_stats
****************************


        "Get the current deposit statistics for a given ID."


        Args:
             id (int): The ID of the entity to retrieve deposit statistics for.

        Returns:
             CurrentDepositStats: The current deposit statistics for the specified ID.
       
        
-----    



5.get_users_deposit_mapping
****************************
        
        """Get the deposit mapping for the specified user.


        Args:
             id (int): The ID of the user.
             
             depositor (str): The name of the depositor.

        Returns:
              UsersDepositMapping: The deposit mapping information for the specified user.
        
        
-----



6.get_data_after_cool_off
***************************
        
        "Get data after cool off period for a given id."


        Args:
             id (int): The id of the data to retrieve.


        Returns:
             DataAfterCoolOff: The data after the cool off period for the given id.

        
        
-----



    
7.get_snapshot_price
**********************


        "Get the snapshot price for a given ID and asset ID."

        
        Args:
             id (int): The ID of the snapshot.
             
             asset_id (int): The ID of the asset.


        Returns:
             QuerySnapshotPriceResponse: The response object containing the snapshot price information.



8.get_asset_data_after_cool_off
*********************************

        "Retrieve asset data after cool-off period."


        Args:
             app_id (int): The ID of the application to retrieve data for.


        Returns:
             AssetToAmount: A named tuple containing the asset data.

        
    

