#!/usr/bin/env python3

from sys import stdin

print('\n'.join([str(8 - j) + ''.join(['X' if i == int(ln) else '.' for i in range(8)]) for j, ln in enumerate(stdin)]))
print(' abcdefgh')
