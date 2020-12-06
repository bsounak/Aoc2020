import time
import aoc_data

data = aoc_data.load(6).rstrip(b"\n").split(b"\n\n")
data = [v.decode("utf-8") for v in data]

start = time.time()

count = 0
for v in data:
    count += len(set("".join(v.split("\n"))))
print(count)

# part 2
count = 0
for v in data:
    count += len(set.intersection(*[set(i) for i in v.split("\n")]))
print(count)

end = time.time()
print("time: ", end-start)

