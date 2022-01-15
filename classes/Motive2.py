from .Note import *

class Motive2:

    def __init__(self, durs, spans, pitches, dyns):
        self.pitches = pitches
        self.durs = durs
        self.spans = spans
        self.dyns = dyns

    def dur(self):
        return sum(self.spans)

    def render(self, t):
        output = []
        tt = t
        for d, s, p, dyn in zip(self.durs, self.spans, self.pitches, self.dyns):
            output.append(Note(tt, d, p, dyn))
            tt += s
        return output

