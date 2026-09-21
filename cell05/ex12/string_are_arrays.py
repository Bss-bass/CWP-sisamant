import sys

count_arg = len(sys.argv) - 1
if count_arg != 1:
    print("none")
else:
    input_str = sys.argv[1]
    result = ''
    for char in input_str:
        if char == 'z':
            result += 'z'
    if result == '':
        print("none")
    else:
        print(result)
