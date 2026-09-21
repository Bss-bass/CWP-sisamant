import sys

count_param = len(sys.argv) - 1
if count_param == 0:
    print("none")
else:
    print(f'parameters: {count_param} ')
    for i in range(1, len(sys.argv)):
        print(f'{sys.argv[i]}: {len(sys.argv[i])}')
