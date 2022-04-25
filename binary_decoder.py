# MIT License
#
# Copyright (c) 2022 Litrin Jiang
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#

import optparse
import sys


def opts():
    parser = optparse.OptionParser()

    parser.add_option("-e", action="store_true", dest="hex", default=True)
    parser.add_option("-o", action="store_true", dest="oct",
                      default=False)
    parser.add_option("-d", action="store_true", dest="dec",
                      default=False)
    parser.add_option("-b", action="store_true", dest="bin",
                      default=False)

    parser.add_option("-v", "--value", dest="value", default=None)

    return parser.parse_args()


def get_value_pipe(s, fmt=16):
    if (fmt == 16 and s.startswith("0x")) or (fmt == 2 and s.startswith("0b")):
        s = s[2:]

    return int(s, fmt)


def main(value: int, f: bool = True):
    offset = 0
    result = []
    while value > 0:
        last_bit = value & 0x1
        result.append(last_bit == 1)

        if last_bit:
            print("#%s:\tON" % offset)
        elif not f:
            print("#%s:\tOFF" % offset)

        value >>= 1
        offset += 1

    return result


if __name__ == "__main__":
    (options, args) = opts()

    fmt = 16

    if options.dec:
        fmt = 10

    if options.oct:
        fmt = 8

    if options.bin:
        fmt = 2

    if options.value is not None:
        value = options.value
    else:
        value = sys.stdin.readline()

    value = get_value_pipe(value, fmt)

    main(value)
