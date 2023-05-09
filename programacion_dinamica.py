# def fb(arr, memo={}):
#     n = arr[0] # extract the length of the array
#     if n == 1: # if the array has only one element it is already sorted
#         return 0
#     if arr == sorted(arr[1:]): # if the array is already sorted
#         return 0
#     key = tuple(arr) # convert the array to a hashable tuple to use as a key for the memo dictionary
#     if key in memo: # if we have already solved this subproblem, return the stored result
#         return memo[key]
#     min_moves = float('inf') # initialize the minimum number of moves to infinity
#     for i in range(n-1): # try every possible pair of adjacent elements to swap
#         if arr[i+1] < arr[i]: # if the adjacent pair is not sorted
#             arr[i], arr[i+1] = arr[i+1], arr[i] # swap the elements
#             moves = fb(arr, memo) # recursively solve for the modified array
#             min_moves = min(min_moves, 1 + moves) # update the minimum number of moves
#             arr[i], arr[i+1] = arr[i+1], arr[i] # swap the elements back (undo the modification)
#     memo[key] = min_moves # store the minimum number of moves for this subproblem
#     return min_moves

def fb(arr, memo={}):
    n = arr[0] # extract the length of the array
    if n == 1: # if the array has only one element it is already sorted
        return 0
    if arr == sorted(arr[1:]): # if the array is already sorted
        return 0
    if tuple(arr) in memo: # if the result for this subproblem has been computed before
        return memo[tuple(arr)]
    min_moves = float('inf') # initialize the minimum number of moves to infinity
    for i in range(n-1): # try every possible pair of adjacent elements to swap
        if arr[i+1] < arr[i]: # if the adjacent pair is not sorted
            arr[i], arr[i+1] = arr[i+1], arr[i] # swap the elements
            moves = fb(arr, memo) # recursively solve for the modified array
            min_moves = min(min_moves, 1 + moves) # update the minimum number of moves
            arr[i], arr[i+1] = arr[i+1], arr[i] # swap the elements back (undo the modification)
    memo[tuple(arr)] = min_moves # store the result for this subproblem
    return min_moves

if __name__ == "__main__":
    # arr = [5,3,4,6,8,7] # 1
    # arr = [4,4,2,1,3] # 2
    # arr = [6,6,1,2,3,4,5] # 1
    arr = [4,1,8,9,2] # 1
    print(fb(arr))
    