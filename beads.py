"""
ID: benhua41
LANG: PYTHON3
TASK: beads
"""
fin = open('beads.in', 'r')
fout = open('beads.out', 'w')

lines = []
for line in fin:
    lines.append(line)

lines[0] = int(lines[0])

ll = lines[0]
i = lines[1]

c = 1
f = 0

# convert it to list
it = []
for a in range(0, ll):
    it.append(i[a])
jt = it[:]

nums = []
final = 0
temp = 0
isw = False
dotest = False
t = 1

# forward
for a in range(1, ll + 1):
    for b in range(0, ll - 1):
        if it[b] == 'w' and b == 0:
            isw = True
            dotest = True

        if isw == True:
            if t == 1:
                it[b] = 'r'
                t = t + 1
                # print("set r")

            elif t == 2:
                it[b] = 'b'
                t = t + 1
                # print("set p")

        if it[b] == it[b + 1] or it[b + 1] == 'w':
            c = c + 1
            it[b + 1] = it[b]
            print("inc c")
        if it[b] != it[b + 1] or b == ll - 2:
            print('b:',b)
            print(it)
            print("c:",c)
            nums.append(c)
            c = 1

        isw = False
    if it[0] == 'b' and dotest == True:
        isw = False
    if it[0] == 'r' and dotest == True:
        a = a - 1
        isw = True

        nums.append(0)
        print("ran r")
        print("0 added")
        it = jt[:]
        c = 1

        continue
    nums.append(0)
    print("0 added")

    it = jt[:]
    c = 1


    dotest = False
    t = 1
    it = it[a:] + it[0:a]

# find most one
print(nums)
for d in range(0, len(nums) - 1):
    temp = nums[d] + nums[d + 1]

    if temp > final:
        # print(nums[d], nums[d + 1])
        final = temp



final = str(final) + "\n"
fout.write(final)
fout.close()
