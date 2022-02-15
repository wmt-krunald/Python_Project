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


l = [3, 10, 15, 21, 323, 2512]
target = 2512
result1 = naive_search(l, target)
result2 = binary_search(l, target, 0, len(l)-1)

print("\nNaive Search = ", str(result1))
print("\nBinary Search = ", str(result2))

#   ###### METHOD : 2 ######   #

# l = [2, 3, 10, 15, 21, 32, 323, 2512]
# print("l = [2, 3, 10, 15, 21, 32, 323, 2512]")
# target = int(input("\nEnter the number from list, want to know Index : "))
# result1 = naive_search(l, target)
# result2 = binary_search(l, target, 0, len(l)-1)

# print("\nNaive Search = ", str(result1))
# print("\nBinary Search = ", str(result2))
