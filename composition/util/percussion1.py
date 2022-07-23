from termios import TIOCM_DSR
from typing import Tuple
from classes.Hole import Hole
from classes.MeasureBeat import MeasureBeat


def gen_perc(length: int) -> Tuple[list[Hole]]:
    kick_holes: list[Hole] = []
    snare_holes: list[Hole] = []
    # 1, 2.5, 3.5, 4.5
    def g(tim, dyn):
        snare_holes.append(Hole(MeasureBeat(i, tim), 0.25, dyn))
    for i in range(1, length + 1):
        tds = [(1, 0.6), (2, 0.5), (3, 0.6), (4, 0.5), (4.5, 0.7), (4.625, 0.7), (4.750, 0.7), (4.875, 0.7)]
        for td in tds:
            g(*td)
        # snare_holes.append(Hole(MeasureBeat(i, 1), 0.25))
        # snare_holes.append(Hole(MeasureBeat(i, 2), 0.25))
        # snare_holes.append(Hole(MeasureBeat(i, 3), 0.25))
        # snare_holes.append(Hole(MeasureBeat(i, 4), 0.25))
        # snare_holes.append(Hole(MeasureBeat(i, 4.5), 0.25))
        # snare_holes.append(Hole(MeasureBeat(i, 4.625), 0.25))
        # snare_holes.append(Hole(MeasureBeat(i, 4.750), 0.25))
        # snare_holes.append(Hole(MeasureBeat(i, 4.875), 0.25))

    high_hat_holes: list[Hole] = []
    for i in range(1, length + 1):
        # 1, 2.5, 3.5, 4.5
        high_hat_holes.append(Hole(MeasureBeat(i, 1), 0.25))
        high_hat_holes.append(Hole(MeasureBeat(i, 2), 0.25))
        high_hat_holes.append(Hole(MeasureBeat(i, 2.667), 0.25))
        high_hat_holes.append(Hole(MeasureBeat(i, 3), 0.25))
        high_hat_holes.append(Hole(MeasureBeat(i, 4), 0.25))
        high_hat_holes.append(Hole(MeasureBeat(i, 4.667), 0.25))
    return (kick_holes, snare_holes, high_hat_holes)