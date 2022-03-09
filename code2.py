from scamp import *

s = Session()
o = s.new_part("trombone")

o.play_chord([36, 52.11, 60], 0.8, 6.0, blocking=False)
ps = [60, 62.05, 64.11]
ds = [2.0, 2.0, 2.0]
for p, d in zip(ps, ds):
    o.play_note(p, 0.8, d)
    wait(1)

fp_cresc = Envelope.from_levels_and_durations([1.0, 0.2, .8], [0.1, 0.5])
fp_cresc.show_plot()
o.play_note(64.11, fp_cresc, 2.0, blocking=False)