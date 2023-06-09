import requests as rq
from mojang import MojangAPI
from typing import Optional
import aiohttp
from . import errors as err


class SkinPart:
    def __init__(self, url: str):
        self.__skin_part_url = url

    def __str__(self):
        return self.get_url()

    def __bytes__(self):
        return self.get_image()

    def get_url(self) -> str:
        return self.__skin_part_url

    async def get_image(self) -> bytes:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(self.__skin_part_url) as r:
                    if r.status == 200:
                        return r.content
                    elif r.status >= 500:
                        raise (f'HTTP status: {r.status}, Server Error.')

        except aiohttp.ClientConnectionError as error:
            raise err.SurgeplayApiError(error)

class Cape:
    def __init__(self, url: Optional[str]):
        self.__skin_part_url = url

    def __str__(self):
        if self.__skin_part_url is None:
            return 'None'

        return self.get_url()

    def __bytes__(self):
        image = self.get_image()
        if image is None:
            return bytes(0)

        return image

    def get_url(self) -> Optional[str]:
        if self.__skin_part_url is None:
            return None

        return self.__skin_part_url

    async def get_image(self) -> Optional[bytes]:
        if self.__skin_part_url is None:
            return None

        try:
            
            async with aiohttp.ClientSession() as session:
                async with session.get(self.__skin_part_url) as r:
                    if r.status == 200:
                        return r.content
                    elif r.status >= 500:
                        raise (f'HTTP status: {r.status}, Server Error.')

        except aiohttp.ClientConnectionError as error:
            raise err.SurgeplayApiError(error)




class Skin():
    __visage_surgeplay_url = 'https://visage.surgeplay.com/'

    def __init__(self, uuid: str):
        self.__uuid = uuid

    def __str__(self):
        return self.get_skin().__str__()

    def get_face(self, image_size: int = 64) -> SkinPart:
        return SkinPart(f'https://visage.surgeplay.com/face/{image_size}/{self.__uuid}')

    def get_front(self, image_size: int = 64) -> SkinPart:
        return SkinPart(f'https://visage.surgeplay.com/front/{image_size}/{self.__uuid}')

    def get_front_full(self, image_size: int = 64) -> SkinPart:
        return SkinPart(f'https://visage.surgeplay.com/frontfull/{image_size}/{self.__uuid}')

    def get_head(self, image_size: int = 64) -> SkinPart:
        return SkinPart(f'https://visage.surgeplay.com/head/{image_size}/{self.__uuid}')

    def get_bust(self, image_size: int = 64) -> SkinPart:
        return SkinPart(f'https://visage.surgeplay.com/bust/{image_size}/{self.__uuid}')

    def get_full(self, image_size: int = 64) -> SkinPart:
        return SkinPart(f'https://visage.surgeplay.com/full/{image_size}/{self.__uuid}')

    def get_skin(self, image_size: int = 64) -> SkinPart:
        return SkinPart(f'https://visage.surgeplay.com/skin/{image_size}/{self.__uuid}')

    def get_cape(self) -> Cape:
        return Cape(MojangAPI.get_profile(self.__uuid).cape_url)