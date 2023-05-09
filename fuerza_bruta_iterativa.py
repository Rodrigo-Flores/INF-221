def f(arr):
    l = 0
    
    for j in range(len(arr)):
        for i in range(len(arr)):
            if not i <= j:
                print(arr[j], arr[i])
                if (arr[j] > arr[i]):
                    print(arr[j], arr[i], sep=" > ")
                    l += 1
                    print(arr)
                    arr.insert(0, arr[i])
                    print(arr, i)
                    arr.pop(i+1) # float('inf')
                    break

    return l

# arr = [3,4,5,1]
# arr = [3,4,6,1,5,8,7]
# arr = [1,8,9,2]
# arr = [6,1,2,3,4,5]

# print(f(arr))

def f2(arr):
    l = 0
    
    for j in range(len(arr)):
        for i in range(len(arr)):
            if not i <= j:
                print(arr[j], arr[i])
                if (arr[j] > arr[i]):
                    a=j
                    b=i
                    if i ==len(arr):
                        print(a,b,"aaa")
                        l += 1
                        print(arr)
                        arr.insert(0, arr[b])
                        print(arr, b)
                        arr.pop(b+1) # float('inf')
                        break

    return l

# arr = [6,1,2,3,4,5]

# print(f2(arr))

def f3(arr):
    print(arr)
    times = 0
    r = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            # print(arr)
            if j > i:
                if  arr[i] < arr[j]:
                    print(arr)
                    print(arr[i], arr[j], sep=" < ")
                    times += 1
                    arr.insert(i, arr[j])
                    # arr.insert(j, float('inf'))
                    arr.pop(j+1)
                    break
                
                if i == (len(arr) - 1):
                    # arr.append(arr[i])
                    # arr.append(float('inf'))
                    arr.pop(i+1)
                    break
            
    return times

# arr = [3,4,5,1]
# arr = [3,4,6,1,5,8,7]
arr = [1,8,9,2]
# arr = [6,1,2,3,4,5]
# arr = [1,2,3]
print(f3(arr[::-1]))
