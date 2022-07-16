from classes.Note import Note
from classes.Motive2 import Motive2
from scamp import *
from classes.Play import *
from classes.util import *
from classes.Chord2 import Chord2
from classes.Composer import Composer
import rtmidi


composer = Composer()
composer.chord_list = [
    Chord2(P("D3"), [0, 3, 7], [P("A3"), P("F4")], (0, 0)),
    Chord2(P("G3"), [0, 4, 7, 11], [P("D4"), P("F4"), P("B4")], (0, 0)),
    Chord2(P("C3"), [0, 4, 7], [P("G3"), P("E4")], (0, 0)),
    ]


s = Session()
composer.part_config["bass"] = 1
composer.part_config["harmony"] = 2
composer.part_config["melody"] = 3
composer.compute_bassline()
composer.compute_harmonies()
composer.compute_melody()
print(composer.notes)

play(create_part_dict(s, composer.notes, composer.part_config), composer.notes)