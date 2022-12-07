import argparse
import heapq

from decimal import Decimal


def parse_cli_args() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    return parser


def main() -> None:
    args = parse_cli_args().parse_args()

    max_cals = []
    current_cals = 0

    with open(args.file, "r") as input:
        for line in input:
            if line == "\n":
                heapq.heappush(max_cals, current_cals)
                if len(max_cals) > 3:
                    heapq.heappop(max_cals)
                current_cals = 0
            else:
                current_cals += Decimal(line)
        
    heapq.heappush(max_cals, current_cals)
    heapq.heappop(max_cals)
    print(sum(max_cals))


if __name__ == "__main__":
    main()