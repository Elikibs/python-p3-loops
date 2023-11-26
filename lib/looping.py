#!/usr/bin/env python3

# Assignment 1
def happy_new_year(num):
  while num > 0:
    print(num)
    num -=1
  print("Happy New Year!")

happy_new_year(10)

# Assignment 2
def square_integers(list_of_integers):
  return [num * num for num in list_of_integers]

print(square_integers([1, 2, 3, 4, 5]))

# Assignemnt 3
def fizz_buz():
  for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
      print("FizzBuzz")
    elif num % 3 == 0:
      print("Fizz")
    elif num % 5 == 0:
      print("Buzz")
    else:
      print(num)

print(fizz_buz())
