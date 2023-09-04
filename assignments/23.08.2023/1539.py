class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        num = 1
        missing = 0
        for num in range(1, len(arr) + k + 1):
            if num not in arr:
                missing += 1
                if missing == k:
                    return num
        return num + k - missing