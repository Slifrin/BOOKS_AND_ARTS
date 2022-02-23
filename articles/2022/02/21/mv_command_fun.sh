#! /bin/bash

# https://www.tomshardware.com/how-to/move-remove-files-linux

for f in *.py; do mv -- "$f" "${f%.txt}.log"; done