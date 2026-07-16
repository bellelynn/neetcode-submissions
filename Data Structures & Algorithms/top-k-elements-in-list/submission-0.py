class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = collections.Counter(nums)

        heap = []
        for num, freq in count_map.items():
            heapq.heappush(heap, (freq, num))    

            if len(heap) > k:
                heapq.heappop(heap)

        return [pair[1] for pair in heap]