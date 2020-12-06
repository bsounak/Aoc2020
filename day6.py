import time
import aoc_data

data = aoc_data.load(6).rstrip(b"\n").split(b"\n\n")
data = [v.decode("utf-8") for v in data]

start = time.time()

count = 0
for v in data:
    v = "".join(v.split("\n"))
    count += len(set(v))
print(count)

# part 2
count = 0
for v in data:
    v = v.split("\n")
    count += len(set.intersection(*[set(i) for i in v]))
print(count)

end = time.time()
print("time: ", end-start)

