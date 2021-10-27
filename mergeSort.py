# program to sort an array using mergeSort Algorithm
import timeit
def merge(arr,start,end,mid):
    l = (mid - start) + 1
    r = end - mid
    # L = arr[:mid]
    # R = arr[mid:]
    L,R = [],[]
    for i in range(0,l):
        L.append(arr[start+i])
    for j in range(0,r):
        R.append(arr[(mid+1)+j])
    i = 0
    j = 0
    k = start
    length = len(arr)
    while(i < len(L) and j < len(R)):
        if (L[i] <= R[j]):
            arr[k] = L[i]
            i +=1
        else:
            arr[k] = R[j]
            j+=1
        k+=1
    while(i < len(L)):
        arr[k] = L[i]
        i +=1
        k +=1
    while(j < len(R)):
        arr[k] = R[j]
        j +=1
        k +=1


def mergeSort(arr,start,end):
    if start < end:
        mid = (start + end)//2
        mergeSort(arr,start,mid)
        mergeSort(arr,mid+1,end)
        merge(arr,start,end,mid)


arr = [11668, 557, 6333, 11501, 1545, 10006, 18211, 8189, 1152, 19266, 444444]
start = timeit.default_timer()
mergeSort(arr,0,len(arr)-1)
end   = timeit.default_timer()
print(arr)
print(end-start)
