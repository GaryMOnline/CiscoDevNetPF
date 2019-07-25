import math
import random

#Declaration of all variable types.
int = 100
float = 10.1
string = "hello"
list = ['a',25,7.2]
tuple = ('a',25,7.2)
dictionary = {"apples":5,"pears":12,"bananas":92}

print("int is a {} with a value of {}".format(type(int), int))
print("float is a {} with a value of {}".format(type(float), float))
print("string is a {} with a value of {}".format(type(string), string))
print("list is a {} with a value of {}".format(type(list), list))
print("tuple is a {} with a value of {}".format(type(tuple), tuple))
print("dictionary is a {} with a value of {}".format(type(dictionary), dictionary))

#Integer / Number manipulation:

#String Manipulation:
print("\nContents of Sting is '{}'".format(string))
string = string + " world"
print("Lets add the world, are you ready - '{}'".format(string))
exclaim = "!"
exclaim = exclaim *3
print("Lets make it dramatic - '{}'".format(string + exclaim))
print string          # Prints complete string
print string[0]       # Prints first character of the string
print string[2:5]     # Prints characters starting from 3rd to 5th
print string[2:]      # Prints string starting from 3rd character
print string * 2      # Prints string two times
print string + "TEST" # Prints concatenated string

#List Manipulation:
print("\nContents of list is {}".format(list))
print("Second object in list is {}".format(list[1]))
list.append("new")
print("Contents of list is now {}".format(list))

#Tuple Manipulation:
print("\nContents of tuple is {}".format(tuple))
print("Second object in tuple is {}".format(tuple[1]))
print("Can't add anything to tuple, is immutible!")

