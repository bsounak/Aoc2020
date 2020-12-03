import time
import aoc_data

data = aoc_data.load(3).rstrip(b"\n").split(b"\n")
data = [v.decode("utf-8") for v in data]

#data = [
#"..##.......",
#"#...#...#..",
#".#....#..#.",
#"..#.#...#.#",
#".#...##..#.",
#"..#.##.....",
#".#.#.#....#",
#".#........#",
#"#.##...#...",
#"#...##....#",
#".#..#...#.#"
#]

nrow = len(data)
ncol = len(data[0])

def slope(rstep, cstep):
    i = rstep
    j = cstep
    count = 0
    for i in range(i, nrow, rstep):
        char = data[i][j % ncol]
        if char == "#":
            count+=1
        j+=cstep
    return count

a = slope(1, 1)
b = slope(1, 3)
c = slope(1, 5)
d = slope(1, 7)
e = slope(2, 1)

print(a, b, c, d, e)
print(a*b*c*d*e)
