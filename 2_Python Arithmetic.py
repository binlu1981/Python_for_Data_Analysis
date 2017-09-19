
import math     # Load the math module

# math.log() takes the natural logarithm of its argument:
math.log(2.7182)
#0.9999698965391098

# Add a second argument to specify the log base:
math.log(100, 10)       # Take the log base 10 of 100
#2.0

# math.exp() raises e to the power of its argument
math.exp(10)
#22026.465794806718

# If you ever need the constants e or pi you can use:
math.e    # Get the constant e
#2.718281828459045
math.pi   # Get the constant pi
#3.141592653589793

# Use math.sqrt() to take the square root of a number:
math.sqrt(64)

# Use round() to round a number to the nearest whole number:
round(233.234)
#233

# Add a second argument to round to a specified decimal place

round(233.234, 1)   # round to 1 decimal place
#233.2

# Enter a negative number to round to the left of the decimal
round(233.234, -1)   # round to the 10's place
#230.0

# Round down to the nearest whole number with math.floor()
math.floor(2.8)
#2

# Round up with math.ciel()
math.ceil(2.2)
#3

math.cos(0)         # Cosine
#1.0

math.sin(math.pi/2)  # Sine
#1.0
math.tan(math.pi/4)  # Tangent
#0.9999999999999999
math.acos(1)     # Inverse Cosine
#0.0


ath.asin(1)     # Inverse Sine
#1.5707963267948966

math.atan(1)     # Inverse Tangent
#0.7853981633974483
#Convert between radians and degrees with math.radians() and math.degrees():

math.radians(180)       # Convert degrees to radians
#3.141592653589793

math.degrees(math.pi)   # Convert radians to degrees
#180.0


# Check if 12 is an instance of type "int"
isinstance(12, int)
#True



#Similar to math expressions, logical expressions have a fixed order of operations. In a logical statement, "not" is executed first, followed by "or" and finally "and". Equalities and inequalities are executed last. Use parentheses to enforce the desired order of operations.

2 > 1 or 10 < 8 and not True
#True

((2 > 1) or (10 < 8)) and not True
#False
#You can convert numbers into boolean values using the bool() function. All numbers other than 0 convert to True:
bool(1)
#True
bool(-12.5)
#True
bool(0)
#False


#Check the length, maximum, minimum and sum of a list with the len(), max(), min() and sum() functions, respectively.
num_list = [1, 3, 5, 7, 9]
print( len(num_list))                # Check the length
print( max(num_list))                # Check the max
print( min(num_list))                # Check the min
print( sum(num_list))                # Check the sum
print( sum(num_list)/len(num_list))  # Check the mean*
"""
5
9
1
25
5.0
*Note: Python does not have a built in function to calculate the mean, but the numpy library we will introduce in upcoming lessons does.
"""

#Count the occurrences of an object within a list using the list.count() function:
num_list.count(3)
#1

new_list = [1, 5, 4, 2, 3, 6]      # Make a new list
new_list.reverse()                 # Reverse the list
print("Reversed list", new_list)
new_list.sort()                    # Sort the list
print("Sorted list", new_list)
#Reversed list [6, 3, 2, 4, 5, 1]
#Sorted list [1, 2, 3, 4, 5, 6]



"""
Copying Lists
In the code above, we saw that we can slice an entire list using the [:] indexing operation. You also copy a list using the list.copy() function:
"""
list1 = [1,2,3]                        # Make a list

list2 = list1.copy()                   # Copy the list

list1.append(4)                        # Add an item to list 1

print("List1:", list1)                 # Print both lists
print("List2:", list2)
#List1: [1, 2, 3, 4]
#List2: [1, 2, 3]
"""
As expected, the copy was not affected by the append operation we performed on the original list.
The copy function (and slicing an entire list with [:]) creates what is known as a "shallow copy."
A shallow copy makes a new list where each list element refers to the object at the same position (index)
in the original list. This is fine when the list is contains immutable objects like ints, floats and strings,
since they cannot change. Shallow copies can however, have undesired consequences when copying lists that contain mutable container objects, such as other lists.
"""
#Consider the following copy operation:
list1 = [1,2,3]                        # Make a list

list2 = ["List within a list", list1]  # Nest it in another list

list3 = list2.copy()                   # Shallow copy list2

print("Before appending to list1:")
print("List2:", list2)
print("List3:", list3, "\n")

list1.append(4)                        # Add an item to list1
print("After appending to list1:")
print("List2:", list2)
print("List3:", list3)
"""
Before appending to list1:
List2: ['List within a list', [1, 2, 3]]
List3: ['List within a list', [1, 2, 3]]

After appending to list1:
List2: ['List within a list', [1, 2, 3, 4]]
List3: ['List within a list', [1, 2, 3, 4]]
Notice that when we use a shallow copy on list2, the second element of list2 and its copy both refer to list1. Thus, when we append a new value into list1, the second element of list2 and the copy, list3, both change. When you are working with nested lists, you have to make a "deepcopy" if you want to truly copy nested objects in the original to avoid this behavior of shallow copies.
You can make a deep copy using the deepcopy() function in the copy module:
"""
import copy                            # Load the copy module

list1 = [1,2,3]                        # Make a list

list2 = ["List within a list", list1]  # Nest it in another list

list3 = copy.deepcopy(list2)           # Deep copy list2

print("Before appending to list1:")
print("List2:", list2)
print("List3:", list3, "\n")

list1.append(4)                        # Add an item to list1
print("After appending to list1:")
print("List2:", list2)
print("List3:", list3)
"""
Before appending to list1:
List2: ['List within a list', [1, 2, 3]]
List3: ['List within a list', [1, 2, 3]]

After appending to list1:
List2: ['List within a list', [1, 2, 3, 4]]
List3: ['List within a list', [1, 2, 3]]
This time list3 is not changed when we append a new value into list1 because the second element in list3 is a copy of list1 rather than a reference to list1 itself.
"""

my_string.split("l")  # Supply a substring to split on other values
['He', '', 'o wor', 'd']
#Split a multi-line string into a list of lines using str.splitlines():
multiline_string = """I am
a multiline
string!
"""
multiline_string.splitlines()
['I am', 'a multiline ', 'string!']

#For complex string operations of this sort is preferable to use the str.format() function. str.format() takes in a template string with curly braces as placeholders for values you provide to the function as the arguments. The arguments are then filled into the appropriate placeholders in the string:
template_string = "My name is {} I am {} and I live in {}"
template_string.format(name, age, city)
#'My name is Joe I am 10 and I live in Paris'