class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        heap = []
        heapq.heapify(heap)
        for key, value in counts.items():
            heapq.heappush(heap, (-value, key))
        return_list = []
        for _ in range(k):
            return_list.append(heapq.heappop(heap)[1])
        return return_list