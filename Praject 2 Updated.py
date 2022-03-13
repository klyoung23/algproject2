# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 15:42:54 2022

@authors: Kal Young, Brian Cavin, Landon Johnson
"""

########## RANDOM ARRAY ##########



import random
import time as t


########## ARRAY GENERATION ##########

# Returns a sorted array
def sortedArray(size):
    
    array = []
    for i in range(size):
        array.append(i+1)
    
    return array

# Returns a random array
def randArray(size):
    k = size*2
    array = []
    for i in range(size):
        array.append(random.randint(size*-1, k))
    
    return array

# Returns a reverse sorted array
def reverseArray(size):
    
    num = size
    array = []
    for i in range(size):
        array.append(num)
        num = num -1
    
    return array

########## COMB SORT FUNCTIONS ##########

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


########## MERGE SORT FUNCTIONS ##########

# Merge Sort

def merge_sort(m):
    if len(m) <= 1:
        return m
 
    middle = len(m) // 2
    left = m[:middle]
    right = m[middle:]
 
    left = merge_sort(left)
    right = merge_sort(right)
    return list(merge(left, right))

def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0
    while left_idx < len(left) and right_idx < len(right):
        # change the direction of this comparison to change the direction of the sort
        if left[left_idx] <= right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
 
    if left_idx < len(left):
        result.extend(left[left_idx:])
    if right_idx < len(right):
        result.extend(right[right_idx:])
    return result

########## QUICK SORT ##########

# Partition

def partition(array, low, high):
    i = (low-1)
    pivot = array[high]
 
    for j in range(low, high):
        
        if array[j] <= pivot:
            i = i+1
            array[i], array[j] = array[j], array[i]
 
    array[i+1], array[high] = array[high], array[i+1]
    return (i+1)

# Quick Sort
 
def quickSortIterative(arr,l,h):
  
    # Create an auxiliary stack
    size = h
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

########## BUBBLE SORT ##########

def bubbleSort(array,size):

    for i in range(size-1):

        for j in range(0, size-i-1):
            
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    

########## DRIVER CODE ##########



'''''''''''''''''''''''

Below code used for writing the data to a text file. The top "with open" was the file path 
on Brian Cavin's computer. The commented out "with open" below that is the default path for instructor use.

'''''''''''''''''''''''
with open("C:/Users/xiii8/OneDrive/Documents/Spring 2022/Algorithms/Time Complexity Analysis.txt", 'w') as f:
#with open("Time Complexity Analysis.txt", 'w') as f:
    
    f.write("Algorithms Project 2 - Time Complexity Analysis and Comparison\n")
    f.write("Authors:")
    f.write("\n\tKal Young\n\tBrian Cavin\n\tLandon Johnson\n")
    
    # Variable Declaration and initialization
    sizechoice = 0
    array = [None]
    size = 0
    test_num = 0
    # Quick Sort variables
    low = 0    
    high = array.__len__()-1
    
    # Size Selection
    while sizechoice != "7":
        
        print("\n1. Smallest Array = 100\n2. Small Array = 1,000\n3. Medium Array = 2,500\n4. Extra-Medium Array = 5,000\n5. Large Array = 7,500\n6. Largest Array = 10,000\n7. Exit.")
        sizechoice = input("Please select an array size: ")
        
        # User input from menu determines array size used
        if sizechoice == "1":
            size = 100
        elif sizechoice == "2":
            size = 1000
        elif sizechoice == "3":
            size = 2500
        elif sizechoice == "4":
            size = 5000
        elif sizechoice == "5":
            size = 7500
        elif sizechoice == "6":
            size = 10000
        # Exit choice
        elif sizechoice == "7":
            break
        
        
        
        # Case Selection
        print ("1. Best Case (Presorted)\n2. Average Case (Randomly sorted)\n3. Worst Case (Reverse sorted)\n4. Exit")
        sortchoice = input("Please select a sort: ")
        
        # User input from menu determines conditions of array (best, average, worst)
        if sortchoice == "1":
            array = sortedArray(size)
            case = "Best - presorted"
                    
        elif sortchoice == "2":
            array = randArray(size)
            case = "Average - randomly sorted"
                    
        elif sortchoice == "3":
            array = reverseArray(size)
            case = "Worst - reverse sorted"
        # Exit choice
        elif sortchoice == "4":
            break
        
        # Make copies of array to send to each sort method
        comb_array = array
        merge_array = array
        bubble_array = array
        quick_array = array
        
        
        t0 = t.perf_counter()
        combSort(comb_array)
        t1 = t.perf_counter()
        comb_time = t1-t0
        
        
        t0 = t.perf_counter()
        merge_array = merge_sort(merge_array)
        t1 = t.perf_counter()
        merge_time = t1-t0
        
        t0 = t.perf_counter()
        quickSortIterative(quick_array, 0, array.__len__()-1)
        t1 = t.perf_counter()
        quick_time = t1-t0
        
        t0 = t.perf_counter()
        bubbleSort(bubble_array,size)
        t1 = t.perf_counter()
        bubble_time = t1-t0
        

        
        test_num = test_num + 1
        print("Test number",test_num)
        print("Array size:",size)
        print("Case:",case)
        
        f.write("\nTest # " + str(test_num) + ":\n")
        f.write("\tArray size: " + str(size) + "\n")
        f.write("\tCase: " + case + "\n\n")
        

        print("Comb sort time:",comb_time,"seconds.")
        f.write("\tComb sort time: " + str(comb_time) + " seconds.\n")

        print("Merge sort time:",merge_time,"seconds.")
        f.write("\tMerge sort time: "+ str(merge_time) + " seconds.\n")

        print("Bubble sort time:",bubble_time,"seconds.")
        f.write("\tBubble sort time: " + str(bubble_time) + " seconds.\n")

        print("Quick sort time:",quick_time,"seconds.")
        f.write("\tQuick sort time: " + str(quick_time) + " seconds.\n")
        
    
    print("Goodbye!")
