def merge_sort(list):
    n = len(list)
    if n > 1:
        mid = n // 2
        left = list[:mid]
        right = list[mid:]

        merge_sort(left)
        merge_sort(right)
        merge(left,right,list)

def merge(left, right, list):
    i=0
    j=0
    k=0
    while i < len(left) and j<len(right):
        if left[i] <= right[j]:
            list[k] = left[i]
            i+=1
        else:
            list[k] = right[j]
            j+=1
        k+=1
    if i==len(left):
        for element in right[j:]:
            list[k]=element
            k+=1
    else:
        for element in left[i:]:
            list[k]=element
            k+=1


if __name__ == "__main__":

    lister = [8,4,23,42,16,15]
    print(lister)
    merge_sort(lister)
    print(lister)