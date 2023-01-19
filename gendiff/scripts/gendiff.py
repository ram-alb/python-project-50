"""Generate diff of two files."""

from gendiff.cli import parse_cli_args
from gendiff.gendiff import generate_diff


def main():
    """Generate diff of two files."""
    args = parse_cli_args()
    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == '__main__':
    main()
