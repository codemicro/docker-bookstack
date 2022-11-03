#!/usr/bin/env python3
import sys

VERSION = sys.argv[1]

def do_substitution(input_filename: str, output_filename: str):
    with open(input_filename) as f:
        with open(output_filename, "w") as of:
            of.write(f.read().replace("%s", VERSION))

do_substitution("Dockerfile.tpl", "Dockerfile")
do_substitution("README.md.tpl", "README.md")