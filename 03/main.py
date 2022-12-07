import argparse


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


def main() -> None:
    args = parse_cli_args().parse_args()

    total = 0
    with open(args.file, "r") as input:
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
    
    print(total)


if __name__ == "__main__":
    main()