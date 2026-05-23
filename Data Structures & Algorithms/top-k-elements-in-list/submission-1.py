class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        x = set(nums)
        hashSet = {}
        li = []
        for i in nums:
            hashSet[i] = 1 + hashSet.get(i,0)
        for i in range(k):
            l = max(hashSet.values())
            for key in hashSet:
                if hashSet[key] == l:
                    li.append(key)
                    del hashSet[key]
                    break
        return li
            