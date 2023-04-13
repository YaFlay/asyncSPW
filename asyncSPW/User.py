from typing import List, Dict, Any, Optional, Union
from mojang import MojangAPI

from .getSkin import Skin

class User():
    def __init__(self, nickname: str | None, use_mojang_api: bool = True):
        self.nickname = nickname

        if self.nickname is not None:
            self.is_player = True

            if use_mojang_api:
                self.uuid = MojangAPI.get_uuid(nickname)

        else:
            self.uuid = None
            self.is_player = False

    def __str__(self) -> Union[str, None]:
        if self.nickname is None:
            return 'None'

        return self.nickname

    def get_skin(self) -> Union[Skin, None]:
        if self.uuid is None:
            return None

        return Skin(self.uuid)

    def get_nickname_history(self) -> Optional[List[Dict[str, Any]]]:
        if self.uuid is None:
            return None

        return MojangAPI.get_name_history(self.uuid)
# Special thanks to Teleport2 and his Pyspw library, where did I get several sources