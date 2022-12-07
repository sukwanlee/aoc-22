import argparse

from decimal import Decimal


def parse_cli_args() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    return parser


def main() -> None:
    args = parse_cli_args().parse_args()

    max_cals = 0
    current_cals = 0

    with open(args.file, "r") as input:
        for line in input:
            if line == "\n":
                max_cals = max(max_cals, current_cals)
                current_cals = 0
            else:
                current_cals += Decimal(line)
        
    max_cals = max(max_cals, current_cals)
    print(max_cals)


if __name__ == "__main__":
    main()