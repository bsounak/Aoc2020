import time
import aoc_data

data = aoc_data.load(2).rstrip(b"\n").split(b"\n")
data = [v.decode("utf-8") for v in data]
#data = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]

start = time.time()

valid_pwds = []
for v in data:
    rule, letter, pwd = v.split()
    letter = letter[:-1]
    min_val, max_val = rule.split("-")
    if int(min_val) <= pwd.count(letter) <= int(max_val):
        valid_pwds.append(pwd)
print(len(valid_pwds))

# part 2
valid_pwds = []
for v in data:
    rule, letter, pwd = v.split()
    letter = letter[:-1]
    i, j = rule.split("-")
    # xor gate
    if((pwd[int(i)-1] == letter) != (pwd[int(j)-1] == letter)):
        valid_pwds.append(pwd)
print(len(valid_pwds))

end = time.time()
print("time: ", end-start)
