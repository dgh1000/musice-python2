class Note:
    def __init__(self, time, dur, pitch, dyn):
        self.time = time
        self.dur = dur
        self.pitch = pitch
        self.dyn = dyn
    
    def play(self, part):
        part.play_note(self.pitch, self.dyn, self.dur)

    def to_list(self):
        return [self.time, self.dur, self.pitch, self.dyn]

    def __repr__(self):
        return "<{0}, {1}, {2}, {3}>".format(self.time, self.dur, self.pitch, self.dyn)