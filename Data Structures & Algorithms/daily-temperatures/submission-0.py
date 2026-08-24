from random import randint
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # if out[i] = 0 then if t[i-1] > t[i] then out[i] = 0
        # if t[i] < t[i+1] then out[i] = 1
        #if t[i] > t[i+1] then check t[i] > t[i+out[i]+1]

        out = [0] * (len(temperatures))
        for i in range(len(temperatures) - 2, -1, -1):
            check_index = i + 1
            while check_index < len(temperatures):
                if temperatures[i] < temperatures[check_index]:
                    out[i] = check_index - i
                    break
                if out[check_index] == 0:
                    out[i] = 0
                    break
                check_index += out[check_index]
        return out
