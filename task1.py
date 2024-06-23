import heapq

def min_cost_to_connect_cables(cables):
    heapq.heapify(cables)  # Convert the list of cables into a heap
    total_cost = 0

    while len(cables) > 1:
        # Extract the two shortest cables
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        cost = first + second
        total_cost += cost
        # Add the combined cable back into the heap
        heapq.heappush(cables, cost)
    
    return total_cost

# Example usage:
cables = [4, 3, 2, 6]
print("Minimum cost to connect cables:", min_cost_to_connect_cables(cables))