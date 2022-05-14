from classes.MeasureBeat import MeasureBeat
from classes.Note import Note
from classes.util import P, nearest_from_multiple_pc


class Comp:
    def __init__(self, msr_len, chord_list) -> None:
        self.msr_len = msr_len
        self.chord_list = chord_list
        self.bassline = []
        self.melody = []
        self.tempo = 60
        self.notes = []
        self.time_sig = (4,4)

    def gen_bass(self):
        dur = self.time_sig[0]* 60/self.tempo
        for i in range(len(self.chord_list)):
            mb = MeasureBeat(i+1, 1, self.time_sig)
            self.notes.append(
                Note(mb.to_time(self.tempo), dur, self.chord_list[i].bass_note, 0.7, "bass"))

    def gen_harmony(self):
        dur = dur = self.time_sig[0]* 60/self.tempo
        lower = P("C3")
        upper = P("G4")
        for i in range(len(self.chord_list)):
            mb = MeasureBeat(i+1, 1, self.time_sig)
            pcs = self.chord_list[i].pitch_classes
            for approx_pitch in range(lower, upper, 3):
                pitch = nearest_from_multiple_pc(approx_pitch, pcs)
                self.notes.append(
                    Note(mb.to_time(self.tempo), dur, pitch, 0.7, "harmony"))

    def gen_melody(self, scorer):
        mb = MeasureBeat(1, 1, self.time_sig)
        i = 0
        while i < 4*len(self.chord_list):
            # pick pitch here

            pit = scorer.ev(self, mb)
            self.notes.append(Note(mb.to_time(self.tempo),
                              60/self.tempo/4, pit, 0.5, "melody"))
            if mb.beat > 0 and mb.beat % 4 == 0:
                mb.measure += 1
            mb.beat = i % 4 + 1
            i += 1

    def __str__(self):
        return "\n".join(map(str, self.notes)) + "\n"
