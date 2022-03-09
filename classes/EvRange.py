from .Ev import Ev
from .util import interp_limit
#          _
# f(mb): _/ \_
#          |
#


class InRange(Ev):
    def __init__(self, width, y0, y1, y2, mb0, mb1, mb2) -> None:
        super().__init__()
        # look at the measureBeat and
        # generate curve
        #
        # f(mb, curve over time)=> score is -100*abs(f(mb)-pitch)
        self.width = width
        self.y0 = y0
        self.y1 = y1
        self.y2 = y2
        self.mb0 = mb0
        self.mb1 = mb1
        self.mb2 = mb2

    def ev(self, comp, pitch, mb):
        # target pitch is function based on y0, .., y2, mb0, .. , mb2
        t_mb = mb.to_time()
        t_mb0 = self.mb0.to_time()
        t_mb1 = self.mb1.to_time()
        t_mb2 = self.mb2.to_time()
        if (t_mb < t_mb1):
            val = interp_limit(t_mb0, t_mb, t_mb1, self.y0, self.y1)
        else:
            val = interp_limit(t_mb1, t_mb, t_mb2, self.y1, self.y2)
        return -100 * abs(val - pitch)

        pass
