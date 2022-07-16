from classes.Comp import Comp
from classes.EvRepeat import EvRepeat
from classes.Hole import Hole
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


def get_pitch(mb: MeasureBeat):
    t = mb.to_time(tempo)
    peak = length * 2/3
    if t < peak:
        return interp_limit(0, t, peak, bottom_pitch, top_pitch)
    return interp_limit(peak, t, length, top_pitch, bottom_pitch)


def gen_mel(comp: Comp):
    scorer = Scoring([EvInChord(), EvRange(
        get_pitch, 8, -100, 100), EvRepeat()], 36, 84)
    holes = []
    for i in range(1, comp.num_msrs + 1):
        holes.append(Hole(MeasureBeat(i, 1, (4, 4)), 2))
        holes.append(Hole(MeasureBeat(i, 3, (4, 4)), 1))
        holes.append(Hole(MeasureBeat(i, 4, (4, 4)), 1))
    # holes.append(Hole(MeasureBeat(comp.num_msrs, 1, (4, 4)), 4))
    comp.gen_melody(scorer, holes)


tempo = 60
bottom_pitch = 63
top_pitch = 78
length = MeasureBeat(5, 1, (4, 4)).to_time(tempo)


session = Session()
# comp = Comp(4, [
#     Chord2("A7/C#3"),
#     Chord2("D7/D3"),
#     Chord2("F/A2"),
#     Chord2("G7/G2"),
#     Chord2("C7/C3")
# ])

#  Gb Db Ab Eb Bb F C G D A E B F#
#   ii V I
#  C major (C E G), D minor (D F A), E minor (E G B), F maj (F A C), G maj (G B D), A min (A C E) B dim (B D F)

comp = Comp([
        (MeasureBeat(1, 1, (4, 4)),Chord2("E7/E3")),
        (MeasureBeat(1, 3, (4, 4)),Chord2("A7/A2")),
        (MeasureBeat(2, 1, (4, 4)), Chord2("G7/G2")),
        (MeasureBeat(2, 3, (4, 4)), Chord2("C/C3"))
    ], 2)


comp.gen_bass()
comp.gen_harmony()
gen_mel(comp)

# print(str(comp))
part_config = {"bass": 1, "harmony": 2, "melody": 3}
LNotes = comp.convert()
part_dict = create_part_dict(session, LNotes, part_config)
play(part_dict, LNotes)
