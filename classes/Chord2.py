class Chord2:
    def __init__(self, bass_note: int, pitch_classes: list[int], harmonies: list[int], melody_range: tuple[int, int]) -> None:
        self.bass_note = bass_note
        self.pitch_classes = pitch_classes
        self.harmonies = harmonies
        self.melody_range = melody_range

    