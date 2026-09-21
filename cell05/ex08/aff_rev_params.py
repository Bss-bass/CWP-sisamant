import sys

count_arg = len(sys.argv) - 1
if count_arg < 2:
    print("none")
else:
    for i in range(count_arg, 0, -1):
        print(sys.argv[i])
