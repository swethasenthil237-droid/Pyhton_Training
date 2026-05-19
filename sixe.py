import sys

ch = input("Enter a character: ")
num = int(input("Enter an integer: "))
f = float(input("Enter a float value: "))
d = float(input("Enter a double value: "))

print("Size of char:", sys.getsizeof(ch))
print("Size of int:", sys.getsizeof(num))
print("Size of float:", sys.getsizeof(f))
print("Size of double:", sys.getsizeof(d))