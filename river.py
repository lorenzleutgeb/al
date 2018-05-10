#!/usr/bin/env python3

from sys import stdin

state = {
    'm' : 3,
    'c' : 3,
    'mb': 0,
    'cb': 0,
    'b' : False
}

N = 3                  # number of missionaries/cannibals
R = range(1, 1 + N)

M = '👼'                # missionaries
C = '👹'                # cannibals
W = '\033[96m≈\033[0m' # water/wave (and ANSI control codes for blue color)
S = ' '                # space
T = '⛰️⛰️'

cnt = 0

def line(neutral, spec):
    result = ''
    for it in spec:
        if type(it) is int:
            result = result + neutral * it
        else:
            c, t = it
            result = result + c * t
    return result

def emit():
    global cnt

    print()


    cnt = cnt + 1
    print("Day " + str(cnt) + ":")

    #print(state)

    m, c, mb, cb, b = state['m'], state['c'], state['mb'], state['cb'], state['b']
    print(line(S, [6, m * 2, (M, N - m), 4, (C, N - c)]))
    print(W * ((2 * 3 + 2 + 2 * N) * 2))
    print(line(S, [6, (M, m), (N - m) * 2, 4, (N - c) * 2, (C, c)]))

    if m + c == 0:
        return

    print("Action:")

    srm = mb if not b else 0
    src = cb if not b else 0
    swm = mb * int(b)
    swc = cb * int(b)

    print(line(S, [6, m * 2, srm * 2, (M, N - m - srm), 4, (C, N - c - src)]))
    print(line(W, [11, (S, 1), (M, mb), (C, cb), (S, 2 - (mb + cb)), (S, 1), 11]) + ' ' + ('↑' if b else '↓'))
    print(line(S, [6, (M, m - swm), (N - m - srm) * 2, 4, (N - c + swc) * 2, (C, c - swc)]))
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
