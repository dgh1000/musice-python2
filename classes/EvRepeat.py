from classes.Ev import Ev


class EvRepeat(Ev):
    def __init__(self) -> None:
        super().__init__()

    def ev(self, comp, pitch, mb):
        if len(comp.melody) and comp.melody[-1].pitch == pitch:
            return -1000000
        return 0
