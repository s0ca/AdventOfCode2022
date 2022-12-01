X = [l.strip() for l in open ('1.txt')]
FAT = []
for elf in ('\n'.join(X)).split('\n\n'):
    fat = 0
    for x in elf.split('\n'):
        fat += int(x)
    FAT.append(fat)
print(max(FAT))
