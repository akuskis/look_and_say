class Sequence:
    def __init__(self, sequence: str, evolve_into: [int]):
        self.sequence = sequence
        self.evolve_into = evolve_into


# according to Cosmological Theorem (https://mathworld.wolfram.com/CosmologicalTheorem.html)
SEQUENCES = [Sequence("", [93]),
             Sequence("1112", [63]),
             Sequence("1112133", [64, 62]),
             Sequence("111213322112", [65]),
             Sequence("111213322113", [66]),
             Sequence("1113", [68]),
             Sequence("11131", [69]),
             Sequence("111311222112", [84, 55]),
             Sequence("111312", [70]),
             Sequence("11131221", [71]),
             Sequence("1113122112", [76]),
             Sequence("1113122113", [77]),
             Sequence("11131221131112", [82]),
             Sequence("111312211312", [78]),
             Sequence("11131221131211", [79]),
             Sequence("111312211312113211", [80]),
             Sequence("111312211312113221133211322112211213322112", [81, 29, 91]),
             Sequence("111312211312113221133211322112211213322113", [81, 29, 90]),
             Sequence("11131221131211322113322112", [81, 30]),
             Sequence("11131221133112", [75, 29, 92]),
             Sequence("1113122113322113111221131221", [75, 32]),
             Sequence("11131221222112", [72]),
             Sequence("111312212221121123222112", [73]),
             Sequence("111312212221121123222113", [74]),
             Sequence("11132", [83]),
             Sequence("1113222", [86]),
             Sequence("1113222112", [87]),
             Sequence("1113222113", [88]),
             Sequence("11133112", [89, 92]),
             Sequence("12", [1]),
             Sequence("123222112", [3]),
             Sequence("123222113", [4]),
             Sequence("12322211331222113112211", [2, 61, 29, 85]),
             Sequence("13", [5]),
             Sequence("131112", [28]),
             Sequence("13112221133211322112211213322112", [24, 33, 61, 29, 91]),
             Sequence("13112221133211322112211213322113", [24, 33, 61, 29, 90]),
             Sequence("13122112", [7]),
             Sequence("132", [8]),
             Sequence("13211", [9]),
             Sequence("132112", [10]),
             Sequence("1321122112", [21]),
             Sequence("132112211213322112", [22]),
             Sequence("132112211213322113", [23]),
             Sequence("132113", [11]),
             Sequence("1321131112", [19]),
             Sequence("13211312", [12]),
             Sequence("1321132", [13]),
             Sequence("13211321", [14]),
             Sequence("132113212221", [15]),
             Sequence("13211321222113222112", [18]),
             Sequence("1321132122211322212221121123222112", [16]),
             Sequence("1321132122211322212221121123222113", [17]),
             Sequence("13211322211312113211", [20]),
             Sequence("1321133112", [6, 61, 29, 92]),
             Sequence("1322112", [26]),
             Sequence("1322113", [27]),
             Sequence("13221133112", [25, 29, 92]),
             Sequence("1322113312211", [25, 29, 67]),
             Sequence("132211331222113112211", [25, 29, 85]),
             Sequence("13221133122211332", [25, 29, 68, 61, 29, 89]),
             Sequence("22", [61]),
             Sequence("3", [33]),
             Sequence("3112", [40]),
             Sequence("3112112", [41]),
             Sequence("31121123222112", [42]),
             Sequence("31121123222113", [43]),
             Sequence("3112221", [38, 39]),
             Sequence("3113", [44]),
             Sequence("311311", [48]),
             Sequence("31131112", [54]),
             Sequence("3113112211", [49]),
             Sequence("3113112211322112", [50]),
             Sequence("3113112211322112211213322112", [51]),
             Sequence("3113112211322112211213322113", [52]),
             Sequence("311311222", [47, 38]),
             Sequence("311311222112", [47, 55]),
             Sequence("311311222113", [47, 56]),
             Sequence("3113112221131112", [47, 57]),
             Sequence("311311222113111221", [47, 58]),
             Sequence("311311222113111221131221", [47, 59]),
             Sequence("31131122211311122113222", [47, 60]),
             Sequence("3113112221133112", [47, 33, 61, 29, 92]),
             Sequence("311312", [45]),
             Sequence("31132", [46]),
             Sequence("311322113212221", [53]),
             Sequence("311332", [38, 29, 89]),
             Sequence("3113322112", [38, 30]),
             Sequence("3113322113", [38, 31]),
             Sequence("312", [34]),
             Sequence("312211322212221121123222113", [36]),
             Sequence("312211322212221121123222112", [35]),
             Sequence("32112", [37]),
             Sequence("1", [94]),
             Sequence("11", [95]),
             Sequence("21", [96]),
             Sequence("1211", [97]),
             Sequence("111221", [98]),
             Sequence("312211", [99]),
             Sequence("13112221", [100]),
             Sequence("1113213211", [83, 9]),
             ]


def __get_indices(sequence_number: int) -> [int]:
    indices = [0]
    for _ in range(sequence_number):
        indices = [evolve_index for index in indices for evolve_index in SEQUENCES[index].evolve_into]
    return indices


def get_length_of_sequence(sequence_number: int) -> int:
    indices = __get_indices(sequence_number)
    return sum([len(SEQUENCES[index].sequence) for index in indices])


def get_sequence(sequence_number: int) -> str:
    indices = __get_indices(sequence_number)
    return ''.join([SEQUENCES[index].sequence for index in indices])
