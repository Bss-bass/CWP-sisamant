import sys

count_param = len(sys.argv) - 1
if count_param != 2:
    print("none")
else:
    start = int(sys.argv[1])
    end = int(sys.argv[2])
    result = list(range(start, end + 1))
    print(result)
