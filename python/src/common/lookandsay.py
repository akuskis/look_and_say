def get_length_of_sequence(sequence_number: int) -> int:
    return len(get_sequence(sequence_number))


def get_sequence(sequence_number: int) -> str:
    sequence = [1]
    for _ in range(sequence_number - 1):
        temporary = []
        c = sequence[0]
        count = 0

        def store():
            temporary.append(count)
            temporary.append(c)

        for seq_char in sequence:
            if c != seq_char:
                store()
                c = seq_char
                count = 0
            count += 1

        store()
        sequence = temporary

    return ''.join(map(str, sequence))
