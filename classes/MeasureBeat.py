class MeasureBeat:
    def __init__(self, measure: int, beat: int, time_sig: tuple[int, int], tempo: float) -> None:
        self.measure = measure
        self.beat = beat
        self.time_sig = time_sig
        self.tempo = tempo

    def to_time(self) -> float:
        # one beat : 4 * (1/60) * time_sig[0] / time_sig[1]

        # (4/time_sig[1]) * (tempo/60)
        one_beat =  (4/self.time_sig[1]) * (self.tempo/60)
        return ((self.measure - 1) * self.time_sig[0] + self.beat - 1) * one_beat

if __name__ == "__main__":
    test = MeasureBeat(1, 1, (4, 4), 60)
    print(test.to_time())