with open("day6_data.txt") as f:
    signal = f.read()

number_of_unique_characters = 14


def check_unique(sequence: str) -> bool:
    return len(set(sequence)) == len(sequence)


def get_signal_slice(seq_start: int, seq_end: int) -> str:
    signal_slice = signal[seq_start:seq_end]
    return signal_slice


def main(sequence_start=0, sequence_end=number_of_unique_characters) -> int:
    for x in range(0, len(signal), 1):
        result = check_unique(get_signal_slice(seq_start=sequence_start, seq_end=sequence_end))
        if result:
            return sequence_end
        else:
            sequence_start += 1
            sequence_end += 1


print(main())
