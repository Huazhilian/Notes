# -*- coding:utf-8 -*-
import sys
def reversewords(input):
    inputwords=input.split(" ")
    inputwords=inputwords[-1::-1]
    output=' '.join(inputwords)

    return output

input=input("Enter the string: \n")
rw=reversewords(input)
print(f'The reversed words are: \n{rw}') 
# f-string allows to embed expressions inside string literals 
# using curly braces {}

args = sys.argv # Get command line arguments
print(f"Arguments passed: {args}")