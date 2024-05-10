from pydantic import BaseModel, Field


class Range(BaseModel):
    a: float = Field(default=-1)
    b: float = Field(default=1)


class PlotRequest(BaseModel):
    m: float
    b: float
    range: Range = Field(default=Range())
