import random
import time
# Implementation of Binary Search !!!!
# We will prove that binary search is faster than Naive Search!!

# Naive Search: Scan entire list and ask if its equal to the target
# If YES --> return the Index
# If NO  --> return -1

def naive_search(l, target):
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1

def binary_search(l, target, low, high):

    if high >= low:

        mid = (low + high) // 2

        if l[mid] == target:
            return mid
        
        elif l[mid] > target:
            return binary_search(l, target, low, mid-1)
        
        else:
            return binary_search(l, target, mid+1, high)
    else:
        return -1


length = 10000
sorted_list = set()

while len(sorted_list) < length:
    sorted_list.add(random.randint(-3*length, 3*length))
sorted_list = sorted(list(sorted_list))

start = time.time()
for target in sorted_list:
    naive_search(sorted_list, target)
end = time.time()
print("\nNaive Search takes time is ",  (end - start)/length ," seconds.")

start = time.time()
for target in sorted_list:
    binary_search(sorted_list, target, 0, len(sorted_list) - 1)
end = time.time()
print("\nBinary Search takes time is ( In Seconds ) : ", (end - start)/length)