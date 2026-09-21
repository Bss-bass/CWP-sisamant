import sys

count_arg = len(sys.argv) - 1
first_avg = sys.argv[1] if count_arg >= 1 else None
second_avg = sys.argv[2] if count_arg >= 2 else None

if count_arg != 2 or first_avg not in second_avg:
    print("none")
else:
    count_occurrences = second_avg.count(first_avg)
    print(count_occurrences)
