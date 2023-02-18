def mapping(line):
    splitted_line = line.split()
    instruction = {
        'quantity': int(splitted_line[1]),
        'from': int(splitted_line[3]),
        'to': int(splitted_line[5])
    }
    return instruction


with open("day5_data.txt") as f:
    crates_in_stacks = [line.split(',') for line in f.read().split('\n')]

with open("day5_data_instructions.txt") as f:
    instructions = [mapping(line) for line in f.read().split("\n")]


def initial_setup_all_stacks(crates_in_stacks_raw: list) -> list:
    for crates in crates_in_stacks_raw:
        i = 1
        for crate in crates[0]:
            if (i % 4) == 0:
                crates[0] = crates[0][:i - 1] + ',' + crates[0][i:]
            i += 1

        crates[0] = crates[0].replace('   ', '[-]')
    modified_crates_in_stacks_raw = [crate[0].split(',') for crate in crates_in_stacks_raw]
    return modified_crates_in_stacks_raw


def initial_setup_by_stack(initial_setup_raw: list) -> list:
    initial_setup_raw.pop(-1)
    initial_setup_modified = []
    number_of_crates = len(initial_setup_raw[0])
    for x in range(0, number_of_crates, 1):
        single_crate = []
        for elem in initial_setup_raw:
            if elem[x] != '[-]':
                single_crate.append(elem[x])

        single_crate.reverse()
        initial_setup_modified.append(single_crate)
    return initial_setup_modified


def follow_instruction(instruction: dict, stacks: list) -> list:
    stack_from = stacks[instruction['from'] - 1]
    stack_to = stacks[instruction['to'] - 1]

    elements_to_move = stack_from[-instruction['quantity']:]
    # elements_to_move.reverse()  # uncomment for answer for part 1

    for crate in elements_to_move:
        stack_to.append(crate)

    del stack_from[-instruction['quantity']:]
    return stacks


crates_in_stacks_modified = initial_setup_by_stack(initial_setup_all_stacks(crates_in_stacks))

for instruction in instructions:
    crates_in_stacks_modified = follow_instruction(instruction=instruction, stacks=crates_in_stacks_modified)

for stack in crates_in_stacks_modified:
    print('After: ', stack[-1])
