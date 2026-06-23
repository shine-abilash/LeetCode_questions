class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        ml, nl, mnl = m - 1, n - 1, m + n - 1
        while ml >= 0 and nl >= 0:
            if nums1[ml] > nums2[nl]:
                nums1[mnl] = nums1[ml]
                ml -= 1
            else:
                nums1[mnl] = nums2[nl]
                nl -= 1
            mnl -= 1
        
        while nl>=0:
            nums1[mnl]=nums2[nl]
            nl-=1
            mnl-=1
