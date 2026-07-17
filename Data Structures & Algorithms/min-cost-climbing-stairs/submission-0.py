class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        a = 0
        b = 0

        for i in range(2, len(cost) + 1):
            cost_onestep = b + cost[i - 1]
            cost_twostep = a + cost[i - 2]
            current_cost = min(cost_onestep, cost_twostep)

            a = b
            b = current_cost

        return b