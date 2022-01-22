class Chord2:
    def __init__(self, bass_note: int, pitch_classes: list[int], harmonies: list[int], melody_range: tuple[int, int]) -> None:
        self.bass_note = bass_note
        self.pitch_classes = pitch_classes
        self.harmonies = harmonies
        self.melody_range = melody_range

    @staticmethod
    def major_chord(root, mid_harm, mid_mel):
        pitch_classes = [root%12, (root+4)%12, (root+7)%12]
        # 11   3    6
        pitches = [root]
        for i in range(1, 6):
            pitches 
    
    @staticmethod
    def nearest_pitch_above_pc(pc, pitch):
        """Finds the first pitch above 'pitch' which has the pitch class 'pc'"""

        # pitch class is 1, pitch is 69, answer is 73%12 = 1
        # 69%12. 1 - 9 = -8 . +12 = 4
