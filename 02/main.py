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
        # "X": HandSymbol.ROCK,
        # "Y": HandSymbol.PAPER,
        # "Z": HandSymbol.SCISSORS,
    }

    get_winning_symbol = {
        HandSymbol.ROCK: HandSymbol.PAPER,
        HandSymbol.PAPER: HandSymbol.SCISSORS,
        HandSymbol.SCISSORS: HandSymbol.ROCK,
    }

    get_losing_symbol = {
        HandSymbol.ROCK: HandSymbol.SCISSORS,
        HandSymbol.PAPER: HandSymbol.ROCK,
        HandSymbol.SCISSORS: HandSymbol.PAPER,
    }

    score = 0

    with open(args.file, "r") as input:
        for line in input:
            opponent = symbol_map[line[0]]

            # X: lose
            # Y: draw
            # Z: win
            directive = line[2]
            if directive == "X":
                me = get_losing_symbol[opponent]
            elif directive == "Z":
                me = get_winning_symbol[opponent]
            else:
                me = opponent

            score += me.value
            if me is opponent:
                score += 3
            elif me > opponent:
                score += 6
    
    print(score)



if __name__ == "__main__":
    main()