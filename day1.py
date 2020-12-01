import aoc_data
import time

data = aoc_data.load(1)

start = time.time()
min_val = min(data)
# remove the elements whose sum will always be larger than 2020 with any other
# element
data = [v for v in data if v+min_val <= 2020]

N = len(data)
for i in range(N):
    j = i+1
    for j in range(j, N):
        if data[i]+data[j] == 2020:
            print(i, j)
            print(data[i], data[j])
            print(data[i]*data[j])
            break

print("-------")
# part 2
niter = 0
N = len(data)
for i in range(N):
    j = i+1
    for j in range(j, N):
        if data[i]+data[j] < 2020:
            k = j+1
            for k in range(k, N):
                if data[i]+data[j]+data[k] == 2020:
                    print(i, j, k)
                    print(data[i], data[j], data[k])
                    print(data[i]*data[j]*data[k])
                    break
end = time.time()
print("time: ", end-start)
