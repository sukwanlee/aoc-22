import argparse
from collections import defaultdict
import itertools


def parse_cli_args() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    return parser


def get_priority(char: str) -> int:
    ascii_val = ord(char)
    if ascii_val >= 65 and ascii_val <= 90:
        return ascii_val - 38
    else:
        return ascii_val - 96


def part_one(filename: str) -> None:
    total = 0
    with open(filename, "r") as input:
        for line in input:    
            line = line.rstrip()
            midpoint = int(len(line) / 2)
            first_compartment = line[:midpoint]
            second_compartment = line[midpoint:]

            items = set()
            for c in first_compartment:
                items.add(c)
            for c in second_compartment:
                if c in items:
                    total += get_priority(c)
                    break
    
    print(f"Part one: {total}")


def part_two(filename: str) -> None:
    total = 0

    with open(filename, "r") as input:
        for l1, l2, l3 in itertools.zip_longest(*[input]*3):
            counter = defaultdict(int)
            for l in [l1.rstrip(), l2.rstrip(), l3.rstrip()]:
                items = set()
                for c in l:
                    if c not in items:
                        items.add(c)
                        counter[c] += 1
                        if counter[c] == 3:
                            total += get_priority(c)
                            break
    
    print(f"Part two: {total}")



def main() -> None:
    args = parse_cli_args().parse_args()

    part_one(args.file)
    part_two(args.file)


if __name__ == "__main__":
    main()