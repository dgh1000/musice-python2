from classes.Note import Note
from classes.Motive2 import Motive2
from scamp import *
from classes.Play import *
from classes.Chord2 import Chord2

chord = Chord2(48, [0, 4, 7], [52, 55, 60], (60, 78))
s = Session()
part_dict = create_part_dict(s, chord_to_notes(chord, 0))
play(part_dict, chord_to_notes(chord, 0))