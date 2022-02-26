"""
@authors: Kal Young, Brian Cavin, Landon Johnson

Test code for Comb Sort

Testing on an array of 10 elements. If it does good with that, bigger sizes
should run just fine

"""

# Gap Value

def nextGap(gap):
 
    gap = (gap * 10)//13
    
    if gap < 1:    
        return 1
    
    return gap
 
# Comb Sort

def combSort(array):
    
    n = len(array)
    gap = n
    swapped = True
 
    while gap !=1 or swapped == 1:
 
        gap = nextGap(gap)
 
        swapped = False
 
        for i in range(0, n-gap):
            if array[i] > array[i + gap]:
                array[i], array[i + gap]=array[i + gap], array[i]
                swapped = True
 
 
# Driver Code

array = [ 18, 74, 21, 30, -44, 55, -66, 98, 0]

print ("Original Array:")

for i in range(len(array)):
    print (array[i],end=", ")

combSort(array)
 
print ("\n\nComb sort has been implemented.")

for i in range(len(array)):
    print (array[i],end=", ")
