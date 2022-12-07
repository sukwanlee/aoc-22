import argparse
from enum import Enum


class HandSymbol(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

    def __gt__(self, other) -> bool:
        if self.__class__ is other.__class__:
            if self is HandSymbol.ROCK:
                return other is HandSymbol.SCISSORS
            elif self is HandSymbol.PAPER:
                return other is HandSymbol.ROCK
            else:
                return other is HandSymbol.PAPER


def parse_cli_args() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    return parser


def main() -> None:
    args = parse_cli_args().parse_args()

    symbol_map = {
        "A": HandSymbol.ROCK,
        "B": HandSymbol.PAPER,
        "C": HandSymbol.SCISSORS,
        "X": HandSymbol.ROCK,
        "Y": HandSymbol.PAPER,
        "Z": HandSymbol.SCISSORS,
    }

    score = 0

    with open(args.file, "r") as input:
        for line in input:
            opponent = symbol_map[line[0]]
            me = symbol_map[line[2]]

            score += me.value
            if me is opponent:
                score += 3
            elif me > opponent:
                score += 6
    
    print(score)



if __name__ == "__main__":
    main()