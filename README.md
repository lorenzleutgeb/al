# Advanced Logic

[![Build Status](https://travis-ci.com/lorenzleutgeb/al.svg?branch=master)](https://travis-ci.com/lorenzleutgeb/al)

## Tasks

### Cannibals and Missionaries (`river.smv`)

Three missionaries and three cannibals seek to cross a river. They all start
from the same side of the river. They have a boat which can carry up to two
people at time. All missionaries and cannibals are able to navigate the boat
(no need for a ferryman). If at any time the cannibals outnumber the
missionaries on either side of the bank the cannibals will eat the
missionaries! The goal is to bring all of the missionaries and cannibal on the
other side of the river.

Formalize the problem as an NuSMV program and add temporal logic specifications
to check the existence of a safe solution:

  1. All of the missionaries and cannibals cross the river;
  2. During the transitions to the goal state no missionary is eaten!

                                                                                                                        
To execute the implementation, run `river.py` which will in turn run NuSMV
with `river.smv` as input and render the solution:                                                                     
                                                                                                                        
```                                                                                                                     
$ ./river.py ctl 

  A Solution for The Missionaries and Cannibals Problem

                              
    Action  1 ≈≈≈≈≈≈≈≈≈≈≈ 👼👹 ≈≈≈≈≈≈≈≈≈≈≈ ↑
                    👼👼        👹👹

                              👹
    Action  2 ≈≈≈≈≈≈≈≈≈≈≈ 👼   ≈≈≈≈≈≈≈≈≈≈≈ ↓
                    👼👼        👹👹

                              👹
    Action  3 ≈≈≈≈≈≈≈≈≈≈≈ 👹👹 ≈≈≈≈≈≈≈≈≈≈≈ ↑
                    👼👼👼          

                              👹👹
    Action  4 ≈≈≈≈≈≈≈≈≈≈≈ 👹   ≈≈≈≈≈≈≈≈≈≈≈ ↓
                    👼👼👼          

                              👹👹
    Action  5 ≈≈≈≈≈≈≈≈≈≈≈ 👼👼 ≈≈≈≈≈≈≈≈≈≈≈ ↑
                    👼            👹

                        👼    👹
    Action  6 ≈≈≈≈≈≈≈≈≈≈≈ 👼👹 ≈≈≈≈≈≈≈≈≈≈≈ ↓
                    👼            👹

                        👼    👹
    Action  7 ≈≈≈≈≈≈≈≈≈≈≈ 👼👼 ≈≈≈≈≈≈≈≈≈≈≈ ↑
                                👹👹

                    👼👼👼    
    Action  8 ≈≈≈≈≈≈≈≈≈≈≈ 👹   ≈≈≈≈≈≈≈≈≈≈≈ ↓
                                👹👹

                    👼👼👼    
    Action  9 ≈≈≈≈≈≈≈≈≈≈≈ 👹👹 ≈≈≈≈≈≈≈≈≈≈≈ ↑
                                  👹

                      👼👼    👹👹
    Action 10 ≈≈≈≈≈≈≈≈≈≈≈ 👼   ≈≈≈≈≈≈≈≈≈≈≈ ↓
                                  👹

                      👼👼    👹👹
    Action 11 ≈≈≈≈≈≈≈≈≈≈≈ 👼👹 ≈≈≈≈≈≈≈≈≈≈≈ ↑
                                    

                      👼👼    👹👹
    Action 12 ≈≈≈≈≈≈≈≈≈≈≈ 👼👹 ≈≈≈≈≈≈≈≈≈≈≈ ↓

```

### Eight Queens Problem (`queens.smv`)

Solve the Eight Queens Problem: In a chess board, the goal is to place eight
queens in such a way that none of them is under attack by another one.
Implement and describe specifications (both, in CTL and LTL) that
provide solutions to the problem.

To execute the implementation, run `queens.py` which will in turn run NuSMV
with `queens.smv` as input and render the solution:

```
$ ./queens.py ctl

  A Solution for The Eight Queens Problem

     ╔═══╤═══╤═══╤═══╤═══╤═══╤═══╤═══╗
     ║   │   │   │   │ ♕ │   │   │   ║ 8
     ╟───┼───┼───┼───┼───┼───┼───┼───╢
     ║   │ ♕ │   │   │   │   │   │   ║ 7
     ╟───┼───┼───┼───┼───┼───┼───┼───╢
     ║   │   │   │ ♕ │   │   │   │   ║ 6
     ╟───┼───┼───┼───┼───┼───┼───┼───╢
     ║   │   │   │   │   │ ♕ │   │   ║ 5
     ╟───┼───┼───┼───┼───┼───┼───┼───╢
     ║   │   │   │   │   │   │   │ ♕ ║ 4
     ╟───┼───┼───┼───┼───┼───┼───┼───╢
     ║   │   │ ♕ │   │   │   │   │   ║ 3
     ╟───┼───┼───┼───┼───┼───┼───┼───╢
     ║ ♕ │   │   │   │   │   │   │   ║ 2
     ╟───┼───┼───┼───┼───┼───┼───┼───╢
     ║   │   │   │   │   │   │ ♕ │   ║ 1
     ╚═══╧═══╧═══╧═══╧═══╧═══╧═══╧═══╝
       a   b   c   d   e   f   g   h

FEN 4Q3/1Q6/3Q4/5Q2/7Q/2Q5/Q7/6Q1 w - -
URL https://lichess.org/editor/4Q3/1Q6/3Q4/5Q2/7Q/2Q5/Q7/6Q1_w_-_-
```
