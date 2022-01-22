from Note import Note
from Chord2 import Chord2


class Composer:
    def __init__(self) -> None:
        self.chord_list = []
        self.scale = []
        self.parts = {}
        self.tempo = 60
        self.time_sig = (4,4)
        self.notes = []

    def compute_bassline(self):
        dur = self.time_sig[0]/self.tempo
        notes += [Note(c * dur,
                        dur,
                        self.chord_list[c].bassnote,
                        1.0,
                        self.parts["bass"])
                    for c in range(len(self.chord_list))]

    