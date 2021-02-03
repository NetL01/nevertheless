def merge_sort(rlist, first, last):
    if (last - first) > 0:
        middle = (first + last) // 2
        merge_sort(rlist, first, middle)
        merge_sort(rlist, middle, last)
        func_list_for_merge(rlist, first, middle, last)

def func_list_for_merge(rlist, first, middle, last):
    left = rlist[first:middle]
    right = rlist[middle:last]
    count = first
    i = 0
    j = 0
    while (first + i < middle and middle + j < last):
        if left[i] <= right[j]:
            rlist[count] = left[i]
            i = i + 1

        else:
            rlist[count] = right[j]
            j = j + 1

        count = count + 1
        
        if first + i < middle:
            while count < last:
                rlist[count] = left[i]
                i = i + 1
                count = count + 1

        else:
            while count < end:
                rlist[count] = right[j]
                j = j + 1
                count = count + 1

alist = input().split()
alist = [int(x) for x in alist]
merge_sort(alist, 0, len(alist))
print(rlist)

            
        
