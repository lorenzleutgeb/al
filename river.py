#!/usr/bin/env python3

from sys import stdin

state = {
    'm': 3,
    'c': 3,
    'mb': 0,
    'cb': 0,
    'b': False
}

cnt = 0

def emit():
    global cnt
    cnt = cnt + 1
    print(str(cnt))
    #print(state)
    m, c, mb, cb, b = state['m'], state['c'], state['mb'], state['cb'], state['b']
    print(
        '  ' +
        ''.join(['M' if i > m else ' ' for i in range(1, 4)]) +
        ' ' +
        ''.join(['C' if i > c else ' ' for i in range(1, 4)])
    )
    print('~~~~~~~~~~~')
    print('~~~~~~~~~~~')
    print(
        '  ' +
        ''.join(['M' if i <= m else ' ' for i in range(1, 4)]) +
        ' ' +
        ''.join(['C' if i <= c else ' ' for i in range(1, 4)])
    )

    if m + c == 0:
        return

    if b:
        c = c - cb
        m = m - mb

    print()
    print(
        '  ' +
        ''.join(['M' if i > m else ' ' for i in range(1, 4 - mb)]) +
        ' ' +
        ''.join(['C' if i > c else ' ' for i in range(1, 4 - cb)])
    )
    #print('~~~~~~~')
    if state['b']:
        print('~~~~~~~~~~~')
    print(
        '~~' +
        ''.join(['M' if i <= mb else '~' for i in range(1, 4)]) +
        '~' +
        ''.join(['C' if i <= cb else '~' for i in range(1, 4)]) +
        '~~'
    )
    #print('~~~~~~~')
    if not state['b']:
        print('~~~~~~~~~~~')
    print(
        '  ' +
        ''.join(['M' if i <= m else ' ' for i in range(1, 4 - mb)]) +
        ' ' +
        ''.join(['C' if i <= c else ' ' for i in range(1, 4 - cb)])
    )
    print()

# Discard first line.
stdin.readline()

for ln in stdin:
    ln = ln.strip()

    # New state.
    if ln.startswith('->') or ln == '':
        emit()
    else:
        lhs, rhs = ln.split(' = ')
        if lhs == 'b':
            state['b'] = rhs == 'TRUE'
        else:
            state[lhs] = int(rhs)

emit()
