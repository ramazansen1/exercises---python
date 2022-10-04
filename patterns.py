""" Patterns """

# pattern - 1
"""
$ $ $ $ $ $ $ $ $ $ $
"""

# Solution - 1

# i = 0
# while i < 10:
#     print(" $ ", end=" ")
#     i += 1

# Solution - 2

# for i in range(10):
#     print(" $ ", end=" ")

# pattern - 2
"""
$  #  $  # $  # $  # $  #  
"""

# Solution - 1
# i = 0
# while i < 10:
#     if i % 2 == 1:
#         print(" # ", end=" ")
#     else:
#         print(" $ ", end=" ")
#     i += 1

# Solution - 2

# for i in range(10):
#     if i % 2 == 0:
#         print(" $ ", end=" ")
#     else:
#         print(" # ", end=" ")

# pattern - 3
"""
*
$
*
$
*
$
*
$
*
$
"""
# Solution - 1

# i = 0
# while i < 10:
#     if i % 2 == 0:
#         print(" * ")
#     else:
#         print(" $ ")
#     i += 1

# Solution - 2

# for i in range(10):
#     if i % 2 == 0:
#         print(" * ")
#     else:
#         print(" $ ")

# pattern - 4
"""
 *   *   *   *   *  
 *   *   *   *   *  
 *   *   *   *   *  
 *   *   *   *   *  
 *   *   *   *   *  
"""
# Solution - 1

# i, j = 0, 0
# while i < 5:
#     while j < 5:
#         print(" * ", end=" ")
#         j += 1   //j will increase by one
#     j = 0       //j will be zero when the loop ends
#     i += 1      //i will increase by one
#     print()    // will go to the bottom line

# Solution - 2

# for i in range(5):
#     for j in range(5):
#         print(" * ", end=" ")
#     print()

# pattern - 5
"""
. . . . . . . . . .
* * * * * * * * * *
. . . . . . . . . .
* * * * * * * * * *
. . . . . . . . . .
* * * * * * * * * *
"""

# Solution - 1

# i, j = 0, 0
# while i < 6:
#     while j < 6:
#         if i % 2 == 0:
#             print(" . ", end=" ")
#         else:
#             print(" * ", end=" ")
#         j += 1
#     j = 0
#     i += 1
#     print()

# Solution - 2
# for i in range(6): // when the variable i is zero
#     for j in range(6): // variable j returned 5 times
#         if i % 2 == 0:
#             print(" . ", end=" ")
#         else:
#             print(" * ", end=" ")
#     print()

# pattern - 6
"""
* 
* *
* * *
* * * *
* * * * *
"""

# Solution - 1

# i, j = 0, 0
# while i < 5:
#     while i >= j:
#         j += 1
#         print(" * ", end=" ")
#     j = 0
#     i += 1
#     print()

# Solution - 2

# for i in range(1,6):
#     for j in range(i):
#         print(" * ", end=" ")
#     print()

# pattern - 7
"""
* * * * *
* * * *
* * *
* *
* 
"""

# Solution - 1

# i, j = 0, 5
# while i < 5:
#     while j > 0:
#         print(" * ", end=" ")
#         j -= 1
#     i += 1
#     print()
#     j = 5 -i

# Solution - 2

# for i in range(5):
#     for j in range(5-i):
#         print(" * ", end=" ")
#     print()

# pattern - 8
"""
* * * *
. * * *
. . * *
. . . *
"""

# Solution - 1

# i, j = 0, 0
# while i < 4:
#     while j < 4:
#         if i <= j:
#             print(" * ", end=" ")
#         else:
#             print(" . ", end=" ")
#         j += 1
#     j = 0
#     i += 1
#     print()

# Solution - 2

# for i in range(4):
#     for j in range(4):
#         if i <= j:
#             print(" * ", end=" ")
#         else:
#             print(" . ", end=" ")
#     print()

# pattern - 9
"""
# # # # # #
#         #      
#         #        
#         #        
# # # # # # 
"""
# Solution - 1

# i, j = 0, 0
# while i < 5:
#     while j < 6:
#         if i == 0 or i == 4 or j == 0 or j == 5:
#             print(" # ", end=" ")
#         else:
#             print("   ", end=" ")
#         j += 1
#     j = 0
#     i += 1
#     print()

# Solution - 2

# for i in range(5):
#     for j in range(5):
#         if i == 0 or i == 4 or j == 0 or j == 4: // here we connect the conditions with 'or'
#                                                 // We tried to catch the appropriate condition to create our pattern.
#             print(" # ", end=" ")               // output '#' when we caught any of the above conditions.
#         else:
#             print("   ", end=" ")               // We entered the else state when we couldn't catch any of the conditions!
#     print()

