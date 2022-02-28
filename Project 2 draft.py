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
                
def mergeSort(array):
    #placeholder
    return 42069

def quickSort(array):
    #placeholder
    return 42069

def bubbleSort(array):
    #placeholder
    return 42069
 
# Writen by Brian "I got a 'python' for you lol" Cavin
# Generates 3 lists, one presorted, one random, and one reverse sorted
def get_lists(size):
        
    floor = 1
    ceiling = size+1
   
    best = np.arange(floor,ceiling,1)
    avg = np.random.randint(ceiling*-1,ceiling,size)
    worst = np.arange(ceiling-1, floor-1, -1)
    
    return best, avg, worst

# Written by Brian "Testicle puns are still funny to me" Cavin
# Tests a given algorith with the array pased to the function 3 times and returns the times
def test_icles(array, sort_type):
    
    times = []
    
    # Copies the list 3 times so that a sorted array is not passed to a sort function
    arrays = []
    arrays.insert(0,array.copy())
    arrays.insert(1,array.copy())
    arrays.insert(2,array.copy())
    
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
            quickSort(arrays[i])
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

#####################
#                   #
#    Merge sorted   #
#                   #
#####################


# Generate lists for merge sort
small_best, small_avg, small_worst = get_lists(10000)
med_best, med_avg, med_worst = get_lists(100000)
large_best, large_avg, large_worst = get_lists(1000000)

# Call test function for each size and case
# Print Results
print("Merge sort results:\n")
print("\tSmall list (size: 10,000):\n")

msb_1, msb_2, msb_3 = test_icles(small_best, 'merge')
print("\t\tBest case #1:",msb_1,"seconds.")
print("\t\tBest case #2:",msb_2,"seconds.")
print("\t\tBest case #2:",msb_3,"seconds.")

msa_1, msa_2, msa_3 = test_icles(small_avg, 'merge')
print("\t\tAverage case #1:",msa_1,"seconds.")
print("\t\tAverage case #2:",msa_2,"seconds.")
print("\t\tAverage case #2:",msa_3,"seconds.")

msw_1, msw_2, msw_3 = test_icles(small_worst, 'merge')
print("\t\tWorst case #1:",msw_1,"seconds.")
print("\t\tWorst case #2:",msw_2,"seconds.")
print("\t\tWorst case #2:",msw_3,"seconds.")

print("\n\tMedium list (size: 100,000):\n")

mmb_1, mmb_2, mmb_3 = test_icles(med_best, 'merge')
print("\t\tBest case #1:",mmb_1,"seconds.")
print("\t\tBest case #2:",mmb_2,"seconds.")
print("\t\tBest case #2:",mmb_3,"seconds.")

mma_1, mma_2, mma_3 = test_icles(med_avg, 'merge')
print("\t\tAverage case #1:",mma_1,"seconds.")
print("\t\tAverage case #2:",mma_2,"seconds.")
print("\t\tAverage case #2:",mma_3,"seconds.")

mmw_1, mmw_2, mmw_3 = test_icles(med_worst, 'merge')
print("\t\tWorst case #1:",mmw_1,"seconds.")
print("\t\tWorst case #2:",mmw_2,"seconds.")
print("\t\tWorst case #2:",mmw_3,"seconds.")

print("\n\tLarge list (size: 1,000,000):\n")

mlb_1, mlb_2, mlb_3 = test_icles(large_best, 'merge')
print("\t\tBest case #1:",mlb_1,"seconds.")
print("\t\tBest case #2:",mlb_2,"seconds.")
print("\t\tBest case #2:",mlb_3,"seconds.")

mla_1, mla_2, mla_3 = test_icles(large_avg, 'merge')
print("\t\tAverage case #1:",mla_1,"seconds.")
print("\t\tAverage case #2:",mla_2,"seconds.")
print("\t\tAverage case #2:",mla_3,"seconds.")

mlw_1, mlw_2, mlw_3 = test_icles(large_worst, 'merge')
print("\t\tWorst case #1:",mlw_1,"seconds.")
print("\t\tWorst case #2:",mlw_2,"seconds.")
print("\t\tWorst case #2:",mlw_3,"seconds.\n")


#####################
#                   #
#    Quick sorted   #
#                   #
#####################


# Generate lists for quick sort
small_best, small_avg, small_worst = get_lists(10000)
med_best, med_avg, med_worst = get_lists(100000)
large_best, large_avg, large_worst = get_lists(1000000)

# Call test function for each size and case
# Print Results
print("Quick sort results:\n")
print("\tSmall list (size: 10,000):\n")

qsb_1, qsb_2, qsb_3 = test_icles(small_best, 'quick')
print("\t\tBest case #1:",qsb_1,"seconds.")
print("\t\tBest case #2:",qsb_2,"seconds.")
print("\t\tBest case #2:",qsb_3,"seconds.")

qsa_1, qsa_2, qsa_3 = test_icles(small_avg, 'quick')
print("\t\tAverage case #1:",qsa_1,"seconds.")
print("\t\tAverage case #2:",qsa_2,"seconds.")
print("\t\tAverage case #2:",qsa_3,"seconds.")

qsw_1, qsw_2, qsw_3 = test_icles(small_worst, 'quick')
print("\t\tWorst case #1:",qsw_1,"seconds.")
print("\t\tWorst case #2:",qsw_2,"seconds.")
print("\t\tWorst case #2:",qsw_3,"seconds.")

print("\n\tMedium list (size: 100,000):\n")

qmb_1, qmb_2, qmb_3 = test_icles(med_best, 'quick')
print("\t\tBest case #1:",qmb_1,"seconds.")
print("\t\tBest case #2:",qmb_2,"seconds.")
print("\t\tBest case #2:",qmb_3,"seconds.")

qma_1, qma_2, qma_3 = test_icles(med_avg, 'quick')
print("\t\tAverage case #1:",qma_1,"seconds.")
print("\t\tAverage case #2:",qma_2,"seconds.")
print("\t\tAverage case #2:",qma_3,"seconds.")

qmw_1, qmw_2, qmw_3 = test_icles(med_worst, 'quick')
print("\t\tWorst case #1:",qmw_1,"seconds.")
print("\t\tWorst case #2:",qmw_2,"seconds.")
print("\t\tWorst case #2:",qmw_3,"seconds.")

print("\n\tLarge list (size: 1,000,000):\n")

qlb_1, qlb_2, qlb_3 = test_icles(large_best, 'quick')
print("\t\tBest case #1:",qlb_1,"seconds.")
print("\t\tBest case #2:",qlb_2,"seconds.")
print("\t\tBest case #2:",qlb_3,"seconds.")

qla_1, qla_2, qla_3 = test_icles(large_avg, 'quick')
print("\t\tAverage case #1:",qla_1,"seconds.")
print("\t\tAverage case #2:",qla_2,"seconds.")
print("\t\tAverage case #2:",qla_3,"seconds.")

qlw_1, qlw_2, qlw_3 = test_icles(large_worst, 'quick')
print("\t\tWorst case #1:",qlw_1,"seconds.")
print("\t\tWorst case #2:",qlw_2,"seconds.")
print("\t\tWorst case #2:",qlw_3,"seconds.\n")


#####################
#                   #
#    Bubble sorted  #
#                   #
#####################


# Generate lists for bubble sort
small_best, small_avg, small_worst = get_lists(10000)
med_best, med_avg, med_worst = get_lists(100000)
large_best, large_avg, large_worst = get_lists(1000000)

# Call test function for each size and case
# Print Results
print("Bubble sort results:\n")
print("\tSmall list (size: 10,000):\n")

bsb_1, bsb_2, bsb_3 = test_icles(small_best, 'bubble')
print("\t\tBest case #1:",bsb_1,"seconds.")
print("\t\tBest case #2:",bsb_2,"seconds.")
print("\t\tBest case #2:",bsb_3,"seconds.")

bsa_1, bsa_2, bsa_3 = test_icles(small_avg, 'bubble')
print("\t\tAverage case #1:",bsa_1,"seconds.")
print("\t\tAverage case #2:",bsa_2,"seconds.")
print("\t\tAverage case #2:",bsa_3,"seconds.")

bsw_1, bsw_2, bsw_3 = test_icles(small_worst, 'bubble')
print("\t\tWorst case #1:",bsw_1,"seconds.")
print("\t\tWorst case #2:",bsw_2,"seconds.")
print("\t\tWorst case #2:",bsw_3,"seconds.")

print("\n\tMedium list (size: 100,000):\n")

bmb_1, bmb_2, bmb_3 = test_icles(med_best, 'bubble')
print("\t\tBest case #1:",bmb_1,"seconds.")
print("\t\tBest case #2:",bmb_2,"seconds.")
print("\t\tBest case #2:",bmb_3,"seconds.")

bma_1, bma_2, bma_3 = test_icles(med_avg, 'bubble')
print("\t\tAverage case #1:",bma_1,"seconds.")
print("\t\tAverage case #2:",bma_2,"seconds.")
print("\t\tAverage case #2:",bma_3,"seconds.")

bmw_1, bmw_2, bmw_3 = test_icles(med_worst, 'bubble')
print("\t\tWorst case #1:",bmw_1,"seconds.")
print("\t\tWorst case #2:",bmw_2,"seconds.")
print("\t\tWorst case #2:",bmw_3,"seconds.")

print("\n\tLarge list (size: 1,000,000):\n")

blb_1, blb_2, blb_3 = test_icles(large_best, 'bubble')
print("\t\tBest case #1:",blb_1,"seconds.")
print("\t\tBest case #2:",blb_2,"seconds.")
print("\t\tBest case #2:",blb_3,"seconds.")

bla_1, bla_2, bla_3 = test_icles(large_avg, 'bubble')
print("\t\tAverage case #1:",bla_1,"seconds.")
print("\t\tAverage case #2:",bla_2,"seconds.")
print("\t\tAverage case #2:",bla_3,"seconds.")

blw_1, blw_2, blw_3 = test_icles(large_worst, 'bubble')
print("\t\tWorst case #1:",blw_1,"seconds.")
print("\t\tWorst case #2:",blw_2,"seconds.")
print("\t\tWorst case #2:",blw_3,"seconds.\n")


#####################
#                   #
#    Comb sorted    #
#                   #
#####################

# Generate lists for comb sort
small_best, small_avg, small_worst = get_lists(10000)
med_best, med_avg, med_worst = get_lists(100000)
large_best, large_avg, large_worst = get_lists(1000000)

# Call test function for each size and case
# Print Results
print("Comb sort results:\n")
print("\tSmall list (size: 10,000):\n")

csb_1, csb_2, csb_3 = test_icles(small_best, 'comb')
print("\t\tBest case #1:",csb_1,"seconds.")
print("\t\tBest case #2:",csb_2,"seconds.")
print("\t\tBest case #2:",csb_3,"seconds.")

csa_1, csa_2, csa_3 = test_icles(small_avg, 'comb')
print("\t\tAverage case #1:",csa_1,"seconds.")
print("\t\tAverage case #2:",csa_2,"seconds.")
print("\t\tAverage case #2:",csa_3,"seconds.")

csw_1, csw_2, csw_3 = test_icles(small_worst, 'comb')
print("\t\tWorst case #1:",csw_1,"seconds.")
print("\t\tWorst case #2:",csw_2,"seconds.")
print("\t\tWorst case #2:",csw_3,"seconds.")

print("\n\tMedium list (size: 100,000):\n")

cmb_1, cmb_2, cmb_3 = test_icles(med_best, 'comb')
print("\t\tBest case #1:",cmb_1,"seconds.")
print("\t\tBest case #2:",cmb_2,"seconds.")
print("\t\tBest case #2:",cmb_3,"seconds.")

cma_1, cma_2, cma_3 = test_icles(med_avg, 'comb')
print("\t\tAverage case #1:",cma_1,"seconds.")
print("\t\tAverage case #2:",cma_2,"seconds.")
print("\t\tAverage case #2:",cma_3,"seconds.")

cmw_1, cmw_2, cmw_3 = test_icles(med_worst, 'comb')
print("\t\tWorst case #1:",cmw_1,"seconds.")
print("\t\tWorst case #2:",cmw_2,"seconds.")
print("\t\tWorst case #2:",cmw_3,"seconds.")

print("\n\tLarge list (size: 1,000,000):\n")

clb_1, clb_2, clb_3 = test_icles(large_best, 'comb')
print("\t\tBest case #1:",clb_1,"seconds.")
print("\t\tBest case #2:",clb_2,"seconds.")
print("\t\tBest case #2:",clb_3,"seconds.")

cla_1, cla_2, cla_3 = test_icles(large_avg, 'comb')
print("\t\tAverage case #1:",cla_1,"seconds.")
print("\t\tAverage case #2:",cla_2,"seconds.")
print("\t\tAverage case #2:",cla_3,"seconds.")

clw_1, clw_2, clw_3 = test_icles(large_worst, 'comb')
print("\t\tWorst case #1:",clw_1,"seconds.")
print("\t\tWorst case #2:",clw_2,"seconds.")
print("\t\tWorst case #2:",clw_3,"seconds.\n")




    
