from .Note import Note
from .Chord2 import Chord2
from .util import *

class Composer:
    def __init__(self) -> None:
        self.chord_list = []
        self.scale = []
        self.parts = {}
        self.tempo = 60
        self.time_sig = (4,4)
        self.notes = []

    def compute_bassline(self):
        dur = 60 * self.time_sig[0] / self.tempo 
        self.notes += [Note(c * dur,
                        dur,
                        self.chord_list[c].bass_note,
                        1.0,
                        self.parts["bass"])
                    for c in range(len(self.chord_list))]

    def compute_harmonies(self):
        dur = 60 * self.time_sig[0] / self.tempo 
        for c in range(len(self.chord_list)):
            for h in self.chord_list[c].harmonies:
                self.notes.append(Note(c * dur, dur, h, 1.0, self.parts["harmony"]))

    def compute_melody(self):
        melody_span = 60 * self.time_sig[0] / self.tempo * len(self.chord_list)
        def compute_approx(time: float):
            if (time < melody_span/2):
                return interp_limit(0, time, melody_span/2, 60, 75)
            return interp_limit(melody_span/2, time, melody_span, 75, 60)
        
        
    