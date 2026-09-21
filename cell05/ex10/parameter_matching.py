import sys

count_args = len(sys.argv) - 1
if count_args != 1:
    print("none")
else:
    param = input("What was the parameter? ")
    if param == sys.argv[1]:
        print("Good job!")
    else:
        print("Nope, sorry...")
