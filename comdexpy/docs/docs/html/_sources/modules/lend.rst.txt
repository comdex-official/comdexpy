===========
LEND
===========


Query
--------

1.get_params
**************

        "Gets params of lend module."

         Args: None

         Returns: Lend Module's global Parameters
        
------

2.get_lend
*************

        "Retrieves a LendAsset object associated with a given ID."

        Args:
              id (int): The unique identifier of the LendAsset to be retrieved.


        Returns:
              The LendAsset object corresponding to the specified ID.
        

------

3.get_lends
***************

        "Retrieves a list of lends from the server, using the provided pagination settings if available."

        Args:
              pagination (PageRequest, optional): An instance of the PageRequest class, containing pagination settings such as the current page number and the number of items per page. Defaults to None.
        
        Returns:
              An instance of the QueryLendsResponse class, containing a list of lends and pagination information.
        
        
------

4.get_all_lend_by_owner
************************

        "Retrieves all lend records associated with a specific owner, and returns the results with optional pagination support."

        Args:
             owner (str): The unique identifier of the owner whose lend records are to be fetched.
             
             pagination (PageRequest, optional): An optional pagination object to retrieve results in chunks, if desired. Defaults to None.


        Returns:
             A response object containing a list of lend records associated with the specified owner and the pagination details, if applicable.
        
        
------

5.get_all_lend_by_owner_and_pool
*********************************

        "Retrieves all the lending information associated with a specific owner and pool using the provided owner and pool ID."

        Args:
             owner (str): The owner's unique identifier (e.g. wallet address or user ID) for whom the lending information is to be fetched.
             
             pool_id (int): The unique identifier of the pool for which the lending information is to be fetched.
             
             pagination (PageRequest, optional): An optional pagination object to control the number of records retrieved and the starting point of the records. Defaults to None.
        

        Returns:
             A response object containing the lending information for the specified owner and pool, including any pagination details if provided.
        
------       


6.get_pairs
************

        "Fetches the trading pairs from the server using pagination and returns the response as a QueryPairsResponse object."

        Args:
             pagination (PageRequest, optional): An instance of the PageRequest object containing pagination information such as the start key and limit. Default is None, which means no pagination is applied.
        
        Returns:
             An instance of the QueryPairsResponse object containing a list of trading pairs and pagination details, if applicable.
        
        
------

7.get_pair   
************

        "Retrieve an ExtendedPair object associated with the given ID."

        Args:
             id (int): The unique identifier of the desired pair.


        Returns:
             An object containing information about the pair associated with the given ID.
        
        
------


8.get_asset_rates_params  
*************************

        "Retrieves the asset rates parameters from the lending platform, allowing for optional pagination."

        Args:
             pagination (PageRequest, optional): An object containing pagination information, such as limit and offset, to control the number of results returned. Default is None, which retrieves all available data.
        
        Returns:
             A response object containing the asset rates parameters and any associated pagination metadata.
        
    
------


9.get_asset_rates_param 
************************


        "Retrieves the asset rates parameters for a specified asset ID."

        Args:
             id (int): The unique identifier of the asset for which the rates parameters are to be fetched.

        Returns:
             An instance of the AssetRatesParams class containing the rates parameters for the specified asset.
        
------        


10.get_pools  
**************

        "Queries the list of available lending pools and returns the results as a QueryPoolsResponse object."

        Args:
             pagination (PageRequest, optional): An object specifying the pagination options for the results.Defaults to None, which returns all results.

        Returns:
             An object containing the list of available lending pools and any relevant metadata
        
        
------


11.get_pool  
*************

        "Retrieves the pool information for a given pool ID." 

        Args:
             id (int): The ID of the pool for which the information is to be retrieved.

        Returns:
             An instance of the Pool class containing the retrieved pool information.

------

   
12.get_asset_to_pair_mappings  
*******************************


        "Retrieves the asset-to-pair mappings from the underlying service. It takes an optional pagination argument and returns the mappings as a response object."

        Args:
             pagination (PageRequest, optional): An optional pagination object containing the pagination details such as the limit and offset for the requested data.

        Returns:
             A response object containing the asset-to-pair mappings along with any associated metadata.
        
        
------

   
13.get_asset_to_pair_mapping   
*****************************

        """Retrieves the mapping of a specific asset to a trading pair in a pool.


        Args:
             asset_id (int): The unique identifier of the asset.
             
             pool_id (int): The unique identifier of the liquidity pool.
       
        Returns:
             An instance of the AssetToPairMapping data structure containing the mapping information for the given asset and pool.
        
    
------

    
14.get_borrows 
***************


        "Retrieves a list of borrows from the lending service using the provided pagination information."


        Args:
             pagination (PageRequest, optional): An object containing pagination information (e.g., limit, offset) for querying the borrows. Default is None.

        Returns:  
             An object containing the list of borrows and additional pagination details
    

------
  
15.get_borrow  
***************

        "Fetch the borrow asset information using the given ID and return the corresponding BorrowAsset object."

        Args:
             id (int): The unique identifier of the borrow asset to be fetched.

        Returns:
             An instance of the BorrowAsset class containing the fetched borrow asset information.
    
------


16.get_all_borrow_by_owner
***************************

        "Retrieves all borrow records associated with a given owner, with optional pagination support."


        Args:
             owner (str): The owner for which to retrieve the borrow records.
             
             pagination (PageRequest, optional): A pagination object containing information for paginating the results. Defaults to None.
        
        
        Returns:
             A response object containing a list of borrow records associated with the specified owner and pagination information, if applicable.
        
------


17.get_all_borrow_by_owner_and_pool
************************************

        "Queries the lending service for all borrow records associated with a given owner and pool.The results can be paginated by providing an optional pagination parameter."
        
        Args:
             owner (str): The owner's address in string format.
             
             pool_id (int): The unique identifier of the pool.
             
             pagination (PageRequest, optional): A pagination object specifying the desired number of results per page and the key for the starting point. Defaults to None.

        
        Returns:
             A response object containing a list of borrow records and pagination information.

------


18.get_pool_asset_lb_mapping
******************************
        
        "Get the mapping of pool assets to liquidity balances for a specific asset and pool."

        Args:
             asset_id (int): The unique identifier for the asset in the pool.
             
             pool_id (int): The unique identifier for the pool.


        Returns:
             An object containing the mapping of assets to liquidity balances for the specified asset and pool.
    

------

19.get_reserve_buyback_asset_data
***********************************
        
        "Retrieves the reserve buyback asset data for a given asset ID."

        Args:
             asset_id (int): The unique identifier of the asset for which the reserve buyback asset data is to be retrieved.
        
        Returns:
             An object containing the reserve buyback asset data for the specified asset ID.
        
------

20.get_auction_param
*********************
        
        "Retrieves the auction parameters for a given application ID."

        Args:
             app_id (int): The application ID for which to fetch the auction parameters.

        Returns:
             An instance of the AuctionParams class, containing the fetched auction parameters for the given application ID.
        
------

21.get_module_balance
***********************
        
        "Retrieves the balance of a specific module in a lending pool by querying the module balance using the provided 'pool_id'."

        Args:
             pool_id (int): The unique identifier of the lending pool for which the module balance is to be retrieved.

        Returns:
             An instance of the ModuleBalance class representing the balance information for the specified module in the lending pool.
        

------
 
22.get_fund_mod_bal
********************
        
        "Get the current modified balance of the fund."

        Args:
             None

        Returns:
             The modified balance of the fund as a ModBal object.
        
------


23.get_fund_reserve_bal
*************************

        "Retrieves the balance information of the fund reserve."

        Args:
             None

        Returns:
             An instance of the ReserveBal class containing the balance details of the fund reserve.
        
------
    

24.get_all_reserve_stats
*************************

        "Fetches and returns all reserve statistics for the given asset ID."

        Args:
             asset_id (int): The unique identifier of the asset for which to retrieve reserve statistics.

        Returns:
             An object containing all reserve statistics related to the specified asset.
        
  
------

25.get_fund_mod_bal_by_asset_pool
***********************************

        "Retrieves the modified balance of a specific asset in a given asset pool from the lending platform."

        
        Args:
             asset_id (int): The unique identifier of the asset to query.
             
             pool_id (int): The unique identifier of the asset pool to query.


        Returns:
             A response object containing the modified balance of the specified asset in the given asset pool.
           
------


26.get_lend_interest
**********************

        "Retrieves the current lending interest rate from the pool."

        Args:
             None
       
        Returns:
             An instance of the PoolInterest class containing the lending interest rate information from the pool.
        
     
------


27.get_borrow_interest
************************
        
        "Retrieves the current borrow interest rate for a lending pool."

        Args:
             None

        Returns:
             An instance of the 'PoolInterestB' class containing the current borrow interest rate information.
        

------

Messages
---------

1.MsgLend:
************

         -An user can come and create their own Lend Position using MsgLend.
         
         -The user provides the assetID, poolID and the amount. After the tx is complete a new lend position is created for that user with an unique lendID.
         
         -A cToken representative of the IBC-Asset is minted and then transferred to the user which denotes the borrowing power/ Available to borrow capacity.
         
         -Rewards start to get accumulated on the lent Amount if the lendingApr is above 0 and sent to the user in cToken. Available borrowing is also increased accordingly.

                          MsgLend {
                              string   lender
                             
                              uint64   asset_id 
                             
                              cosmos.base.v1beta1.Coin   amount
                             
                              uint64   pool_id 
                             
                              uint64   app_id 
                         
                         }

------

2.MsgDeposit:
*************

         -An user can add further IBC-assets to their existing lend position by the Msgdeposit Txn.
         
         -As the tx is done the Amount goes to the respective cPool Module account and the user’s Available to borrow is updated.
         
         -Additional cToken is provided to the user.

                         MsgDeposit {
                             string   lender
                             
                             uint64   lend_id 
                             
                             cosmos.base.v1beta1.Coin   amount   

                         }

-------

3.MsgWithdraw:
***************

         -An user can withdraw further IBC-assets to their existing lend position by the Msgdeposit Txn.
         
         -User enters the amount to withdraw and then the equivalent amount of cToken is transferred to the module account of the respective cPool and finally burned.
         
         -Available to borrow is updated accordingly.
         
         -The max amount that can be withdrawn is limited to available to borrow.

                         MsgWithdraw {
                             string    lender 
                             
                             uint64    lend_id
                             
                             cosmos.base.v1beta1.Coin   amount 

                         }

------

4.MsgCloseLend:
****************

         -The user Inputs the lendID, AmountIn(in terms of cToken), AmoutOut(in terms of IBC-Asset), pairId and Stable Borrow check.
         
         -If all the criteria are satisfied then a new borrow position is created.
         
         -Lend to borrow mapping is updated and Available to borrow is reduced by the amountIn token amount.
         
         -Interest starts to get accumulated for the borrowed position for the borrowed amount.

                         MsgCloseLend {
                             string  lender
                             
                             uint64  lend_id 

                         }

-------

5.MsgRepay:
************

         -An User can Repay the Borrowed Amount by using MsgRepay txn.
         
         -However the user can't close the lend position by Msgrepay Txn.
         
         -After Repayment, the total borrowed is updated.
         
         -Whenever a user repays, first his interest is settled and then the borrowed amount is reduced.    

                         MsgRepay {
                             string   borrower
                             
                             uint64   borrow_id
                             
                             cosmos.base.v1beta1.Coin   amount

                         }

-------
                     
6.MsgDepositBorrow:
********************

         -This Txn is similar to Msg Deposit.
         
         -Here an user can deposit an additional amount of cToken to his borrowed position to maintain the collateralization ratio.
         
         -AmountIn is updated after the txn is done.
         
         -Available to borrow is also updated after the txn is done.

                         MsgDepositBorrow {
                             string   borrower
                             
                             uint64   borrow_id
                             
                             cosmos.base.v1beta1.Coin   amount 

                         }

--------

7.MsgDraw:
***********

         -If a user wants to take out further IBC-Asset from his borrow position maintaining the collateralization ratio, then this txn is used.
         
         -Additional IBC-Assets are given to the user from the cPool moduleAccount.
         
         -The Borrow position is updated accordingly.

                         MsgDraw {
                             string   borrower 
                             
                             uint64   borrow_id
                             
                             cosmos.base.v1beta1.Coin   amount 

                         }

-------

8.MsgCloseBorrow:
******************

         -This txn is similar to the MsgCloseLend Txn.
             
         -The updated IBC-Asset Amount is taken from the user’s account (amount out + interest accumulated on that) and sent to the cPool module account.
             
         -The cTokens are sent back to the user’s account.
             
         -The borrow Position is deleted from the KV Store and also Available to Borrow is updated.
             
         -If the user doesn't have sufficient funds then the txn fails.

                         MsgCloseBorrow {
                             string   borrower 
                             
                             uint64   borrow_id
                         
                         }

-------

9.MsgBorrowAlternate:
**********************

             -This txn is a combination of lend and borrow.
             
             -The user can create a borrow position directly by lending the IBC-Assets using the lend position.
             
             -The lent IBC-Assets are converted to corresponding cAssets and using them as the deposit token a borrow position is opened.
             
             -The user can edit their lend and borrow position individually thereafter.

                         MsgBorrowAlternate {
                             string   lender 
                             
                             uint64   asset_id 
                             
                             uint64   pool_id 
                             
                             cosmos.base.v1beta1.Coin   amount_in
                             
                             uint64   pair_id
                             
                             bool   is_stable_borrow
                             
                             cosmos.base.v1beta1.Coin   amount_out
                             
                             uint64   app_id 

                         }

--------

10.MsgFundModuleAccounts:
**************************

             -This txn is used to fund the cPools Module Account to bootstrap the liquidity for the protocol.
             
             -AssetId, cPool Module name and Amount is provided by the user. After the txn the specified amount is sent to the moduleAccount from the user’s account.

                         MsgFundModuleAccounts {
                             string   moduleName
                             
                             uint64   assetId
                             
                             string   lender
                             
                             cosmos.base.v1beta1.Coin   amount

                         }

-------

11.MsgFundReserveAccounts:
***************************

                         MsgFundReserveAccounts{
                             uint64   assetId
                             
                             string   lender
                             
                             cosmos.base.v1beta1.Coin   amount

                         }     

-------

12.MsgCalculateInterestAndRewards:
***********************************
          
                         MsgCalculateInterestAndRewards{
                             string   borrower
                         
                         }    
                    


