from dataclasses import dataclass
from datetime import datetime


@dataclass
class GasParametrs:
    tabs: datetime
    trel: int
    h_2: float
    co: float
    co_2: float
    ch_4: float
    comments: str = ""
