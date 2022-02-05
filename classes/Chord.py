from .Note import Note

# eventually produce a piece with bassline, background chords and melody
# chord progression and a scale
# chord is very concrete : set of pitches which all sound
#
# in an actual piece,
# C3 G3 C4 E4
# ^ good in baseline
#     ^  ^  ^ sound good in trombone as a chord
# sax melody will have notes from C in it C5, E5, G5
#
# chord provides a bass note, some pitches to sustain, and pitches to choose
# a melody from. list of pitch classes (0 through 11) - name of the pitch
# without associated octave.
#
# pitch classes: which pitch class is the bass note and specific pitch
# range from whjich to draw the melody - any of the pitch classes that fall
# into a range of pitches


class Chord:
    def __init__(self, pitches: list[int]) -> None:
        self.pitches = pitches

    @staticmethod
    def major_chord(root: int, num_pitches: int):
        return Chord.abstract_chord([0, 4, 7], root, num_pitches)

    @staticmethod
    def minor_chord(root: int, num_pitches: int):
        return Chord.abstract_chord([0, 3, 7], root, num_pitches)

    @staticmethod
    def dom7(root: int, num_pitches: int):
        return Chord.abstract_chord([0, 4, 7, 10], root, num_pitches)

    @staticmethod
    def abstract_chord(deltas: list[int], root: int, num_pitches: int):
        return Chord([root + deltas[i % len(deltas)] + 12 * (i//len(deltas)) for i in range(num_pitches)])

    def to_notes(self, time: float, dur: float, dyn: float) -> list[int]:
        return [Note(time, dur, pitch, dyn) for pitch in self.pitches]
