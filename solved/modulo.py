mods = []
for i in range(10):
    mods.append(int(input()))
i = 0
while(i < len(mods) and len(mods) > 0):
    curr = mods[i]
    ix = i + 1
    while(ix < len(mods)):
        if((curr % 42) == (mods[ix] % 42)):
            if(len(mods) != 0):
                mods.pop(ix)
                ix -= 1
        ix += 1
    i += 1
print(len(mods))