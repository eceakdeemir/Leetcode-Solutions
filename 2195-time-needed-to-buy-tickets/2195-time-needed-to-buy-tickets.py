class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        count = 0
        i = 0
        while (i < len(tickets)):
            if (tickets[k] == 0):
                return count
            if (tickets[i] != 0):
                tickets[i] -= 1
                count += 1
            i += 1
            if (i == len(tickets)):
                i = 0
        return c
