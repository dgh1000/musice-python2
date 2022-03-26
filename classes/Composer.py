from classes.MeasureBeat import MeasureBeat
from .Note import Note
from .Chord2 import Chord2
from .util import *

class Composer:
    def __init__(self) -> None:
        self.chord_list = []
        self.scale = []
        self.parts = {}
        self.part_config = {}
        self.tempo = 60
        self.time_sig = (4,4)
        self.notes = []

    def compute_bassline(self):
        dur = 60 * self.time_sig[0] / self.tempo 
        self.notes += [Note(c * dur,
                        dur,
                        self.chord_list[c].bass_note,
                        1.0,
                        "bass")
                    for c in range(len(self.chord_list))]

    def compute_harmonies(self):
        dur = 60 * self.time_sig[0] / self.tempo 
        for c in range(len(self.chord_list)):
            for h in self.chord_list[c].harmonies:
                self.notes.append(Note(c * dur, dur, h, 0.5, "harmony"))

    def compute_melody(self):
        melody_span = 60 * self.time_sig[0] / self.tempo * len(self.chord_list)
        def compute_approx(time: float):
            if (time < melody_span/2):
                return interp_limit(0, time, melody_span/2, 60, 75)
            return interp_limit(melody_span/2, time, melody_span, 75, 60)
        # loop over each beat 
        msr = 1
        beat = 1
        for i in range(len(self.chord_list) * self.time_sig[0]):
            ch = self.chord_list[msr-1]
            mb = MeasureBeat(msr, beat, self.time_sig, self.tempo)
            t = mb.to_time()
            pc = nearest_from_multiple_pc(compute_approx(t), ch.pitch_classes)
            self.notes.append(Note(t, 60/self.tempo, pc, 1.0, "melody"))
            beat += 1
            if beat > self.time_sig[1]:
                beat = 1
                msr += 1
        # determine MeasureBeat of melody note
        # 
        # determine which chord: msr of MeasureBeat
        # 
        # find pitch classes that are part of chord
        # use nearest_from_multiple_pc to find an actual note
        # add that note to a list of notes that make up our melody

# pick one note , one chord at a time. picking first chord. 2nd chord
# pick first note, second note. pick chords by hand. pick first note, second note
# try every possible note. and have scoring criteria
# class Eval: base class. subclass InChord
#   job is to evaluate whether a melody note is present in thte currernt chord
# InChord -> 0 to anything in the chord, -1000000 anything not in the chord
# Range -> has the shape curve -> gives higher score to notes closer to the shape curve
# Rep -> gives high schore to repetitions on beat 2, low score to reps on beats 1, 3, & 4

# 0     1      2      3      4      3      2      1
# |  |  |   |  |   |  |   |  |  |
                
        
        
    