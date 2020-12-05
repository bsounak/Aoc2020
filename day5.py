from math import floor, ceil
import aoc_data

data = aoc_data.load(5).rstrip(b"\n").split(b"\n")
data = [v.decode("utf-8") for v in data]
#data = ["FBFBBFFRLR", "BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]


def bsp(scode:str, low:str, up:str, start:int, end:int):
    """
    Binary space partioning
    """
    for v in scode:
        if v == low:
            end = floor((start + end) / 2)
        if v == up:
            start = ceil((start + end) / 2)
    return min(start, end)


sids = []  # seat ids
for v in data:
    sids.append(
        bsp(v[:-3], low="F", up="B", start=0, end=127) * 8
        + bsp(v[-3:], low="L", up="R", start=0, end=7)
    )
print(max(sids))

# part 2
# Every id in the list should be consecutive integers when sorted.
sids = sorted(sids)
for n in range(len(sids)-1):
    if abs(sids[n]-sids[n+1]) > 1:
        print(sids[n], sids[n+1])
