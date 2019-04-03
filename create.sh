#!/usr/bin/bash

# For consistency
DIRECTORY_NUMBER="<directoryNumber>"

# Check number of arguments
if (( $# != 1 )); then
    echo "Usage: " $0 $DIRECTORY_NUMBER
    exit
fi

# Directory number
n=$1

# Has to be 1 or 2 digit
if (( $n > 99 )); then
    echo $DIRECTORY_NUMBER "has to be smaller than 100"
    exit
fi

# Add leading zero
if (( $n < 10 )); then
    n=0$n
fi

# Create directory 
echo "Creating day$n directory..."
mkdir day$n

# Create empty files
echo "Creating __init__.py..."
touch day$n/__init__.py
echo "Creating input.txt..."
touch day$n/input.txt

# Create template python file
echo "Creating day$n.py"
echo "import sys
sys.path.append(\"..\")
import util

def partOne():
    pass

def partTwo():
    pass

def main():
    partOne()
    partTwo()

if __name__ == \"__main__\":
    main()" > day$n/day$n.py

