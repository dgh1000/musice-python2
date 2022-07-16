from classes.Comp import Comp
from classes.Hole import Hole
from classes.MeasureBeat import MeasureBeat
from classes.Play import play
from classes.util import create_part_dict
from scamp import *
from .util.chords1 import chords_a, chords_a_len
from .util.melody1 import scorer_a, gen_mel

session = Session()

comp = Comp(chords_a, chords_a_len, {i:(4, 4) for i in range(1, chords_a_len+1)}, {i: 120 for i in range(1, chords_a_len + 1)})
bass_holes: list[Hole] = []
for i in range(1, chords_a_len + 1):
    # 1, 2.5, 3.5, 4.5
    bass_holes.append(Hole(MeasureBeat(i, 1), 0.75))
    bass_holes.append(Hole(MeasureBeat(i, 2), 0.75))
    bass_holes.append(Hole(MeasureBeat(i, 3), 0.75))
    bass_holes.append(Hole(MeasureBeat(i, 4), 0.75))
comp.gen_bass(bass_holes)
comp.gen_harmony([Hole(MeasureBeat(i, 1), 0.5) for i in range(1, chords_a_len)] +
                 [Hole(MeasureBeat(chords_a_len, 1), 4)])
gen_mel(comp, scorer_a)
snare_holes: list[Hole] = []
for i in range(1, chords_a_len + 1):
    # 1, 2.5, 3.5, 4.5
    snare_holes.append(Hole(MeasureBeat(i, 1), 0.25))
    snare_holes.append(Hole(MeasureBeat(i, 2), 0.25))
    snare_holes.append(Hole(MeasureBeat(i, 3), 0.25))
    snare_holes.append(Hole(MeasureBeat(i, 4), 0.25))
    snare_holes.append(Hole(MeasureBeat(i, 4.5), 0.25))
    snare_holes.append(Hole(MeasureBeat(i, 4.625), 0.25))
    snare_holes.append(Hole(MeasureBeat(i, 4.750), 0.25))
    snare_holes.append(Hole(MeasureBeat(i, 4.875), 0.25))

high_hat_holes: list[Hole] = []
for i in range(1, chords_a_len + 1):
    # 1, 2.5, 3.5, 4.5
    high_hat_holes.append(Hole(MeasureBeat(i, 1), 0.25))
    high_hat_holes.append(Hole(MeasureBeat(i, 2), 0.25))
    high_hat_holes.append(Hole(MeasureBeat(i, 2.667), 0.25))
    high_hat_holes.append(Hole(MeasureBeat(i, 3), 0.25))
    high_hat_holes.append(Hole(MeasureBeat(i, 4), 0.25))
    high_hat_holes.append(Hole(MeasureBeat(i, 4.667), 0.25))
comp.gen_percussion([], 
                    snare_holes,
                    high_hat_holes)




part_config = {"bass": 1, "harmony": 2, "melody": 3, "perc": 4}
LNotes = comp.convert()
part_dict = create_part_dict(session, LNotes, part_config)
play(part_dict, LNotes)

