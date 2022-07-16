from typing import Callable

from .MeasureBeat import MeasureBeat
from .Ev import Ev
from .util import interp_limit
#          _
# f(mb): _/ \_
#         | |
#         b t
#


class EvRange(Ev):
    def __init__(self, get_pitch: Callable[[float, float], float], width: float, bottom: float, top: float) -> None:
        super().__init__()
        self.get_pitch = get_pitch
        self.width = width
        self.bottom = bottom    
        self.top = top
        # look at the measureBeat and
        # generate curve
        #
        # f(mb, curve over time)=> score is -100*abs(f(mb)-pitch)
        # self.width = width
        # self.y0 = y0
        # self.y1 = y1
        # self.y2 = y2
        # self.mb0 = mb0
        # self.mb1 = mb1
        # self.mb2 = mb2
    #   _
    #  / \
    def ev(self, comp, pitch, mb):
        target_pitch = self.get_pitch(comp.to_time(mb), comp.to_time(MeasureBeat(comp.num_msrs, 1)))
        y1 = target_pitch - 24
        y2 = target_pitch + 24
        if y1 < pitch < y2:
            return self.top
        if target_pitch < y1:
            return interp_limit(y1, pitch, y1 + self.width, self.bottom, self.top)
        return interp_limit(y2 - self.width, pitch, y2, self.bottom, self.top)
        
        # target pitch is function based on y0, .., y2, mb0, .. , mb2
        # t_mb = mb.to_time()
        # t_mb0 = self.mb0.to_time()
        # t_mb1 = self.mb1.to_time()
        # t_mb2 = self.mb2.to_time()
        # if (t_mb < t_mb1):
        #     val = interp_limit(t_mb0, t_mb, t_mb1, self.y0, self.y1)
        # else:
        #     val = interp_limit(t_mb1, t_mb, t_mb2, self.y1, self.y2)
        # return -100 * abs(val - pitch)

        pass

    