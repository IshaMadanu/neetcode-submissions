class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = [] #monotonic increasing
        for index, temp in enumerate(temperatures):
            while len(stack) > 0 and temp > stack[-1][0]:
                stackTemp, stackIndex = stack.pop()

                result[stackIndex] = index - stackIndex
            stack.append((temp, index))
        return result

        #iterate thru temps w index
        # while temp in temps> stack's largest temp
            # get prev warmest day with increasing stack
            # add diff in indiceis to result
            # add warmest day to top stack + index

        #stack = wwiting line for needs higher temps