from classes import Chord2, MeasureBeat
from .Ev import Ev

class EvInChord(Ev):
    def __init__(self) -> None:
        pass

    def ev(self, comp, pitch, mb):
        ch = comp.get_chord_at(mb)
        return int(pitch % 12 not in ch.pitch_classes) * -1000000

