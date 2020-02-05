class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ind = [0] * len(arr2)
        record = {}
        left = []
        for i in range(len(arr2)):
            record[arr2[i]] = i

        for num in arr1:
            if num in record.keys():
                ind[record[num]] += 1
            else:
                left.append(num)

        for j in range(1, len(arr2)):
            ind[j] += ind[j - 1]

        ret = [0] * (len(arr1) - len(left))

        for k in range(len(arr1) - 1, -1, -1):
            if arr1[k] in record.keys():
                ret[ind[record[arr1[k]]] - 1] = arr1[k]
                ind[record[arr1[k]]] -= 1
        left.sort()
        return ret + left

