import heapq

def min_cost(cables): 
    total_cost = 0
    heapq.heapify(cables)

    while len(cables) > 1:
        cable1 = heapq.heappop(cables)
        cable2 = heapq.heappop(cables)

        cost = cable1 + cable2
        total_cost += cost

        heapq.heappush(cables, cost)

    return total_cost

cables = [1, 2, 3, 4, 5, 6, 7, 8]
result = min_cost(cables)
print(f"Min connection cost: {result}")
