import sys

count_arg = len(sys.argv) - 1
if count_arg != 1:
    print("none")
else:
    print(sys.argv[1].upper())
