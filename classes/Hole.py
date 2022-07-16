from dataclasses import dataclass

from classes.MeasureBeat import MeasureBeat

# dur is in beats

@dataclass
class Hole:
    time: MeasureBeat
    dur: float


        