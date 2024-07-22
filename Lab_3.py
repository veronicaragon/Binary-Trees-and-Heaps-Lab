from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Helper function to check if a binary tree is complete
def is_complete(node, index=0, count=0):
    if not node:
        return True
    
    queue = deque([node])
    while queue:
        node = queue.popleft()
        if not node:
            break  # Encountered a gap in the tree
        queue.append(node.left)
        queue.append(node.right)
    
    # Check if there are any non-None nodes left in the queue
    while queue:
        if queue.popleft():
            return False  # Non-None nodes found after encountering a None
    return True

# Problem 1: Determine if a binary tree is a min heap
def is_min_heap(node):

    while node is not None:
        if node.left is not None and node.left.val < node.val:
            return False
        if node.right is not None and node.right.val < node.val:
            return False
        return is_min_heap(node.left) and is_min_heap(node.right) and is_complete(node)
    return True


# Problem 2: Given the level-order traversal of a binary tree, determine if its is a min heap
def lvl_order(arr):
    n = len(arr)
    i = 0
    while i < n:
        if arr[i] is None:
            break
        left_child = 2 * i + 1
        right_child = 2 * i + 2

        if left_child < n and (arr[left_child] is not None and arr[left_child] < arr[i]):
            return False

        if right_child < n and (arr[right_child] is not None and arr[right_child] < arr[i]):
            return False

        i += 1

    # Ensure that the remaining elements after the first occurrence of None are all None
    while i < n:
        if arr[i] is not None:
            return False
        i += 1

    return True

# Problem 3: Implement Heap Sort
def heapify(heap, n, i):  
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left child
    r = 2 * i + 2  # right child

    # Check if left child exists and is greater than the root
    if l < n and heap[l] > heap[largest]: 
        largest = l 

    # Check if right child exists and is greater than the largest so far
    if r < n and heap[r] > heap[largest]: 
        largest = r 

    # If largest is not root, swap it with the largest and heapify the affected subtree
    if largest != i: 
        heap[i], heap[largest] = heap[largest], heap[i] 
        heapify(heap, n, largest) 

    return heap

def heap_sort(arr):
    n = len(arr)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)

    return arr

# Test cases
# Problem 1 Test case 1: A min heap
#        2
#      /   \
#     3     4
root1 = TreeNode(2)
root1.left = TreeNode(3)
root1.right = TreeNode(4)
print("Problem 1 Test 1: \nExpected: True \nOutput:", is_min_heap(root1))

# Problem 1 Test case 2: Not a min heap
#        2
#      /   \
#           3
root2 = TreeNode(2)
root2.right = TreeNode(3)
print("\nProblem 1 Test 2: \nExpected: False \nOutput:", is_min_heap(root2))

# Problem 2 Test case 1: Min heap
arr1 = [1,2,10,3,77,11,12]
print("\nProblem 2 Test 1: \nExpected: True \nOutput:", lvl_order(arr1))

# Problem 2 Test case 2: Not a min heap
arr2 = [1,2,4,5,6,7, None,8]
print("\nProblem 2 Test 2: \nExpected: False \nOutput:", lvl_order(arr2))

# Problem 3 Test case 1: 
arr3 = [12, 11, 13, 5, 6, 7]
print("\nProblem 3 Test 1: \nExpected: [5, 6, 7, 11, 12, 13] \nOutput:  ",heap_sort(arr3))
print("The time complexity of heap sort is O(n log n) in the average and worst-case scenarios.")
