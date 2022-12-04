def priority(elf1, elf2, elf3):
    shared, = set(elf1).intersection(set(elf2)).intersection(set(elf3))
    return ord(shared) - ord('a') + 1 if not shared.isupper() else ord(shared) - ord('A') + 27


with open("input.txt") as f:
    lines = f.read()[:-1].split("\n")
    print(sum(priority(lines[i*3], lines[i*3+1], lines[i*3+2]) for i in range(int(len(lines)/3))))
