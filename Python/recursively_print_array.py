def print_array(arr, index=0):
    if index == len(arr):
        return
    print(arr[index])
    print_array(arr, index + 1)

print_array([1, 2, 3, 4, 5])