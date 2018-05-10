#!/usr/bin/env python3

from sys import stdin

print(
    '\n' +
    '  A Solution for The Eight Queens Problem\n'
    '     ╔═══╤═══╤═══╤═══╤═══╤═══╤═══╤═══╗\n'+
    '     ╟───┼───┼───┼───┼───┼───┼───┼───╢\n'.join(['   ' + str(8 - j) + ' ║ ' + ' │ '.join(['♕' if i == int(ln) else ' ' for i in range(8)]) + ' ║\n' for j, ln in enumerate(stdin)]) +
    '     ╚═══╧═══╧═══╧═══╧═══╧═══╧═══╧═══╝\n' +
    '       a   b   c   d   e   f   g   h' +
    '\n'
)
