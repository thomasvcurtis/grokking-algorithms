def sum_array(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr[0] + sum_array(arr[1:])

print(sum_array([1,2,3]))

def count_items(arr):
    if len(arr) == 0:
        return 0
    else:
        return 1 + count_items(arr[1:])



print(count_items([1,2,3]))
