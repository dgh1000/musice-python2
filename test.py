from scamp import *

s = Session()
p1 = s.new_midi_part("Bass", "MidiPipe Input 1", start_channel=0, num_channels=1)
p2 = s.new_midi_part("Sax", "MidiPipe Input 1", start_channel=1, num_channels=1)
p3 = s.new_midi_part("Trumpets", "MidiPipe Input 1", start_channel=2, num_channels=1)
p1.play_note(48, 1.0, 1.0, blocking=False)
p2.play_note(64, 1.0, 1.0, blocking=False)
p3.play_note(79, 1.0, 1.0, blocking=False)
wait(1.0)
