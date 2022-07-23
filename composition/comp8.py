from classes.Comp import Comp
from classes.Hole import Hole
from classes.MeasureBeat import MeasureBeat
from classes.Play import play
from classes.util import create_part_dict
from composition.util.percussion1 import gen_perc
from scamp import *
from .util.chords1 import chords_b, chords_b_len
from .util.melody1 import scorer_a, gen_mel

session = Session()

comp = Comp(chords_b, chords_b_len, {i:(4, 4) for i in range(1, chords_b_len+1)}, {i: 120 for i in range(1, chords_b_len + 1)})
bass_holes: list[Hole] = []
for i in range(1, chords_b_len + 1):
    # 1, 2.5, 3.5, 4.5
    bass_holes.append(Hole(MeasureBeat(i, 1), 0.75, 0.7))
    bass_holes.append(Hole(MeasureBeat(i, 2), 0.75, 0.7))
    bass_holes.append(Hole(MeasureBeat(i, 3), 0.75, 0.7))
    bass_holes.append(Hole(MeasureBeat(i, 4), 0.75, 0.7))
comp.gen_bass(bass_holes)
comp.gen_harmony([Hole(MeasureBeat(i, 1), 0.5, 0.7) for i in range(1, chords_b_len)] +
                 [Hole(MeasureBeat(chords_b_len, 1), 4, 0.7)])
gen_mel(comp, scorer_a)
comp.gen_percussion(*gen_perc(chords_b_len))




part_config = {"bass": 1, "harmony": 2, "melody": 3, "perc": 4}
LNotes = comp.convert()
part_dict = create_part_dict(session, LNotes, part_config)
play(part_dict, LNotes)

