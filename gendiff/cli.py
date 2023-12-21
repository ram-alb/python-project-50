"""Parse command-line arguments."""

import argparse


def parse_cli_args():
    """
    Parse command line arguments.

    Returns:
        argparse.Namespace object with cli arguments
    """
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.',
    )
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument(
        '-f',
        '--format',
        type=str,
        help='set format of output',
        default='stylish',
    )
    return parser.parse_args()
