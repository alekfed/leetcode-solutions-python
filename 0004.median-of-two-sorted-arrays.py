class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        def kth(nums1, nums2, k, s1, e1, s2, e2):
            if s1 >= e1:
                return nums2[s2+k]
            if s2 >= e2:
                return nums1[s1+k]
            if k == 0:
                return min(nums1[s1], nums2[s2])

            m = (e1+s1)/2
            n = (e2+s2)/2

            if (m-s1)+(n-s2) < k:
                if nums1[m] < nums2[n]:
                    return kth(nums1, nums2, k-(m-s1)-1, m+1, e1, s2, e2)
                return kth(nums1, nums2, k-(n-s2)-1, s1, e1, n+1, e2)
            if nums1[m] < nums2[n]:
                return kth(nums1, nums2, k, s1, e1, s2, n)
            return kth(nums1, nums2, k, s1, m, s2, e2)

        m = len(nums1)
        n = len(nums2)
        length = m+n

        if length % 2 == 0:
            return ((kth(nums1, nums2, length/2-1, 0, m, 0, n) +
                     kth(nums1, nums2, length/2, 0, m, 0, n))/2.0)
        return kth(nums1, nums2, length/2, 0, m, 0, n)
