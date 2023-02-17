import math

with open("2022/input.txt") as f:
    nums = [list(map(int, (line.split()))) for line in f.read().split("\n\n")]

sums = [math.fsum(elem) for elem in nums]
print(max(sums))

sums.sort(reverse=True)
print(math.fsum(sums[:3]))

