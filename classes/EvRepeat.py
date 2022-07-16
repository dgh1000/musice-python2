from classes.Ev import Ev


class EvRepeat(Ev):
    def __init__(self, num_backward) -> None:
        super().__init__()
        self.num_backward = num_backward

    def ev(self, comp, pitch, mb):
        for i in range(len(comp.melody)-1, -1, -1):
            #  4: 3 
            if i < len(comp.melody) - self.num_backward:
                break
            if comp.melody[i].pitch == pitch:
                return -1000000
        return 0

        # if len(comp.melody) and any(comp.melody[i].pitch == pitch for i in range(-1, -min(len(comp.melody), self.num_backward)-1, -1)):
        #     return -1000000
        # return 0
