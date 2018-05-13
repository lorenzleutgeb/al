#!/usr/bin/env python3

from re         import match
from subprocess import STDOUT, check_output
from sys        import argv, exit

presets = {
    'ltl': ['-is'],
    'ctl': ['-ils'],
}

if len(argv) != 2 or argv[1] not in presets:
    print('Expecting exactly one argument from {}!'.format(set(presets.keys())))
    exit(1)

state = {
    'm' : 3,
    'c' : 3,
    'mb': 0,
    'cb': 0,
    'b' : 1,
}

N = 3                  # number of missionaries/cannibals
R = range(1, 1 + N)

M = '👼'               # missionaries
C = '👹'               # cannibals
W = '\033[96m≈\033[0m' # water/wave (and ANSI control codes for blue color)
S = ' '                # space

cnt = 0

output = str(check_output(
    ['NuSMV'] +
    presets[argv[1]] +
    ['river.smv'],
    stderr=STDOUT
), 'utf-8').strip().split('\n')

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
        print("NOTE: Goal was reached, yay!")
        return

    if not(not(m != 0 and m != 3) or (c == m)):
        print("NOTE: Safety is violated!")

    print("Action:")

    srm = mb if b == -1 else 0
    src = cb if b == -1 else 0
    swm = mb * b
    swc = cb * b

    print(line(S, [6, m * 2, srm * 2, (M, N - m - srm), 4, (C, N - c - src)]))
    print(line(W, [11, (S, 1), (M, mb), (C, cb), (S, 2 - (mb + cb)), (S, 1), 11]) + ' ' + ('↑' if b == 1 else '↓'))
    print(line(S, [6, (M, m - swm), (N - m - srm) * 2, 4, (N - c + swc) * 2, (C, c - swc)]))
    print()

for ln in output:
    ln = ln.strip()

    # New state.
    if ln.startswith('->'):
        emit()
    else:
        m = match("(m|c|mb|cb|b) = ([A-Z0-9\-]+)", ln)
        if not m:
            continue

        lhs, rhs = m.group(1), m.group(2)
        state[lhs] = int(rhs)

emit()
