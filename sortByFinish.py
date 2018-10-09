
def partition(arr,low,high):
    i = low-1         # index of smaller element
    #print("high =",high)
    pivot = arr[high].finish     # pivot
    aux = None

    for j in range(low , high):
        # If current element is smaller than or
        # equal to pivot
        if   arr[j].finish <= pivot:
            # increment index of smaller element
            i = i+1
            aux = arr[i]
            arr[i] = arr[j]
            arr[j] = aux
    aux = arr[i+1]
    arr[i+1] = arr[high]
    arr[high] = aux

    return (i+1)

# The main function that implements quickSortFim
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index

# Function to do Quick sort
def quickSortFim(arr,low,high):
    if low < high:
        # pi is partitioning index, arr[p] is now at right place
        pi = partition(arr,low,high)
        # Separately sort elements before partition and after partition
        arr = quickSortFim(arr, low, pi-1)
        arr = quickSortFim(arr, pi+1, high)
    return arr

def sortByFinish(list):
    return quickSortFim(list,0,len(list)-1)













#
