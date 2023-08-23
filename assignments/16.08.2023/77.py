class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k == 0:
            return [[]]
        
        result = []
        
        def generate_combinations(index, current):
            if len(current) == k:
                result.append(current)
                return
            
            for i in range(index, n + 1):
                generate_combinations(i + 1, current + [i])
        
        generate_combinations(1, [])
        return result