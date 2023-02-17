def mapping(line):
    a = list(map(int, line.split('-')))
    return a


with open("day4_data.txt") as f:
    pairs = [list(map(mapping, line.split(','))) for line in f.read().split("\n")]


def single_elf_territory(elf: list) -> list:
    all_territory = [x for x in range(elf[0], elf[1] + 1, 1)]
    return all_territory


def pair_territory(pair: list) -> list:
    mutual = [single_elf_territory(elf) for elf in pair]
    return mutual


def pair_full_intersection(mutual_territory: list) -> int:
    check = all(item in mutual_territory[0] for item in mutual_territory[1])
    check_reversed = all(item in mutual_territory[1] for item in mutual_territory[0])

    if check or check_reversed:
        return 1
    else:
        return 0


def pair_partial_intersection(mutual_territory: list) -> int:
    check = any(item in mutual_territory[0] for item in mutual_territory[1])
    check_reversed = any(item in mutual_territory[1] for item in mutual_territory[0])

    if check or check_reversed:
        return 1
    else:
        return 0


full_intersections = [pair_full_intersection(pair_territory(pair)) for pair in pairs]
partial_intersections = [pair_partial_intersection(pair_territory(pair)) for pair in pairs]
print(sum(full_intersections))
print(sum(partial_intersections))
