from base64 import b64encode
import aiohttp
from typing import Union
from .User import User
from .getSkin import Skin
from .paymentsParam import PaymentParameters, TransactionParameters

class asyncSPW():
    """asyncSPW api, Using Corouеione in most cases is great for freights with ASYNC | AWAIT syntax

    Returns:
        None: class not return anythyng
    """
    __spworlds_api_url = 'https://spworlds.ru/api/public'
    def __init__(self, card_token, card_id):
        """We offer to use asyncSPW like this: \n
            >>> import asyncSPW
            >>> api = asyncSPW.api("ur_card_token", "ur_card_id)
            >>> await api.get_user(discord_id).nickname 
            -> YaFlay
            
        \n
        Args:
            card_token (_type_): _description_
            card_id (_type_): _description_
        """
        self.card_id = card_id
        self.token_id = f"Bearer {str(b64encode(str(f'{card_id}:{card_token}').encode('utf-8')), 'utf-8')}"
    
    async def __get(self, path: str, ignore_status: bool = False) -> aiohttp.ClientResponse:
        """Get data from SPW api.

        Args:
            path (str): path to GET likely(/users/{user_id}/)
            ignore_status (bool, optional): return data with all cases. Defaults to False.
            json_decode (bool, optional): Automatically decode returns data to json. Defaults to False.

        Returns:
            [aiohttp.ClientResponse]: Returns site response 
        """
        header = {
            'Authorization': self.token_id,
            'Agent': "AsyncSPW"
        }
        async with aiohttp.ClientSession() as session:
            async with session.get(self.__spworlds_api_url+path, data=header) as r:
                
                if ignore_status:
                    return r
                if r.status == 200:
                    return r
                elif r.status >= 500:
                    raise (f'HTTP: {r.status}, Server Error.')
                
                    
    async def __post(self, path: str, ignore_status:bool = False) -> aiohttp.ClientResponse:
        """Post data to SPW api.

        Args:
            path (str): path to POST likely(/users/{user_id}/)
            ignore_status (bool, optional): return data with all cases. Defaults to False.
            json_decode (bool, optional): Automatically decode returns data to json. Defaults to False.

        Returns:
            [aiohttp.ClientResponse]: Returns site response or json element
        """
        header = {
            'Authorization': self.token_id,
            'Agent': "AsyncSPW"
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.__spworlds_api_url+path, data=header) as r:
                

                if ignore_status:
                    return r
                if r.status == 200:
                    return r
                elif r.status >= 500:
                    raise (f'HTTP: {r.status}, Server Error.')
    async def get_user(self, user_id: str) -> User:
        """Get user from SPW api

        Args:
            user_id (str): Discord ID of the user

        Returns:
            User: User type
        """
        userResponse = await self.__get(f"/users/{user_id}", True)  
        
        if userResponse.status == 200:
            jsonData = await userResponse.json()['username']
            return User(jsonData, True)
        elif userResponse.status >= 500:
            return User(None, False)
        else:
            raise (f'HTTP: {userResponse.status}, Server error')
        
    async def check_is_player(self, player_id: str) -> bool:
        """Obtaining the status of a hill on a selected server

        Args:
            player_id (str): Discord ID of the player

        Returns:
            bool: Status
        """
        return await self.get_user(player_id).is_player
    
    async def get_skin(self, player_id: str) -> Skin:
        """Obtaining and returning user skin

        Args:
            player_id (str): Discord ID of the player

        Returns:
            Skin: user`s skin
        """
        return await self.get_user(player_id).get_skin()
    
    async def create_payment(self, params: PaymentParameters) -> str:
        """Create payment url

        Args:
            params (PaymentParameters): Parameters for the payment

        Returns:
            str: Payment url
        """

        body = {
            'amount': params.amount,
            'redirectUrl': params.redirectUrl,
            'webhookUrl': params.webhookUrl,
            'data': params.data
        }
        return await self.__post('/payment', body).json()['url']

    async def send_transaction(self, params: TransactionParameters) -> int:
        """Send a transaction to user

        Args:
            params (TransactionParameters): Parameters for transaction

        Returns:
            int: Transaction status
        """

        body = {
            'receiver': params.receiver,
            'amount': params.amount,
            'comment': params.comment
        }
        return await self.__post('/transactions', body).status
    
    async def get_balance(self) -> int:
        """Returns user's balance

        Returns:
            int: user`s balance 
        """

        return await self.__get('/card').json()['balance']