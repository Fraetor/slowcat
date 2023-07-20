#! /usr/bin/env python3

"""slowcat: Slowly read a file"""

import argparse
import sys
import time


def parse_args():
    """Parse CLI arguments"""
    parser = argparse.ArgumentParser(description="Read out a file one byte at a time.")
    parser.add_argument(
        "-r",
        "--rate",
        type=float,
        default=10.0,
        help="how many bytes to read per second (default: 10)",
    )
    parser.add_argument(
        "FILE",
        type=argparse.FileType("rb"),
        help="the file(s) to read; use - or omit for standard input",
        default=sys.stdin.buffer,
    )
    parser.add_argument(
        "--version",
        action="version",
        version="0.1.0",
        help="show version information and exit",
    )
    return parser.parse_args()


def main():
    """Program entry point"""
    args = parse_args()
    delay: float = 1.0 / args.rate
    byte: bytes = b"1"
    while byte:
        byte = args.FILE.read(1)
        sys.stdout.buffer.write(byte)
        sys.stdout.buffer.flush()
        time.sleep(delay)


if __name__ == "__main__":
    sys.exit(main())
