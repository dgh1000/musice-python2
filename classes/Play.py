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
        print("i", i, "t_next", t_next, "t_prev", t_prev)
        wait(t_next-t_prev)
        while i < len(notes) and ns[i].time == t_next:
            part = part_dict[ns[i].inst]
            part.play_note(ns[i].pitch, ns[i].dyn, ns[i].dur, blocking=False)
            i += 1
        t_prev = t_next
    wait(2)
    
    



