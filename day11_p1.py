import time
import aoc_data
data = aoc_data.load(11).rstrip(b"\n").split(b"\n")
data = [v.decode("utf-8") for v in data]

start = time.time()

nrow = len(data)
ncol = len(data[0])

flips = None
while flips != 0:
    flips = 0
    result = data.copy()
    for i in range(nrow):
        for j in range(ncol):
            # for neighbor search
            sx = -1  # start x
            ex = 1  # end x
            sy = -1
            ey = 1

            if i == 0:
                sy = 0
            if j == 0:
                sx = 0
            if i == nrow-1:
                ey = 0
            if j == ncol-1:
                ex = 0

            v = data[i][j]
            ns = []  # hold the neighbor search outcomes
            if v == "L":
                for y in range(sy, ey+1):
                    for x in range(sx, ex+1):
                        if not (x == 0 and y == 0):
                            ns.append(data[i+y][j+x] == "#")
                if not any(ns):
                    nv = result[i][:j] + "#" + data[i][j+1:]
                    result[i] = nv
                    flips += 1

            elif v == "#":
                for y in range(sy, ey+1):
                    for x in range(sx, ex+1):
                        if not (x == 0 and y == 0):
                            ns.append(data[i+y][j+x] == "#")
                if sum(ns) >= 4:
                    nv = result[i][:j] + "L" + data[i][j+1:]
                    result[i] = nv
                    flips += 1
    data = result

os = 0  # occupied seats
for line in result:
    os += line.count("#")
print(os)

end = time.time()
print("time: ", end-start)
