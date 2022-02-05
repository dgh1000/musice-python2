from classes.util import *
from classes.Chord2 import Chord2

# generate a contour: at eacgh point in the meldody we 
# have approx. pass that to our functions to get an actual pitch
# which we play

approx = 65
pcs = [0, 3, 7]
print(nearest_from_multiple_pc(approx, pcs))
