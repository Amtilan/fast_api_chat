from dataclasses import dataclass
from domain.values.messages import Text

@dataclass
class Message:
    object_id: str
    text: Text