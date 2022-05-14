from classes.Comp import Comp
from classes.EvRepeat import EvRepeat
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

session = Session()
comp = Comp(4, [
    Chord2("A7/C#3"),
    Chord2("D7/D3"),
    Chord2("F/A2"),
    Chord2("G7/G2"),
    Chord2("C7/C3")
])

comp.gen_bass()
comp.gen_harmony()
scorer = Scoring([EvInChord(), EvRange(get_pitch, 8, -100, 100), EvRepeat()], 36, 84)
comp.gen_melody(scorer)

print(str(comp))
part_config = {"bass": 1, "harmony": 2, "melody": 3}
part_dict = create_part_dict(session, comp.notes, part_config)
play(part_dict, comp.notes)



