from shlex import join

with open("day3_data.txt") as f:
    rucksacks = f.read().split()


def divide_rucksack(rucksack: str) -> list:
    divided_rucksack = [
        rucksack[:int(len(rucksack)/2)],
        rucksack[int(len(rucksack)/2):]
    ]
    return divided_rucksack


def find_common_element(divided_rucksack: list) -> str:
    common_element = join(set.intersection(*map(set, divided_rucksack)))
    return common_element


def element_priority(element: str) -> int:
    search_string = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return search_string.index(element) + 1


priorities = [element_priority(find_common_element(divide_rucksack(rucksack))) for rucksack in rucksacks]
print(sum(priorities))


elves_groups = [rucksacks[elves:elves+3] for elves in range(0, len(rucksacks), 3)]
group_priorities = [element_priority(find_common_element(group)) for group in elves_groups]
print(sum(group_priorities))
