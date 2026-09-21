#! /usr/bin/env python3

num = input("Enter a number less than 25: \n")

if int(num) > 25:
    print("Error")
else:
    for i in range(int(num), 26):
        print(f"Inside the loop, my variable is: {i}")
