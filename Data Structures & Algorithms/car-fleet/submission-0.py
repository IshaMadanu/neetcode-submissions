class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [[p, s] for p, s in zip(position, speed)] #list comprhension
        stack = []
        #sort array of paris + reverse order
        for p, s in sorted(pairs)[:: -1]:
            first = (target - p) / s
            stack.append(first)
            if len(stack) > 1 and stack[-1] <= stack[-2]: #if stack has atl 2 items and if the latest car is faster than car before it
                stack.pop()
        return len(stack)


        # stack = []
        # for i in range(len[speed] - 1, -1, -1):
        #     stack.append([position[i], speed[i]])
        #     first = stack[0]
        #     second = stack[1]
        #     if (target - first[0]) / first[1] >= (target - second[0]) / second[1]:
        #         stack.pop()
            