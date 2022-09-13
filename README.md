# Taktile Coding Challenge

## Requirements: 
- Python3.8+
- Further requirements are listed in the requirements.txt file

## Introduciton
This code represents an alternative implementation of the fold function.

## Description of the fold funciton
_Source: assignement description._

`fold` is a higher order function that takes
* a sequence of type A
* a "starting" value of type B
* a function (A, B) -> B

and returns a B. E.g., the `sum` of an array is a special case of fold, where
* the sequence is an array of numbers
* the starting value is 0
* the function is `+`