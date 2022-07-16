from classes.MeasureBeat import MeasureBeat


class Note:
    # dur is in beats. time is measure beat
    def __init__(self, time: MeasureBeat, dur: float, pitch: int, dyn: float, inst: str):
        self.time = time
        self.dur = dur
        self.pitch = pitch
        self.dyn = dyn
        self.inst = inst
    
    '''
    def play(self, part_dict: dict):
        part = part_dict[self.inst]
        part.play_note(self.pitch, self.dyn, self.dur)
    '''

    def to_list(self):
        return [self.time, self.dur, self.pitch, self.dyn, self.inst]

    def __repr__(self):
        return "<{0}, {1}, {2}, {3}, {4}>".format(self.time, self.dur, self.pitch, self.dyn, self.inst)