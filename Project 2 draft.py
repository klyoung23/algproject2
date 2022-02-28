"""
@authors: Kal Young, Brian Cavin, Landon Johnson
Test code for Comb Sort
Testing on an array of 10 elements. If it does good with that, bigger sizes
should run just fine
"""

# Gap Value

import time as t
import numpy as np


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
                
# Python program for implementation of MergeSort
def mergeSort(array):
    if len(array) > 1:
  
         # Finding the mid of the array
        mid = len(array)//2
  
        # Dividing the array elements
        L = array[:mid]
  
        # into 2 halves
        R = array[mid:]
  
        # Sorting the first half
        mergeSort(L)
  
        # Sorting the second half
        mergeSort(R)
  
        i = j = k = 0
  
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = R[j]
                j += 1
            k += 1
  
        # Checking if any element was left
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1
  
        while j < len(R):
            array[k] = R[j]
            j += 1
            k += 1

# Python program for implementation of Quicksort 
  
# This function is same in both iterative and recursive
def partition(arr,l,h):
    i = ( l - 1 )
    x = arr[h]
  
    for j in range(l , h):
        if   arr[j] <= x:
  
            # increment index of smaller element
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
  
    arr[i+1],arr[h] = arr[h],arr[i+1]
    return (i+1)
  
# Function to do Quick sort
# arr[] --> Array to be sorted,
# l  --> Starting index,
# h  --> Ending index
def quickSortIterative(arr,l,h):
  
    # Create an auxiliary stack
    size = h - l + 1
    stack = [0] * (size)
  
    # initialize top of stack
    top = -1
  
    # push initial values of l and h to stack
    top = top + 1
    stack[top] = l
    top = top + 1
    stack[top] = h
  
    # Keep popping from stack while is not empty
    while top >= 0:
  
        # Pop h and l
        h = stack[top]
        top = top - 1
        l = stack[top]
        top = top - 1
  
        # Set pivot element at its correct position in
        # sorted array
        p = partition( arr, l, h )
  
        # If there are elements on left side of pivot,
        # then push left side to stack
        if p-1 > l:
            top = top + 1
            stack[top] = l
            top = top + 1
            stack[top] = p - 1
  
        # If there are elements on right side of pivot,
        # then push right side to stack
        if p+1 < h:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h

# Python program for implementation of Bubble Sort
 
def bubbleSort(array):
    n = len(array)
 
    # Traverse through all array elements
    for i in range(n-1):
    # range(n) also work but outer loop will
    # repeat one time more than needed.
 
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if array[j] > array[j + 1] :
                array[j], array[j + 1] = array[j + 1], array[j]
 
# Writen by Brian Cavin
# Generates 3 lists, one presorted, one random, and one reverse sorted
def get_lists(size):
        
    floor = 1
    ceiling = size+1
   
    best = np.arange(floor,ceiling,1)
    avg = np.random.randint(ceiling*-1,ceiling,size)
    worst = np.arange(ceiling-1, floor-1, -1)
    
    return best, avg, worst

# Written by Brian Cavin
# Tests a given algorith with the array pased to the function 3 times and returns the times
def test(array, sort_type):
    
    times = []
    
    # Copies the list 3 times so that a sorted array is not passed to a sort function
    arrays = []
    arrays.insert(0,array.copy())
    arrays.insert(1,array.copy())
    arrays.insert(2,array.copy())
    high = array.__len__()-1
    
    if sort_type == 'merge':
        
        i = 0
        while i < 3:
            
            t0 = t.time()
            mergeSort(arrays[i])
            t1 = t.time()
            time = t1-t0
            times.append(time)
            i+=1
            
    elif sort_type == 'quick':
        i = 0
        while i < 3:
            
            t0 = t.time()
            quickSortIterative(arrays[i],0,high)
            t1 = t.time()
            time = t1-t0
            times.append(time)
            i+=1
            
    elif sort_type == 'bubble':
        
        i = 0
        while i < 3:
            
            t0 = t.time()
            bubbleSort(arrays[i])
            t1 = t.time()
            time = t1-t0
            times.append(time)
            i+=1
        
    elif sort_type == 'comb':
        
        i = 0
        while i < 3:
            
            t0 = t.time()
            combSort(arrays[i])
            t1 = t.time()
            time = t1-t0
            times.append(time)
            i+=1
            
            

    return times[0], times[1], times[2]
    


# Driver Code

'''
Variable Legend:

Times:
    
    Merge Sort:
        msb = merge sort, small, best case
        msa = merge sort, small, average case
        msw = merge sort, small, worst case
        
        mmb = merge sort, medium, best case
        mma = merge sort, medium, average case
        mmw = merge sort, medium, worst case
        
        mlb = merge sort, large, best case
        mla = merge sort, large, average case
        mlw = merge sort, large, worst case
    
    Quick Sort:
        qsb = quick sort, small, best case
        qsa = quick sort, small, average case
        qsw = quick sort, small, worst case
        
        qmb = quick sort, medium, best case
        qma = quick sort, medium, average case
        qmw = quick sort, medium, worst case
        
        qlb = quick sort, large, best case
        qla = quick sort, large, average case
        qlw = quick sort, large, worst case
    
    Bubble Sort:
        bsb = bubble sort, small, best case
        bsa = bubble sort, small, average case
        bsw = bubble sort, small, worst case
        
        bmb = bubble sort, medium, best case
        bma = bubble sort, medium, average case
        bmw = bubble sort, medium, worst case
        
        blb = bubble sort, large, best case
        bla = bubble sort, large, average case
        blw = bubble sort, large, worst case
        
    Comb Sort:
        csb = comb sort, small, best case
        csa, comb sort, small, average case
        csw = comb sort, small, worst case
        
        cmb = comb sort, medium, best case
        cma = comb sort, medium, average case
        cmw = comb sort, medium, worst case
        
        clb = comb sort, large, best case
        cla = comb sort, large, average case
        clw = comb sort, large, worst case

Lists:
    
    Small:
        small_best:
            A presorted list of 10,000 integers from 1 to 10,000
            
        small_avg:
            A random list of 10,000 integers from -10,000 to 10,000
        
        small_worst:
            A reverse sorted list of 10,000 integers from 10,000 to 1
    
    Medium:    
        med_best:
            A presorted list of 100,000 integers from 1 to 100,000
            
        med_avg:
            A random list of 100,000 integers from -100,000 to 100,000
            
        med_worst:
            
            
    Large:  
        large_best:
            A presorted list of 1,000,000 integers from 1 to 1,000,000
            
        large_avg:
            A random list of 1,000,000 integers from -1,000,000 to 1,000,000
            
        large_worst:
            A reverse sorted list of 1,000,000 integers from 1,000,000 to 1
        



'''

small = 100
medium = 1000
large = 10000


#####################
#                   #
#    Merge sort     #
#                   #
#####################


# Generate lists for merge sort
small_best, small_avg, small_worst = get_lists(small)
med_best, med_avg, med_worst = get_lists(medium)
large_best, large_avg, large_worst = get_lists(large)

# Call test function for each size and case
# Print Results
print("Merge sort results:\n")
print("\tSmall list (size:",small,"):\n")

msb_1, msb_2, msb_3 = test(small_best, 'merge')
print("\t\tBest case #1:",msb_1,"seconds.")
print("\t\tBest case #2:",msb_2,"seconds.")
print("\t\tBest case #2:",msb_3,"seconds.")

msa_1, msa_2, msa_3 = test(small_avg, 'merge')
print("\t\tAverage case #1:",msa_1,"seconds.")
print("\t\tAverage case #2:",msa_2,"seconds.")
print("\t\tAverage case #2:",msa_3,"seconds.")

msw_1, msw_2, msw_3 = test(small_worst, 'merge')
print("\t\tWorst case #1:",msw_1,"seconds.")
print("\t\tWorst case #2:",msw_2,"seconds.")
print("\t\tWorst case #2:",msw_3,"seconds.")

print("\n\tMedium list (size:",medium,"):\n")

mmb_1, mmb_2, mmb_3 = test(med_best, 'merge')
print("\t\tBest case #1:",mmb_1,"seconds.")
print("\t\tBest case #2:",mmb_2,"seconds.")
print("\t\tBest case #2:",mmb_3,"seconds.")

mma_1, mma_2, mma_3 = test(med_avg, 'merge')
print("\t\tAverage case #1:",mma_1,"seconds.")
print("\t\tAverage case #2:",mma_2,"seconds.")
print("\t\tAverage case #2:",mma_3,"seconds.")

mmw_1, mmw_2, mmw_3 = test(med_worst, 'merge')
print("\t\tWorst case #1:",mmw_1,"seconds.")
print("\t\tWorst case #2:",mmw_2,"seconds.")
print("\t\tWorst case #2:",mmw_3,"seconds.")

print("\n\tLarge list (size:",large,"):\n")

mlb_1, mlb_2, mlb_3 = test(large_best, 'merge')
print("\t\tBest case #1:",mlb_1,"seconds.")
print("\t\tBest case #2:",mlb_2,"seconds.")
print("\t\tBest case #2:",mlb_3,"seconds.")

mla_1, mla_2, mla_3 = test(large_avg, 'merge')
print("\t\tAverage case #1:",mla_1,"seconds.")
print("\t\tAverage case #2:",mla_2,"seconds.")
print("\t\tAverage case #2:",mla_3,"seconds.")

mlw_1, mlw_2, mlw_3 = test(large_worst, 'merge')
print("\t\tWorst case #1:",mlw_1,"seconds.")
print("\t\tWorst case #2:",mlw_2,"seconds.")
print("\t\tWorst case #2:",mlw_3,"seconds.\n")


#####################
#                   #
#    Quick sort     #
#                   #
#####################


# Generate lists for quick sort
small_best, small_avg, small_worst = get_lists(small)
med_best, med_avg, med_worst = get_lists(medium)
large_best, large_avg, large_worst = get_lists(large)

# Call test function for each size and case
# Print Results
print("Quick sort results:\n")
print("\tSmall list (size:",small,"):\n")

qsb_1, qsb_2, qsb_3 = test(small_best, 'quick')
print("\t\tBest case #1:",qsb_1,"seconds.")
print("\t\tBest case #2:",qsb_2,"seconds.")
print("\t\tBest case #2:",qsb_3,"seconds.")

qsa_1, qsa_2, qsa_3 = test(small_avg, 'quick')
print("\t\tAverage case #1:",qsa_1,"seconds.")
print("\t\tAverage case #2:",qsa_2,"seconds.")
print("\t\tAverage case #2:",qsa_3,"seconds.")

qsw_1, qsw_2, qsw_3 = test(small_worst, 'quick')
print("\t\tWorst case #1:",qsw_1,"seconds.")
print("\t\tWorst case #2:",qsw_2,"seconds.")
print("\t\tWorst case #2:",qsw_3,"seconds.")

print("\n\tMedium list (size:",medium,"):\n")

qmb_1, qmb_2, qmb_3 = test(med_best, 'quick')
print("\t\tBest case #1:",qmb_1,"seconds.")
print("\t\tBest case #2:",qmb_2,"seconds.")
print("\t\tBest case #2:",qmb_3,"seconds.")

qma_1, qma_2, qma_3 = test(med_avg, 'quick')
print("\t\tAverage case #1:",qma_1,"seconds.")
print("\t\tAverage case #2:",qma_2,"seconds.")
print("\t\tAverage case #2:",qma_3,"seconds.")

qmw_1, qmw_2, qmw_3 = test(med_worst, 'quick')
print("\t\tWorst case #1:",qmw_1,"seconds.")
print("\t\tWorst case #2:",qmw_2,"seconds.")
print("\t\tWorst case #2:",qmw_3,"seconds.")

print("\n\tLarge list (size:",large,"):\n")

qlb_1, qlb_2, qlb_3 = test(large_best, 'quick')
print("\t\tBest case #1:",qlb_1,"seconds.")
print("\t\tBest case #2:",qlb_2,"seconds.")
print("\t\tBest case #2:",qlb_3,"seconds.")

qla_1, qla_2, qla_3 = test(large_avg, 'quick')
print("\t\tAverage case #1:",qla_1,"seconds.")
print("\t\tAverage case #2:",qla_2,"seconds.")
print("\t\tAverage case #2:",qla_3,"seconds.")

qlw_1, qlw_2, qlw_3 = test(large_worst, 'quick')
print("\t\tWorst case #1:",qlw_1,"seconds.")
print("\t\tWorst case #2:",qlw_2,"seconds.")
print("\t\tWorst case #2:",qlw_3,"seconds.\n")


#####################
#                   #
#    Bubble sort    #
#                   #
#####################


# Generate lists for bubble sort
small_best, small_avg, small_worst = get_lists(small)
med_best, med_avg, med_worst = get_lists(medium)
large_best, large_avg, large_worst = get_lists(large)

# Call test function for each size and case
# Print Results
print("Bubble sort results:\n")
print("\tSmall list (size:",small,"):\n")

bsb_1, bsb_2, bsb_3 = test(small_best, 'bubble')
print("\t\tBest case #1:",bsb_1,"seconds.")
print("\t\tBest case #2:",bsb_2,"seconds.")
print("\t\tBest case #2:",bsb_3,"seconds.")

bsa_1, bsa_2, bsa_3 = test(small_avg, 'bubble')
print("\t\tAverage case #1:",bsa_1,"seconds.")
print("\t\tAverage case #2:",bsa_2,"seconds.")
print("\t\tAverage case #2:",bsa_3,"seconds.")

bsw_1, bsw_2, bsw_3 = test(small_worst, 'bubble')
print("\t\tWorst case #1:",bsw_1,"seconds.")
print("\t\tWorst case #2:",bsw_2,"seconds.")
print("\t\tWorst case #2:",bsw_3,"seconds.")

print("\n\tMedium list (size:",medium,"):\n")

bmb_1, bmb_2, bmb_3 = test(med_best, 'bubble')
print("\t\tBest case #1:",bmb_1,"seconds.")
print("\t\tBest case #2:",bmb_2,"seconds.")
print("\t\tBest case #2:",bmb_3,"seconds.")

bma_1, bma_2, bma_3 = test(med_avg, 'bubble')
print("\t\tAverage case #1:",bma_1,"seconds.")
print("\t\tAverage case #2:",bma_2,"seconds.")
print("\t\tAverage case #2:",bma_3,"seconds.")

bmw_1, bmw_2, bmw_3 = test(med_worst, 'bubble')
print("\t\tWorst case #1:",bmw_1,"seconds.")
print("\t\tWorst case #2:",bmw_2,"seconds.")
print("\t\tWorst case #2:",bmw_3,"seconds.")

print("\n\tLarge list (size:",large,"):\n")

blb_1, blb_2, blb_3 = test(large_best, 'bubble')
print("\t\tBest case #1:",blb_1,"seconds.")
print("\t\tBest case #2:",blb_2,"seconds.")
print("\t\tBest case #2:",blb_3,"seconds.")

bla_1, bla_2, bla_3 = test(large_avg, 'bubble')
print("\t\tAverage case #1:",bla_1,"seconds.")
print("\t\tAverage case #2:",bla_2,"seconds.")
print("\t\tAverage case #2:",bla_3,"seconds.")

blw_1, blw_2, blw_3 = test(large_worst, 'bubble')
print("\t\tWorst case #1:",blw_1,"seconds.")
print("\t\tWorst case #2:",blw_2,"seconds.")
print("\t\tWorst case #2:",blw_3,"seconds.\n")


#####################
#                   #
#    Comb sort      #
#                   #
#####################

# Generate lists for comb sort
small_best, small_avg, small_worst = get_lists(small)
med_best, med_avg, med_worst = get_lists(medium)
large_best, large_avg, large_worst = get_lists(large)

# Call test function for each size and case
# Print Results
print("Comb sort results:\n")
print("\tSmall list (size:",small,"):\n")

csb_1, csb_2, csb_3 = test(small_best, 'comb')
print("\t\tBest case #1:",csb_1,"seconds.")
print("\t\tBest case #2:",csb_2,"seconds.")
print("\t\tBest case #2:",csb_3,"seconds.")

csa_1, csa_2, csa_3 = test(small_avg, 'comb')
print("\t\tAverage case #1:",csa_1,"seconds.")
print("\t\tAverage case #2:",csa_2,"seconds.")
print("\t\tAverage case #2:",csa_3,"seconds.")

csw_1, csw_2, csw_3 = test(small_worst, 'comb')
print("\t\tWorst case #1:",csw_1,"seconds.")
print("\t\tWorst case #2:",csw_2,"seconds.")
print("\t\tWorst case #2:",csw_3,"seconds.")

print("\n\tMedium list (size:",medium,"):\n")

cmb_1, cmb_2, cmb_3 = test(med_best, 'comb')
print("\t\tBest case #1:",cmb_1,"seconds.")
print("\t\tBest case #2:",cmb_2,"seconds.")
print("\t\tBest case #2:",cmb_3,"seconds.")

cma_1, cma_2, cma_3 = test(med_avg, 'comb')
print("\t\tAverage case #1:",cma_1,"seconds.")
print("\t\tAverage case #2:",cma_2,"seconds.")
print("\t\tAverage case #2:",cma_3,"seconds.")

cmw_1, cmw_2, cmw_3 = test(med_worst, 'comb')
print("\t\tWorst case #1:",cmw_1,"seconds.")
print("\t\tWorst case #2:",cmw_2,"seconds.")
print("\t\tWorst case #2:",cmw_3,"seconds.")

print("\n\tLarge list (size:",large,"):\n")

clb_1, clb_2, clb_3 = test(large_best, 'comb')
print("\t\tBest case #1:",clb_1,"seconds.")
print("\t\tBest case #2:",clb_2,"seconds.")
print("\t\tBest case #2:",clb_3,"seconds.")

cla_1, cla_2, cla_3 = test(large_avg, 'comb')
print("\t\tAverage case #1:",cla_1,"seconds.")
print("\t\tAverage case #2:",cla_2,"seconds.")
print("\t\tAverage case #2:",cla_3,"seconds.")

clw_1, clw_2, clw_3 = test(large_worst, 'comb')
print("\t\tWorst case #1:",clw_1,"seconds.")
print("\t\tWorst case #2:",clw_2,"seconds.")
print("\t\tWorst case #2:",clw_3,"seconds.\n")




    
