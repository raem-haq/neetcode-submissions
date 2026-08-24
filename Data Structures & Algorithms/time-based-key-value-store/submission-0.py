class TimeMap:

    def __init__(self):
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if timestamp in self.timeMap:
            self.timeMap[timestamp][key] = value
        else:
            self.timeMap[timestamp] = {key : value}

    def get(self, key: str, timestamp: int) -> str:
        t = timestamp
        while t > 0:
            if t in self.timeMap and key in self.timeMap[t]:
                return self.timeMap[t][key]
            t -= 1
        return ""
