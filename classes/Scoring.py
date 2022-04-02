from .Ev import Ev
import random

class Scoring:
    def __init__(self, evs: list[Ev], min_pitch: int, max_pitch: int) -> None:
        self.evs = evs
        self.min_pitch = min_pitch
        self.max_pitch = max_pitch

    def ev(self, comp, mb):
        pitches = []
        for pitch in range(self.min_pitch, self.max_pitch + 1):
            score = 0
            for ev_ in self.evs:
                score += ev_.ev(comp, pitch, mb)
            pitches.append([pitch, score])
        pitches.sort(key=lambda x: x[1], reverse=True)
        idx = 0
        while idx < len(pitches) - 1:
            if pitches[idx] != pitches[idx + 1]:
                return idx
        return random.choice(pitches[:idx + 1][0])



