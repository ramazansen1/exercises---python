"""
9, 7, 6, 3, 4, 1, 5, 2, 8 # Is 9 greater than 7?, Is 9 greater than 6?
9>7?, 9>6?, 9>3?, 9>4?, 9>1?, 9>5, 9>2?, 9>8?
# We should sort them by changing places with the largest to the right.
7, 6, 3, 4, 1, 5, 2, 8, 9
6, 3, 4, 1, 5, 2, 7, 8, 9
.....
...

1, 2, 3, 4, 5, 6, 7, 8, 9
"""
# Sorting Algorithm
myList = [9, 7, 6, 3, 4, 1, 5, 2, 8]
while True:
    arrangement = True
    # To prevent the loop from being out of range, we need to make it loop 8 times.
    for i in range(len(myList)-1):
        if myList[i] > myList[i+1]:
            #listem[i], listem[i+1] = listem[i+1], listem[i]
            # In order for the sequence to happen, we need to make a displacement.
            myList[i], myList[i+1] = myList[i+1], myList[i]
            arrangement = False
            # the arrangement must be wrong so the loop won't break
    if arrangement:
        break
print(myList)