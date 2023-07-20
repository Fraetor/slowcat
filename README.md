# Slowcat

A very slow concatenation program.

Much like the well known [cat](https://en.wikipedia.org/wiki/Cat_(Unix))
command, slowcat reads a file to standard output. The difference is that slowcat
does it slowly, one byte at a time. This can be used to emulate historic data
rates, or otherwise look generally nifty.

## Requirements and Installation

The only requirement of slowcat is [Python 3](https://www.python.org).

It can be installed on Linux simply by copying an executable `slowcat.py` into
`~/.local/bin/`. You may want to remove the file extension in this case.

## Usage

```text
usage: slowcat [-h] [-r RATE] [--version] [FILE ...]

Read out a file one byte at a time.

positional arguments:
  FILE                  the file(s) to read; use - or omit for standard input

options:
  -h, --help            show this help message and exit
  -r RATE, --rate RATE  how many bytes to read per second (default: 10)
  --version             show version information and exit
```

## Licence

Slowcat is available under the following public domain equivalent licence.

### BSD Zero Clause License

Copyright © 2023 by James Frost

Permission to use, copy, modify, and/or distribute this software for any purpose
with or without fee is hereby granted.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH
REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND
FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT,
INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS
OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER
TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF
THIS SOFTWARE.
