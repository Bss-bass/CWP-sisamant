import sys

count_param = len(sys.argv) - 1
if count_param == 0:
    print("none")
else:
    for i in range(1, len(sys.argv)):
        if not sys.argv[i].endswith("ism"):
            print(f'{sys.argv[i]}ism')
