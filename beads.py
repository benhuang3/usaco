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



# forward red
for a in range(1, ll + 1):
    for b in range(0, ll - 1):
        if it[b] == 'w' and b == 0:
            it[b] = 'r'

        if it[b] == it[b + 1] or it[b + 1] == 'w':
            c = c + 1
            it[b + 1] = it[b]
        if it[b] != it[b + 1] or b == ll - 2:
            nums.append(c)
            c = 1

    #print(it)
    nums.append(0)
    it = jt[:]
    c = 1

    it = it[a:] + it[0:a]

it = jt[:]
# forward blue
for a in range(1, ll + 1):
    for b in range(0, ll - 1):
        if it[b] == 'w' and b == 0:
            it[b] = 'b'

        if it[b] == it[b + 1] or it[b + 1] == 'w':
            c = c + 1
            it[b + 1] = it[b]
        if it[b] != it[b + 1] or b == ll - 2:
            nums.append(c)
            c = 1

    #print(it)
    nums.append(0)
    it = jt[:]
    c = 1

    it = it[a:] + it[0:a]

# find most one
#print(nums)
for d in range(0, len(nums) - 1):
    temp = nums[d] + nums[d + 1]

    if temp > final:
        # #print(nums[d], nums[d + 1])
        final = temp



final = str(final) + "\n"
fout.write(final)
fout.close()
