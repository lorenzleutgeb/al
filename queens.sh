#!/bin/bash
set -e

NuSMV -bmc -bmc_length 8 queens.smv | \
grep -oP "col\[[1-8]{1}\] = \K[1-9]{1}" | \
python3 queens.py
