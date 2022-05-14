from .Ev import Ev

class EvInChord(Ev):
    def __init__(self) -> None:
        pass

    def ev(self, comp, pitch, mb):
        ch = comp.chord_list[mb.measure - 1]
        return int(pitch % 12 not in ch.pitch_classes) * -1000000