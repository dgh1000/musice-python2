from scamp import *
from .Note import Note
from .Motive2 import Motive2
from .Chord2 import Chord2


def chord_to_notes(chord: Chord2, time: float, dur: float = 1, dyn: float = 1) -> list[Note]:
    return [Note(time, dur, chord.bass_note, dyn, "Electric Bass (finger)")]

def create_part_dict(session: Session, notes: list[Note], part_config) -> dict[str, ScampInstrument]:
    out = {}
    instr_names = {n.inst for n in notes}
    for i in instr_names:
        out[i] = session.new_midi_part(i, "MidiPipe Input 1", start_channel=part_config[i]-1, num_channels=1)
    return out

def num_to_pitch(num: int) -> str:
    # TODO: Decide whether to make something sharp/flat
    return ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"][num % 12] + str(num//12 - 1)

def P(pitch: str) -> int:
    return ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"].index(pitch[:-1]) + (12 * (1+int(pitch[-1])))

def nearest_pc(approx, pc):
    trunc = approx//12
    # approx % 12 - pc
    lis = [(trunc + x) * 12 + pc for x in range(-1, 2)]
    return min(lis, key=lambda x: abs(x-approx))

def nearest_from_multiple_pc(approx, pcs):
    lis = [nearest_pc(approx, pc) for pc in pcs]
    return min(lis, key=lambda x: abs(x-approx))


def interp_limit(x1: float, x2: float, x3: float, y1: float, y2: float) -> float:
    if (x2 < x1): return y1
    if (x2 > x3): return y2
    return y1 + (y2-y1)*(x2-x1)/(x3-x1)

def interp(x1: float, x2: float, x3: float, y1: float, y2: float) -> float:
    return y1 + (y2-y1)*(x2-x1)/(x3-x1)


    

