from classes.Comp import Comp
from classes.MeasureBeat import MeasureBeat
from classes.Note import Note
from classes.Motive2 import Motive2
from classes.Scoring import Scoring
from scamp import *
from classes.Play import *
from classes.util import *
from classes.Chord2 import Chord2
from classes.EvInChord import EvInChord
from classes.EvRange import EvRange


session = Session()
bass = session.new_midi_part("bass", "MidiPipe Input 1", start_channel=0, num_channels=1)
melody = session.new_midi_part("melody", "MidiPipe Input 1", start_channel=1, num_channels=1)

bass.play_note(48, 0.5, 1, blocking=False)
melody.play_note(64, 0.5, 1, blocking=False)
wait(2)
