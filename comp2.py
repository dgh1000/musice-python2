# I IV ii V7 I
# experiment with num_pitches
# experiment with root. lower down, higher up.
# different octaves for different chords
# tonic: 60
# root IV: 65

import sys
sys.path.append("..")

import classes.Note 
import classes.Motive2
from scamp import *
import classes.Play
import classes.Chord

chords = [classes.Chord.Chord.major_chord(60, 3), 
          classes.Chord.Chord.major_chord(65, 3), 
          classes.Chord.Chord.minor_chord(62, 3),
          classes.Chord.Chord.dom7(67, 4),
          classes.Chord.Chord.major_chord(60, 3)]
times = [i * 2 for i in range(len(chords))]
#print(*zip(*[n.to_list() for i in range(len(chords)) for n in chords[i].to_notes(times[i], 1.0, 0.5)]))
notes = [n for i in range(len(chords)) for n in chords[i].to_notes(times[i], 1.0, 0.5)]
#notes = motive1.render(0)
s = Session()
o = s.new_part("trombone")
classes.Play.play(o, notes)
