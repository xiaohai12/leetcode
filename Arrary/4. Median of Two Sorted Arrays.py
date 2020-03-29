class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)
        if n > m:  ## make sure nums1 > nums2
            m, n = n, m
            nums1, nums2 = nums2, nums1
        if n == 0:
            if m % 2 == 1:
                return nums2[int(m / 2)]
            else:
                return (nums2[int(m / 2)] + nums2[int(m / 2) - 1]) / 2

        mid = int((n + m + 1) / 2)
        imin = 0
        imax = n
        while imin <= imax:
            i = int((imax + imin) / 2)
            j = mid - i
            if i > 0 and nums1[i - 1] > nums2[j]:
                imax = i - 1
            elif i < n and nums1[i] < nums2[j - 1]:
                imin = i + 1
            else:
                if i == 0:
                    left = nums2[j - 1]
                elif j == 0:
                    left = nums1[i - 1]
                else:
                    left = max(nums1[i - 1], nums2[j - 1])

                if (m + n) % 2 == 1:
                    return left
                else:
                    if i == n:
                        right = nums2[j]
                    elif j == m:
                        right = nums1[i]
                    else:
                        right = min(nums1[i], nums2[j])
                    return (left + right) / 2


