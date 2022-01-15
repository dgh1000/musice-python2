from scamp import *
from .Note import Note
from .Motive2 import Motive2

def play(part, notes):
    assert(len(notes) > 0)
    ns = sorted(notes, key = lambda n1: n1.time)
    ts = [no.time for no in ns]
    t_prev = ts[0]
    i = 0
    while i < len(notes):
        t_next = ts[i]
        wait(t_next-t_prev)
        while i < len(notes) and notes[i].time == t_next:
            part.play_note(notes[i].pitch, notes[i].dur, notes[i].dyn, blocking=False)
            i += 1
        t_prev = t_next
    wait(2)
    
    



