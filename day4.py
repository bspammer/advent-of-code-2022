def intersects(line):
    lowLeft, highLeft = map(int, line.split(",")[0].split("-"))
    lowRight, highRight = map(int, line.split(",")[1].split("-"))

    return len(set(range(lowLeft, highLeft+1)).intersection(set(range(lowRight, highRight+1)))) > 0

with open("input.txt") as f:
    lines = f.read()[:-1].split("\n")
    print(sum(intersects(line) for line in lines))
