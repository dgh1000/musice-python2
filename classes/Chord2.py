


class Chord2:
    # def __init__(self, bass_note: int, pitch_classes: list[int], harmonies: list[int], melody_range: tuple[int, int]) -> None:
    #     self.bass_note = bass_note
    #     self.pitch_classes = pitch_classes
    #     self.harmonies = harmonies
    #     self.melody_range = melody_range
    def __init__(self, notation) -> None:
        root, idx = Chord2.pc_parser(notation, 0)
        is_minor = False
        if idx < len(notation) and notation[idx] == "m":
            is_minor = True
            idx += 1
        is_seven = False
        if idx < len(notation) and notation[idx] == "7":
            is_seven = True
            idx += 1
        
        if idx >= len(notation) or notation[idx] != "/":
            raise Exception("Expecting / in Chord2 constructor")
        idx += 1
        self.bass_note, idx = Chord2.pc_parser(notation, idx)
        if idx >= len(notation) or not notation[idx].isdigit():
            raise Exception("Expecting digit in Chord2 constructor")
        octave = int(notation[idx])
        
        self.bass_note += (octave + 1) * 12
        if is_minor:
            if is_seven:
                rel_pc = [0, 3, 7, 9]
            else:
                rel_pc = [0, 3, 7]
        else:
            if is_seven:
                rel_pc = [0, 4, 7, 9]
            else:
                rel_pc = [0, 4, 7]
        self.pitch_classes = sorted([(root + p) % 12 for p in rel_pc])
        
        # Bb??/Db?d
        # 
    @staticmethod
    def pc_parser(notation, idx):
        """Find D, Eb, etc. No number, no minor m

            Aware of difference between pitch class and pitch
        """
        d = {"C": 0, "D": 2, "E": 4, "F": 5, "G": 7, "A": 9, "B": 11}
        if (idx >= len(notation)):
            raise Exception("string ran out in pc_parser in Chord2")
        if notation[idx] not in d:
            raise Exception("Invalid note in pc_parser in Chord2")
        val = d[notation[idx]]
        alter = 0
        shift = 1
        if len(notation) >= idx:
            if notation[idx + 1] == "#":
                alter = 1
                shift = 2
            elif notation[idx + 1] == "b":
                alter = -1
                shift = 2
        return ((val + alter) % 12, shift + idx)


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

if __name__ == "__main__":
    test = Chord2("C#m7/E4")
    print(test.bass_note)
    print(test.pitch_classes)