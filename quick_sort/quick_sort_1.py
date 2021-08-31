def quick_sort(list, left, right):
    if left < right:
        postition = partition(list,left,right)
        quick_sort(list, left, postition-1)
        quick_sort(list, postition+1, right)

def partition(list, left, right):
    pivot=list[right]
    low=left-1
    for i in range(left, right):
        if list[i] <= pivot:
            low += 1
            swap(list, i, low)
    swap(list, right, low + 1)
    return low + 1
    
def swap(list, i, low):
    temp = list[i]
    list[i] = list[low]
    list[low] = temp


if __name__ == "__main__":
    lister = [8,4,23,42,16,15]
    print(lister)
    quick_sort(lister,0,len(lister)-1)
    print(lister)    



