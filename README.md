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

### 8 Queens Problem (`queens.smv`)

Solve the 8 Queens Problem: In a chess board, the goal is to place 8 queens in
such a way that none of them is under attack by another one. Implement and
describe specifications (both, in CTL and LTL) that provide solutions to the
problem.
