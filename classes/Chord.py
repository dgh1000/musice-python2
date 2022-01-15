from .Note import Note

class Chord:
    def __init__(self, pitches: list[int]) -> None:
        self.pitches = pitches

    @staticmethod
    def major_chord(root: int, num_pitches: int):
        return Chord.abstract_chord([0, 4, 7], root, num_pitches)

    @staticmethod
    def minor_chord(root: int, num_pitches: int):
         return Chord.abstract_chord([0, 3, 7], root, num_pitches)

    @staticmethod
    def dom7(root: int, num_pitches: int):
         return Chord.abstract_chord([0, 4, 7, 10], root, num_pitches)

    @staticmethod
    def abstract_chord(deltas: list[int], root: int, num_pitches: int):
        return Chord([root + deltas[i%len(deltas)] + 12 * (i//len(deltas)) for i in range(num_pitches)])
        
    def to_notes(self, time: float, dur: float, dyn: float) -> list[int]:
        return [Note(time, dur, pitch, dyn) for pitch in self.pitches]