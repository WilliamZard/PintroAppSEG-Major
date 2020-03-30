import uuid
from dataclasses import dataclass

from .users import User


@dataclass
class Chatroom:
    chat_id: uuid.UUID

    def __init__(self, chat_id=None):
        if chat_id is None:
            chat_id = uuid.uuid4()
        self.chat_id = chat_id

    def _asdict(self):
        return {'chat_id': self.chat_id}
