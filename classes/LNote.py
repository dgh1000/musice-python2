from dataclasses import dataclass


@dataclass
class LNote:
    time: float
    dur: float
    pitch: int
    dyn: float
    inst: str
