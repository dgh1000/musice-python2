from classes.LNote import LNote
from classes.MeasureBeat import MeasureBeat
from classes.Note import Note
from classes.util import P, nearest_from_multiple_pc


class Comp:
    def __init__(self, msr_len, chord_list) -> None:
        self.msr_len = msr_len
        self.chord_list = chord_list
        self.bassline = []
        self.harmony = []
        self.melody = []
        self.tempo = 60
        self.time_sig = (4,4)

    def gen_bass(self):
        dur = self.time_sig[0]
        # dur = self.time_sig[0]* 60/self.tempo
        for i in range(len(self.chord_list)):
            mb = MeasureBeat(i+1, 1, self.time_sig)
            self.bassline.append(
                Note(mb, dur, self.chord_list[i].bass_note, 0.7, "bass"))

    def gen_harmony(self):
        dur = self.time_sig[0]
        # dur = self.time_sig[0]* 60/self.tempo
        lower = P("C3")
        upper = P("G4")
        for i in range(len(self.chord_list)):
            mb = MeasureBeat(i+1, 1, self.time_sig)
            pcs = self.chord_list[i].pitch_classes
            for approx_pitch in range(lower, upper, 3):
                pitch = nearest_from_multiple_pc(approx_pitch, pcs)
                self.harmony.append(
                    Note(mb, self.time_sig[0], pitch, 0.7, "harmony"))

    def gen_melody(self, scorer):
        mb = MeasureBeat(1, 1, self.time_sig)
        i = 0
        while i < 4*len(self.chord_list):
            # pick pitch here

            pit = scorer.ev(self, mb)
            self.melody.append(Note(mb,
                                   1,
                                   pit,
                                   0.5, 
                                   "melody"))
            print("gen_melody: " + str(mb))
            if mb.beat > 0 and mb.beat % 4 == 0:
                mb.measure += 1
            mb.beat = i % 4 + 1
            i += 1

    def convert(self) -> list[LNote]:
        def to_LNote(note: Note) -> LNote:
            return LNote(note.time.to_time(self.tempo), note.dur * 60/self.tempo, note.pitch, note.dyn, note.inst)
        out = []
        for note in self.bassline:
            out.append(to_LNote(note))
        for note in self.harmony:
            out.append(to_LNote(note))
        for note in self.melody:
            out.append(to_LNote(note))
        return out

    def __str__(self):
        return "\n".join(map(str, self.notes)) + "\n"
