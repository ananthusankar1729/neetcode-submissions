class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(m,len(nums1)):
            nums1.pop()
        for x in nums2:
            nums1.append(x)
        for j in range(len(nums1)-1):
            for i in range(len(nums1)-1):
                if nums1[i]>nums1[i+1]:
                    nums1[i],nums1[i+1] = nums1[i+1],nums1[i]

        

        




        



        


        