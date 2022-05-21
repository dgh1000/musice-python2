from dataclasses import dataclass

from classes.MeasureBeat import MeasureBeat


@dataclass
class Hole:
    time: MeasureBeat
    dur: float


if __name__ == "__main__":
    print(Hole(5, 5))

        