from Note import *
from Motive2 import *
from scamp import *
from Play import play


motive1 = Motive2([1.0, 1.0], [1.0, 1.0], [60, 62], [0.5, 0.5])
notes = motive1.render(0)
s = Session()
o = s.new_part("trombone")
play(o, notes)
