from scamp import *
s = Session(tempo=120)
s.print_default_soundfont_presets()
clarinet = s.new_part("trumpet")
pitches = [60, 61, 68, 75, 76]
durs = [0.5, 0.5, 1.0, 0.5, 0.5]
for p, d in zip(pitches, durs):
    clarinet.play_note(p, 0.8, d)
pitches = [60, 61, 68, 69, 75, 76]
durs = [0.5, 0.5, 1.0, 0.5, 0.5, 0.5]
for p, d in zip(pitches, durs):
    clarinet.play_note(p, 0.8, d)
