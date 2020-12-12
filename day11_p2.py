import time
from sys import exit
import aoc_data

data = aoc_data.load(11).rstrip(b"\n").split(b"\n")
data = [v.decode("utf-8") for v in data]

start = time.time()

nrow = len(data)
ncol = len(data[0])

# Empty seat that see no occupied seat become occupied.
# It now takes five or more visible occupied seats for an occupied seat to
# become empty.

flips = None
while flips != 0:
    flips = 0
    result = data.copy()

    for i in range(nrow):
        for j in range(ncol):

            v = data[i][j]

            if v != ".":
                # left diagonal
                ii, jj = i, j
                ds = []  # hold the line (love isn't always on time :D) of
                # sight search outcome

                # towards top-left
                while True:
                    ii -= 1
                    jj -= 1
                    if ii < 0 or jj < 0:
                        break
                    if data[ii][jj] != ".":
                        ds.append(data[ii][jj])
                        break
                # towards bottom-right
                ii, jj = i, j
                while True:
                    ii += 1
                    jj += 1
                    if ii == nrow or jj == ncol:
                        break
                    if data[ii][jj] != ".":
                        ds.append(data[ii][jj])
                        break

                # right diagonal
                ii, jj = i, j
                # towards top-right
                while True:
                    ii -= 1
                    jj += 1
                    if ii < 0 or jj == ncol:
                        break
                    if data[ii][jj] != ".":
                        ds.append(data[ii][jj])
                        break
                # towards bottom-left
                ii, jj = i, j
                while True:
                    ii += 1
                    jj -= 1
                    if ii == nrow or jj < 0:
                        break
                    if data[ii][jj] != ".":
                        ds.append(data[ii][jj])
                        break

                # up-down
                ii, jj = i, j
                # towards up
                while True:
                    ii -= 1
                    if ii < 0:
                        break
                    if data[ii][jj] != ".":
                        ds.append(data[ii][jj])
                        break
                # towards down
                ii, jj = i, j
                while True:
                    ii += 1
                    if ii == nrow:
                        break
                    if data[ii][jj] != ".":
                        ds.append(data[ii][jj])
                        break

                # sideways
                ii, jj = i, j
                # towards left
                while True:
                    jj -= 1
                    if jj < 0:
                        break
                    if data[ii][jj] != ".":
                        ds.append(data[ii][jj])
                        break
                # towards right
                ii, jj = i, j
                while True:
                    jj += 1
                    if jj == ncol:
                        break
                    if data[ii][jj] != ".":
                        ds.append(data[ii][jj])
                        break

                if v == "L":
                    if not "#" in ds:
                        nv = result[i][:j] + "#" + data[i][j + 1 :]
                        result[i] = nv
                        flips += 1

                if v == "#":
                    if ds.count(v) >= 5:
                        nv = result[i][:j] + "L" + data[i][j + 1 :]
                        result[i] = nv
                        flips += 1

    data = result


os = 0  # occupied seats
for line in result:
    os += line.count("#")
print(os)

end = time.time()
print("time: ", end-start)
