from classes.Comp import Comp
from classes.EvInChord import EvInChord
from classes.EvRange import EvRange
from classes.EvRepeat import EvRepeat
from classes.Hole import Hole
from classes.MeasureBeat import MeasureBeat
from classes.Scoring import Scoring
from classes.util import interp_limit


# def get_pitch_a(mb: MeasureBeat):
#     t = mb.to_time(tempo)
#     peak = length * 2/3
#     if t < peak:
#         return interp_limit(0, t, peak, bottom_pitch, top_pitch)
#     return interp_limit(peak, t, length, top_pitch, bottom_pitch)

def get_pitch_b(time: float, end: float) -> float:
    return 70.0

scorer_a = Scoring([EvInChord(), EvRange(
            get_pitch_b, 20, -100, 100), EvRepeat(6)], 36, 84)


def gen_mel(comp: Comp, scorer: Scoring):
    holes = []
    for i in range(1, comp.num_msrs):
        for j in range(12, 40):
            # constant beat duration: cause problems? will cause
            # overlapping notes. shouldn't be a problem. 
            holes.append(Hole(MeasureBeat(i, j/8), 0.125))
    # holes.append(Hole(MeasureBeat(comp.num_msrs, 1, (4, 4)), 4))
    comp.gen_melody(scorer, holes)
