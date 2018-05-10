#!/usr/bin/env python3

from subprocess import STDOUT, check_output

col = [0] * 8

output = str(check_output(
    [
        'NuSMV',
        '-bmc',
        '-bmc_length', '8',
        'queens.smv'
    ],
    stderr=STDOUT
), 'utf-8').strip().split('\n')

prefix = '    col['

for ln in output:
    if ln.startswith(prefix):
        col[int(ln[len(prefix)]) - 1] = int(ln[len(prefix + '] = ') + 1]) - 1

print(
    '\n' +
    '  A Solution for The Eight Queens Problem\n'
    '     ╔═══╤═══╤═══╤═══╤═══╤═══╤═══╤═══╗\n'+
    '     ╟───┼───┼───┼───┼───┼───┼───┼───╢\n'.join(['     ║ ' + ' │ '.join(['♕' if i == ln else ' ' for i in range(8)]) + ' ║ ' + str(8 - j) + '\n' for j, ln in enumerate(col)]) +
    '     ╚═══╧═══╧═══╧═══╧═══╧═══╧═══╧═══╝\n' +
    '       a   b   c   d   e   f   g   h' +
    '\n'
)

# Computes the FEN for the board represented by col
fen = '/'.join([
    (str(c) if c > 0 else '') + 'Q' + (str(7 - c) if c < 7 else '') for c in col
]) + ' w - -'

print('FEN ' + fen)
print('URL ' + 'https://lichess.org/editor/' + fen.replace(' ', '_'))
