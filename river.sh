#!/bin/bash
set -e

NuSMV -ils river.smv | \
grep -Eo "(    (m|c|mb|cb|b) = [a-Z0-9]+|  -> )" | \
python3 river.py
