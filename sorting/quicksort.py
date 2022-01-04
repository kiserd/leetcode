
def quicksort(arr, low, high):
    # base case handled implicitly
    if low < high:
        # get our partitioning index
        p_idx = partition(arr, low, high)
        # perform quicksort on elements to the left
        # and right of sorted index (p_idx)
        quicksort(arr, low, p_idx - 1)
        quicksort(arr, p_idx + 1, high)
        

def partition(arr, low, high):
    # let pivot element be at high index
    pivot = arr[high]
    i = low - 1
    # loop through indices
    for j in range(low, high, 1):
        # handle case where elt belongs to left of pivot
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    # place pivot to right of i
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1