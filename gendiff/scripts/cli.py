import argparse
from gendiff.generate_diff import generate_diff


def parse_args():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    return parser.parse_args()


def main():
    args = parse_args()
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)
