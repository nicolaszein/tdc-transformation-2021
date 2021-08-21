import uuid
from dataclasses import dataclass, field, replace


@dataclass(frozen=True)
class Employee:
    name: str
    role: str

    id: uuid.UUID = field(init=True, default_factory=uuid.uuid4)

    def update_role(self, new_role):
        return replace(self, role=new_role)
