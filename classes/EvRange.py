from types import FunctionType
from .Ev import Ev
from .util import interp_limit
#          _
# f(mb): _/ \_
#          |
#


class EvRange(Ev):
    def __init__(self, get_pitch: FunctionType, width: float, bottom: float, top: float) -> None:
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


    def ev(self, comp, pitch, mb):
        target_pitch = self.get_pitch(mb)
        if target_pitch < pitch:
            return interp_limit(target_pitch, pitch, target_pitch + self.width, self.bottom, self.top)
        return interp_limit(target_pitch - self.width, pitch, target_pitch, self.bottom, self.top)
        
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

    