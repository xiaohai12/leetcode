

def Median(arr):
    if len(arr) < 1:
        return None
    elif len(arr) == 1:
        return arr[0]
    else:
        if len(arr)%2==0:
            addition = arr.copy()
            addition.append(max(addition))
            return (Quicksort(arr, 0, len(arr) - 1) + Quicksort(addition, 0, len(addition) - 1))/2
        return Quicksort(arr, 0, len(arr) - 1)


def Quicksort(arr, start, end):
    base = arr[start]
    s = start
    e = end
    if (start < end):
        while (s < e):
            while (s < end and arr[s] <= base):
                s += 1
            while (e > start and arr[e] >= base):
                e -= 1
            if (s < e):
                tmp = arr[s]
                arr[s] = arr[e]
                arr[e] = tmp
            else:
                break

        if base > arr[e]:
            arr[start] = arr[e]
            arr[e] = base
        if (e == (len(arr) - 1) / 2):
            return arr[e]
        elif (e < (len(arr) - 1) / 2):
            return Quicksort(arr, e + 1, end)
        else:
            return Quicksort(arr, start, e - 1)
    else:
        return arr[start]

arr = [4,5,1,2,]
print(Median(arr))