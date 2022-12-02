with open("input.txt") as f:
    print(sum(sorted(sum(map(int, items.split("\n"))) for items in f.read()[:-1].split("\n\n"))[-3:]))
