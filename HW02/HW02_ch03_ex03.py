#!/usr/bin/env python
# HW02_ch03_ex03

# This exercise can be done using only the statements and other features we 
# have learned so far.

# (1) Write a function that draws a grid like the following:
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +

# Hint: to print more than one value on a line, you can print a 
# comma-separated sequence of values:

# print('+', '-')

# By default, print advances to the next line, but you can 
# override that behavior and put a space at the end, like this:

# print('+', end=' ')
# print('-')

# The output of these statements is '+ -'.

# A print statement with no argument ends the current line and 
# goes to the next line.



# (2) Write a function that draws a similar grid with four rows and four columns.
################################################################################
# Write your functions below:
# Body

#1

def do_twice(f):
	f()
	f()

def do_four(f):
	do_twice(f)
	do_twice(f)

def row():
	print('+ - - - -', end= ' ')

def column():
	print('|', ' ' * 7, end= ' ')

def draw_row():
	do_twice(row)
	print('+')

def draw_column():
	do_twice (column)
	print ('|')

def draw_two_by_two():
	draw_row()
	do_four(draw_column)
	draw_row()
	do_four(draw_column)
	draw_row()

draw_two_by_two()

#2

def draw_row_for_4by4():
	do_four(row)
	print('+')

def draw_column_for_4by4():
	do_four(column)
	print('|')

def draw_1by4():
	draw_row_for_4by4()
	do_four(draw_column_for_4by4)


def draw_4by4():
	do_four(draw_1by4)
	do_four(row)
	print('+')

print ("""         


""")

draw_4by4()






# Write your functions above:
################################################################################
def main():
    """Call your functions within this function.
    When complete have two function calls in this function:
    two_by_two()
    four_by_four()
    """
    print("Hello World!")
    



if __name__ == "__main__":
    main()