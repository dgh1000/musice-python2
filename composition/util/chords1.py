from classes.Chord2 import Chord2
from classes.MeasureBeat import MeasureBeat


chords_a = [
    (MeasureBeat(1, 1), Chord2("C/C3")), 
    (MeasureBeat(2, 1), Chord2("Dm/D3")),
    (MeasureBeat(3, 1), Chord2("Em/E3")),
    (MeasureBeat(4, 1), Chord2("F/F3")),
    (MeasureBeat(5, 1), Chord2("G/G3")),
    # (MeasureBeat(6, 1), Chord2("Am/A3")),
    # (MeasureBeat(7, 1), Chord2("Bm/B3")),
    # (MeasureBeat(8, 1), Chord2("C/C3"))
]

# I IV/vi V/vi vi iih7/ii IV/ii ii
# 
chords_b = [
    (MeasureBeat(1, 1), Chord2("C/C3")), 
    (MeasureBeat(2, 1), Chord2("D/F#3")),
    (MeasureBeat(3, 1), Chord2("E/E3")),
    (MeasureBeat(4, 1), Chord2("Am/A3")),
    (MeasureBeat(5, 1), Chord2("Eh7/E3")),
    (MeasureBeat(6, 1), Chord2("A7/A3")),
    (MeasureBeat(7, 1), Chord2("Dm/D3")),
    (MeasureBeat(8, 1), Chord2("D7/D3")),
    (MeasureBeat(9, 1), Chord2("G7/G3")),
    (MeasureBeat(10, 1), Chord2("C/C3")),
]

chords_a_len = len(chords_a)
chords_b_len = len(chords_b)
