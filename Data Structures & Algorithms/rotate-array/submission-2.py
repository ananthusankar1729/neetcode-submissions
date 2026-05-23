class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        z=0
        while z<k:
            nums.insert(0,nums[-1])
            nums.pop()
            z+=1
        return nums