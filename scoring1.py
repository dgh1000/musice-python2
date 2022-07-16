from typing import Tuple
from classes.Chord2 import Chord2
from classes.EvInChord import EvInChord
from classes.EvRange import EvRange
from classes.EvRepeat import EvRepeat
from classes.Hole import Hole
from classes.LNote import LNote
from classes.MeasureBeat import MeasureBeat
from classes.Scoring import Scoring
from classes.util import interp_limit

def get_pitch(mb: MeasureBeat, length, bottom_pitch, top_pitch, tempo):
    t = mb.to_time(tempo)
    peak = length * 2/3
    if t < peak:
        return interp_limit(0, t, peak, bottom_pitch, top_pitch)
    return interp_limit(peak, t, length, top_pitch, bottom_pitch)


scorer = Scoring([EvInChord(), EvRange(
        get_pitch, 8, -100, 100), EvRepeat()], 36, 84)
