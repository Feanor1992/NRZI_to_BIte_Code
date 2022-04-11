def nrzi(signal: str) -> str:
    high_signal = '¯'
    low_signal = '_'
    pipe_signal = '|'

    def give_bit(s):
        return str((0, 1)[s])

    bits = ''
    change_signal = False

    for token in signal:
        current_bit = give_bit(change_signal)

        if token == pipe_signal:
            change_signal = True
            continue
        else:
            change_signal = False

        bits += current_bit
    return bits


code = str(input())

print(nrzi(code))