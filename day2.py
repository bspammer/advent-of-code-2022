scores = {
    "A X": 3 + 1,
    "A Y": 6 + 2,
    "A Z": 0 + 3,
    "B X": 0 + 1,
    "B Y": 3 + 2,
    "B Z": 6 + 3,
    "C X": 6 + 1,
    "C Y": 0 + 2,
    "C Z": 3 + 3,
}

choice = {
    "A X": " Z",
    "A Y": " X",
    "A Z": " Y",
    "B X": " X",
    "B Y": " Y",
    "B Z": " Z",
    "C X": " Y",
    "C Y": " Z",
    "C Z": " X",
}

with open("input.txt") as f:
    print(sum(scores[line[0] + choice[line]] for line in f.read()[:-1].split("\n")))
