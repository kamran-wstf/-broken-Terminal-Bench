#!/bin/bash

# Run the strict pytest verifier. Dependencies are provided by the environment image.
pytest /tests/test_outputs.py -rA

exit $?
