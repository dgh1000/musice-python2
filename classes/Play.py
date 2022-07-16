from scamp import * #type: ignore
from .LNote import LNote

def play(part_dict: dict[str, ScampInstrument], notes: list[LNote]) -> None: #type: ignore
    stretch = 2.0
    assert(len(notes) > 0)
    ns = sorted(notes, key = lambda n1: n1.time)
    ts = [no.time * stretch for no in ns]
    t_prev = ts[0]
    i = 0
    while i < len(notes):
        t_next = ts[i]
        print("i", i, "t_next", t_next, "t_prev", t_prev)
        wait(t_next-t_prev)
        while i < len(notes) and ns[i].time * stretch == t_next:
            part = part_dict[ns[i].inst]
            part.play_note(ns[i].pitch, ns[i].dyn, ns[i].dur * stretch, blocking=False)
            i += 1
        t_prev = t_next
    wait(2)
    
    
# Note: instr is "Bass", "Melody", or "Harmony"
# part dict is ["bass" : ScampPart,]
# config dict: we need another dict which is {"bass" : 1}
# going to use that set on Notes to get {"bass", "melody", }



