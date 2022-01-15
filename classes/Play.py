from scamp import *
from .Note import Note
from .Motive2 import Motive2
from .Chord2 import Chord2

def play(part_dict, notes):
    assert(len(notes) > 0)
    ns = sorted(notes, key = lambda n1: n1.time)
    ts = [no.time for no in ns]
    t_prev = ts[0]
    i = 0
    while i < len(notes):
        t_next = ts[i]
        wait(t_next-t_prev)
        while i < len(notes) and notes[i].time == t_next:
            part = part_dict[notes[i].inst]
            part.play_note(notes[i].pitch, notes[i].dur, notes[i].dyn, blocking=False)
            i += 1
        t_prev = t_next
    wait(2)
    
    
def chord_to_notes(chord: Chord2, time: float, dur: float = 1, dyn: float = 1) -> list[Note]:
    return [Note(time, dur, chord.bass_note, dyn, "Electric Bass (finger)")]

def create_part_dict(session, notes):
    s = {n.inst for n in notes}
    return {inst: session.new_part(inst) for inst in s}


