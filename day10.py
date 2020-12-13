import time
import aoc_data

data = aoc_data.load(10).rstrip(b"\n").split(b"\n")
data = [int(v) for v in data]

start = time.time()

sdata = sorted(data)
sdata.insert(0, 0)
sdata.append(sdata[-1] + 3)


# part 1
a = 0
b = 0
for i in range(len(sdata) - 1):
    if sdata[i + 1] - sdata[i] == 1:
        a += 1
    if sdata[i + 1] - sdata[i] == 3:
        b += 1

print(a * b)


# part 2
nway_cache = {}


def nway(n: int):
    """
    Number of ways to complete the adapter from adapter n
    """
    if n == sdata[-1]:
        return 1
    if n in nway_cache:
        return nway_cache[n]

    s = 0
    for v in range(n + 1, n + 4):
        if v in sdata:
            s += nway(v)

    if not n in nway_cache:
        nway_cache[n] = s
    return s

print(nway(0))

end = time.time()
print("time: ", end-start)
