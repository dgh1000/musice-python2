from __future__ import annotations
from dataclasses import dataclass

@dataclass
class MeasureBeat:
    # def __init__(self, measure: int, beat: int, time_sig: tuple[int, int]) -> None:
    #     self.measure = measure
    #     self.beat = beat
    #     self.time_sig = time_sig
    measure: int
    beat: int
    # time_sig: tuple[int, int]

    # def to_time(self, tempo: float) -> float:
    #     # one beat : 4 * (1/60) * time_sig[0] / time_sig[1]

    #     # (4/time_sig[1]) * (tempo/60)
    #     one_beat =  (4/self.time_sig[1]) * (tempo/60)
    #     return ((self.measure - 1) * self.time_sig[0] + self.beat - 1) * one_beat


    def __lt__(self, other: MeasureBeat) -> bool:
        if self.measure == other.measure:
            return self.beat < other.beat
        return self.measure < other.measure

    def __le__(self, other: MeasureBeat) -> bool:
        if self.measure == other.measure:
            return self.beat <= other.beat
        return self.measure <= other.measure

    def __eq__(self, other: MeasureBeat) -> bool:
        return self.measure == other.measure and self.beat == other.beat 

    def __sub__(self, other: MeasureBeat) -> float:
        return self.measure * 4 + self.beat - (other.measure * 4 + other.beat)
    
    

if __name__ == "__main__":
    test0 = MeasureBeat(3, 1, (4, 4))
    test1 = MeasureBeat(2, 2, (4, 4))
    print(test0 <= test1)