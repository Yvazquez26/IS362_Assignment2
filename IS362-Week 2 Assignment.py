#!/usr/bin/env python
# coding: utf-8

# Week 2 - One aspect of data structures that I find challenging are tuples, 
# looping through tuples and checking if items exists I keep getting that
# 'kiwi' is not in the new tuple.

# This function joins two tuples together using the zip function.

a = ("apple", "banana", "cherry")
b = ("Kiwi", "orange", "mango")

x = zip(a, b)

print(tuple(x))


# This function is to determine if a specified item is present in the new tuple.

if "kiwi" in tuple(x):
    print("Yes, 'kiwi' is in the x tuple")
else:
    print("No, 'kiwi' is not in the x tuple")




