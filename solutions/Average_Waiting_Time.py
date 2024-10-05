class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        available_time = 0
        total_wait = 0
        for arrival, time in customers:
            available_time = max(available_time, arrival) + time
            total_wait += available_time - arrival
        
        return total_wait / len(customers)