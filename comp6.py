from classes.Comp import Comp
from classes.MeasureBeat import MeasureBeat
from classes.Note import Note
from classes.Motive2 import Motive2
from classes.Scoring import Scoring
from scamp import *
from classes.Play import *
from classes.util import *
from classes.Chord2 import Chord2
from classes.MeasureBeat import MeasureBeat
from classes.EvInChord import EvInChord
from classes.EvRange import EvRange


tempo = 60
bottom_pitch = 63
top_pitch = 78
length = MeasureBeat(5, 1, (4, 4)).to_time(tempo)


def get_pitch(mb: MeasureBeat):
    t = mb.to_time(tempo)
    peak = length * 2/3
    if t < peak:
        return interp_limit(0, t, peak, bottom_pitch, top_pitch)
    return interp_limit(peak, t, length, top_pitch, bottom_pitch)

comp = Comp(4, [
    Chord2(P("A3"), [0, 3, 7], [P("")]),
    Chord2(P("D3"), [0, 3, 7], [P("A3"), P("F4")], (0, 0)),
    Chord2(P("G3"), [0, 4, 7, 11], [P("D4"), P("F4"), P("B4")], (0, 0)),
    Chord2(P("C3"), [0, 4, 7], [P("G3"), P("E4")], (0, 0)),
    ])
scorer = Scoring([EvInChord(), EvRange(get_pitch, 8, -100, 100)], 36, 84)

