import time
import aoc_data

data = aoc_data.load(8).rstrip(b"\n").split(b"\n")
data = [v.decode("utf-8") for v in data]

start = time.time()

def is_infinite_loop(data):
    acc = 0
    pc = 0
    exel = []  # executed list
    try:
        while True:
            if pc in exel:
                return True, acc

            exel.append(pc)
            op, val = data[pc].split()
            if op == "nop":
                pass
            if op == "acc":
                acc += int(val)
            if op == "jmp":
                pc += int(val)
                continue
            pc += 1
    except IndexError:
        return False, acc


for i, line in enumerate(data):
    if "nop" in line:
        data[i] = line.replace("nop", "jmp")
        a, b = is_infinite_loop(data)
        if not a:
            print(b)
            break
        data[i] = line

    if "jmp" in line:
        data[i] = line.replace("jmp", "nop")
        a, b = is_infinite_loop(data)
        if not a:
            print(b)
            break
        data[i] = line

end = time.time()
print("time:", end-start)
