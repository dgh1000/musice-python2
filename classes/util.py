def chord_to_notes(chord: Chord2, time: float, dur: float = 1, dyn: float = 1) -> list[Note]:
    return [Note(time, dur, chord.bass_note, dyn, "Electric Bass (finger)")]

def create_part_dict(session: Session, notes: list[Note]) -> dict[str, ScampInstrument]:
    s = {n.inst for n in notes}
    return {inst: session.new_part(inst) for inst in s}

def num_to_pitch(num: int) -> str:
    # TODO: Decide whether to make something sharp/flat
    return ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"][num % 12] + str(num//12 - 1)

def P(pitch: str) -> int:
    return ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"].index(pitch[:-1]) + (12 * (1+int(pitch[-1])))

def nearest_pc(approx, pc):
    o = approx//12
    approx % 12 - pc

    return o * 12 + pc