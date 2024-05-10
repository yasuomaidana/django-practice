from pydantic import BaseModel


class TicketDTO(BaseModel):
    category: str
    description: str


class TicketCreateDTO(TicketDTO):
    pass
