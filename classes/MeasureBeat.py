from __future__ import annotations
from dataclasses import dataclass
from re import I

@dataclass
class MeasureBeat:
    # def __init__(self, measure: int, beat: int, time_sig: tuple[int, int]) -> None:
    #     self.measure = measure
    #     self.beat = beat
    #     self.time_sig = time_sig
    measure: int
    beat: int
    time_sig: tuple[int, int]

    def to_time(self, tempo: float) -> float:
        # one beat : 4 * (1/60) * time_sig[0] / time_sig[1]

        # (4/time_sig[1]) * (tempo/60)
        one_beat =  (4/self.time_sig[1]) * (tempo/60)
        return ((self.measure - 1) * self.time_sig[0] + self.beat - 1) * one_beat
    
    

if __name__ == "__main__":
    test = MeasureBeat(1, 1, (4, 4), 60)
    print(test.to_time())