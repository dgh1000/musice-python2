from typing import Tuple
from classes.Chord2 import Chord2
from classes.Hole import Hole
from classes.LNote import LNote
from classes.MeasureBeat import MeasureBeat
from classes.Note import Note
from classes.Scoring import Scoring
from classes.util import P, nearest_from_multiple_pc, num_to_pitch


class Comp:
    def __init__(self, chord_list: list[Tuple[MeasureBeat, Chord2]], num_msrs: int, time_sig_map: dict[int, Tuple[int, int]] = {}, tempo_map: dict[int, float] = {}) -> None:
        # self.num_msrs: length of composition. first measure is 1. last measure is num_msrs.
        # FINAL 'TIME' is MeasureBeat(num_msrs+1, 1)
        self.num_msrs = num_msrs
        self.chord_list = chord_list
        self.bassline = []
        self.harmony = []
        self.melody = []
        self.percussion = []
        # {1: (4, 4)}
        # {num_msrs: (4, 4)}
        self.time_sig_map = time_sig_map
        self.tempo_map = tempo_map
        # time_map: dict[int, float]: msr number & absolute time it begins
        # {1: 0.0, }  (measure 1 is mapped to zero)
        # {num_msrs: X} (there are an additional time_sig_map[num_msrs][0] beats before end of composition)
        # {num_msrs+1: Y}
        self.time_map = Comp.create_time_map(time_sig_map, tempo_map)

    @staticmethod
    def create_time_map(time_sig_map, tempo_map) -> dict[int, float]:
        t = 0
        out = {1: t}
        # 0 to num_msrs-1
        for i in range(len(time_sig_map)):
            # tempo is quarters per minutes
            tempo = tempo_map[i + 1]
            num_beats = time_sig_map[i + 1][0]
            t += num_beats * 60 * 4 / (tempo * time_sig_map[i + 1][1])
            # final entry in out is num_msrs+1
            out[i + 2] = t
        return out

    def gen_bass(self, holes: list[Hole]):

        # abstraction of a musical property : hole means a note or chord takes place
        # at a certain time and duration: all other details left unspecified
        #
        # a certain set of holes can have an experessive effect that can be understood
        #   even when the details aren't known
        # dynamics and rhythm can be close interlinked


        # for mb, chord in self.chord_list:
        #     self.bassline.append(Note(mb, self.time_sig_map[mb.measure][0], chord.bass_note, 0.7, "bass"))
        
        for hole in holes:
            # computing the pitch of the bassline: must check "floor" chord relative to
            # hole.time
            self.bassline.append(Note(hole.time, hole.dur, self.get_chord_at(hole.time).bass_note, 0.7, "bass"))

    def gen_harmony(self, holes: list[Hole]):
        lower = P("C3");
        upper = P("G4");
        for hole in holes:
            for approx_pitch in range(lower, upper, 3):
                pitch = nearest_from_multiple_pc(approx_pitch, self.get_chord_at(hole.time).pitch_classes)
                self.harmony.append(Note(hole.time, hole.dur, pitch, 0.7, "harmony"))

    def gen_melody(self, scorer: Scoring, holes: list[Hole]):
        for i in range(len(holes)):
            # pick pitch here
            pit = scorer.ev(self, holes[i].time)
            #print(scorer.evs[1].ev(self, pit, holes[i].time))
            print("Pitch, InChord, Range, Repeat", pit, [ev_.ev(self, pit, holes[i].time) for ev_ in scorer.evs])
            self.melody.append(Note(holes[i].time,
                                   holes[i].dur,
                                   pit,
                                   0.5, 
                                   "melody"))

    def gen_percussion(self, kick_holes: list[Hole], snare_holes: list[Hole], high_hat_holes: list[Hole]):
        for hole in kick_holes:
            self.percussion.append(Note(hole.time, hole.dur, 36, 0.7, "perc"))
        for hole in snare_holes:
            self.percussion.append(Note(hole.time, hole.dur, 38, 0.7, "perc"))
        for hole in high_hat_holes:
            self.percussion.append(Note(hole.time, hole.dur, 44, 0.7, "perc"))

    def convert(self) -> list[LNote]:
        def to_LNote(note: Note) -> LNote:
            time = self.to_time(note.time)
            end_time = self.to_time(self.add_mb_and_beat(note.time, note.dur))
            if (end_time <= time):
                print("time problem:", note, time, end_time)
            return LNote(time, end_time-time, note.pitch, note.dyn, note.inst)
        out = []
        for note in self.bassline:
            out.append(to_LNote(note))
        for note in self.harmony:
            out.append(to_LNote(note))
        for note in self.melody:
            out.append(to_LNote(note))
        for note in self.percussion:
            print("Perc note", note)
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
        begin = self.time_map[mb.measure]
        # beat is considered a 1/4
        # tempo is quarters per second
        # 3/4. tempo is 30.0. beat is 2
        # beat difference is 2-1 = 1
        # beat_diff * 60 * 4 / (tempo * denom)
        #
        # 3/8. tempo is 30.0 : 30.0 quarters per second
        #                60.0 eighths per second
        #
        if mb.measure == self.num_msrs + 1:
            return begin
        beat_diff = mb.beat - 1
        return begin + beat_diff * 240 / (self.tempo_map[mb.measure] * self.time_sig_map[mb.measure][1])

    def to_beat(self, mb: MeasureBeat) -> float:
        out = 0
        for i in range(1, mb.measure):
            out += self.time_sig_map[i][0]
        out += mb.beat
        return out

    def add_mb_and_beat(self, mb: MeasureBeat, diff: float) -> MeasureBeat:
        # out is return value after adding diff beats to mb. starts
        # at mb.measure and mb.beat
        out = MeasureBeat(mb.measure, mb.beat)
        while True:
            # 4/4: 1, 2, 3, 4 -> 4.999999 still inside the measure
            # loop invariant: diff is remaining beats to add
            if (diff <= 0.001): 
                break
            # num_beats is number of beats in out.measure:
            # t
            num_beats = self.time_sig_map[out.measure][0]
            # here we check if we just can't add 'diff'
            if out.beat + diff >  num_beats + 1.0:
                out.measure += 1
                out.beat = 1
                diff -= num_beats - (out.beat - 1) # num_beats left in measure
            else:
                out.beat += diff
                break
        return out

    def __str__(self):
        return "\n".join(map(str, self.notes)) + "\n"
