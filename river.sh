#!/bin/bash
set -e

NuSMV river.smv | \
grep -Eo "(    (m|c|mb|cb|b) = [a-Z0-9]+|  -> )" | \
python3 river.py
