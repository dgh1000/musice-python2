from scamp import *

s = Session()
p = s.new_midi_part("Piano", "MidiPipe Input 1")
p.play_note(60, 0.5, 1.0, blocking=True)
