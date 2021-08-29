def insertion_sort(lister):
    for i in range(1, len(lister)):
        j = i - 1
        temp = lister[i]

        while j >= 0 and temp < lister[j]:
            lister[j + 1] = lister[j]
            j = j - 1
    lister[j + 1] = temp

    return lister