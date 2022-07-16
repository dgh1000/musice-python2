from dataclasses import dataclass

# dur is in seconds. time is in seconds.

@dataclass
class LNote:
    time: float
    dur: float
    pitch: int
    dyn: float
    inst: str
