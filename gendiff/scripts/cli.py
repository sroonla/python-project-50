import argparse

from gendiff import generate_diff


def parse_args():
    parser = argparse.ArgumentParser(
        description='Generate diff'
    )
    parser.add_argument('first_file', help='path to first file')
    parser.add_argument('second_file', help='path to second file')
    parser.add_argument(
        '--format',
        '-f',
        metavar='FORMAT_NAME',
        default='stylish',
        help="output format (default: 'stylish')"
    )
    return parser.parse_args()


def main():
    args = parse_args()
    diff = generate_diff(
        args.first_file,
        args.second_file,
        format_name=args.format
    )
    print(diff)


if __name__ == '__main__':
    main()
