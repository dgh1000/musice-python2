from typing import Tuple
from classes.Chord2 import Chord2
from classes.Hole import Hole
from classes.LNote import LNote
from classes.MeasureBeat import MeasureBeat
from classes.Note import Note
from classes.Scoring import Scoring
from classes.util import P, nearest_from_multiple_pc, num_to_pitch


class Comp:
    def __init__(self, chord_list: Tuple[MeasureBeat, Chord2], num_msrs, time_sig_map: dict[int, Tuple[int, int]] = {}, tempo_map: dict[int, float] = {}) -> None:
        self.num_msrs = num_msrs
        self.chord_list = chord_list
        self.bassline = []
        self.harmony = []
        self.melody = []
        self.time_sig_map = time_sig_map
        self.tempo_map = tempo_map
        self.time_map = Comp.create_time_map(time_sig_map, tempo_map)

    @staticmethod
    def create_time_map(time_sig_map, tempo_map) -> dict[int, float]:
        t = 0
        out = {1: t}
        for i in range(len(time_sig_map)):
            tempo = tempo_map[i + 1]
            num_beats = time_sig_map[i + 1][0]
            t += num_beats * 60 / tempo
            out[i + 2] = t
        return out

    def gen_bass(self):
        dur = self.time_sig[0]
        # dur = self.time_sig[0]* 60/self.tempo
        # for i in range(len(self.chord_list)):
        #     mb = MeasureBeat(i+1, 1, self.time_sig)
        #     self.bassline.append(
        #         Note(mb, dur, self.chord_list[i].bass_note, 0.7, "bass"))
        for mb, chord in self.chord_list:
            self.bassline.append(Note(mb, dur, chord.bass_note, 0.7, "bass"))

    def gen_harmony(self):
        # dur = self.time_sig[0]* 60/self.tempo
        lower = P("C3");
        upper = P("G4");
        # for i in range(len(self.chord_list)):
        #     mb = MeasureBeat(i+1, 1, self.time_sig)
        #     pcs = self.chord_list[i].pitch_classes
        #     for approx_pitch in range(lower, upper, 3):
        #         pitch = nearest_from_multiple_pc(approx_pitch, pcs)
        #         self.harmony.append(
        #             Note(mb, self.time_sig[0], pitch, 0.7, "harmony"))
        for i in range(len(self.chord_list)):
            print("------------------")
            for approx_pitch in range(lower, upper, 3):
                pitch = nearest_from_multiple_pc(approx_pitch, self.chord_list[i][1].pitch_classes)
                #print(num_to_pitch(pitch))
                if i == len(self.chord_list) - 1:
                    dur = MeasureBeat(self.num_msrs + 1, 1, self.time_sig) - self.chord_list[i][0]
                else:
                    dur = self.chord_list[i + 1][0] - self.chord_list[i][0]
                self.harmony.append(Note(self.chord_list[i][0], dur, pitch, 0.7, "harmony"))

    def gen_melody(self, scorer: Scoring, holes: list[Hole]):
        # mb = MeasureBeat(1, 1, self.time_sig)
        for i in range(len(holes)):
            # pick pitch here

            pit = scorer.ev(self, holes[i].time)
            print(num_to_pitch(pit))
            self.melody.append(Note(holes[i].time,
                                   holes[i].dur,
                                   pit,
                                   0.5, 
                                   "melody"))
            # print("gen_melody: " + str(self.melody[-1]))
            # if mb.beat > 0 and mb.beat % 4 == 0:
            #     mb.measure += 1
            # mb.beat = i % 4 + 1
            # i += 1

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

    def get_chord_at(self, mb: MeasureBeat) -> Chord2:
        if self.chord_list[0][0] > mb:
            raise Exception("error in get_chord_at") 
        for i in range(1, len(self.chord_list)):
            if self.chord_list[i][0] > mb:
                return self.chord_list[i - 1][1]
        return self.chord_list[-1][1]
        
    def to_time(self, mb: MeasureBeat) -> float:

    def __str__(self):
        return "\n".join(map(str, self.notes)) + "\n"
