class TimeMap:

    def __init__(self):
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key] = []
        
        self.timeMap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ""
        L = 0 
        R = len(self.timeMap[key]) - 1 
        res = ""

        while L <= R:
            mid = L + (R-L)//2

            if self.timeMap[key][mid][1] > timestamp:
                R = mid - 1
            else:
                res = self.timeMap[key][mid][0] #save res (as it is either for timestamp or less)
                L = mid + 1

        return res 
        
