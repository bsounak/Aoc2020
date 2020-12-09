import time
import aoc_data

data = aoc_data.load(9).rstrip(b"\n").split(b"\n")
data = [int(v) for v in data]

start = time.time()

def valid(n: int, ln: list):
    for i in range(len(ln)):
        for j in range(i + 1, len(ln)):
            if n == ln[i] + ln[j]:
                return True
    return False


inv = None  # invalid number
# first 25 numbers are the preamble
for i in range(25, len(data)):
    if not valid(data[i], data[i - 25 : i]):
        inv = data[i]
        break
print(inv)

# part 2
for i in range(len(data)):
    s = data[i]
    cl = []  # keep a track of numbers that are being added
    cl.append(data[i])
    for j in range(i + 1, len(data)):
        cl.append(data[j])
        s += data[j]
        if s == inv:
            print(min(cl) + max(cl))
            break

end = time.time()
print("time:", end-start)
