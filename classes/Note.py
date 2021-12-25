class Note:
    def __init__(self, time, dur, pitch, dyn):
        self.time = time
        self.dur = dur
        self.pitch = pitch
        self.dyn = dyn
    
    def play(self, part):
        part.play_note(self.pitch, self.dyn, self.dur)


