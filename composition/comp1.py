# I IV ii V7 I
# experiment with num_pitches
# experiment with root. lower down, higher up.
# different octaves for different chords
# tonic: 60
# root IV: 65


import classes.Note 
import classes.Motive2
from scamp import *
import classes.Play


motive1 = classes.Motive2.Motive2([1.0, 1.0], [1.0, 1.0], [60, 62], [0.5, 0.5])
notes = motive1.render(0)
s = Session()
o = s.new_part("trombone")
classes.Play.play(o, notes)
