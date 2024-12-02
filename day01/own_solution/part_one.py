from typing import List


class Solution:

    def twoSum(self, leftList: List[int], rightList: List[int]) -> int:
        distance = 0
        leftList.sort()
        rightList.sort()
        for i, leftElement in enumerate(leftList):
            distance += abs(leftElement - rightList[i])
        return distance

    def readInput(self, filePath: str):
        leftList = []
        rightList = []
        with open(filePath, 'r') as file:
            lines = file.readlines()
            for line in lines:
                sp = line.split()
                leftList.append(int(sp[0]))
                rightList.append(int(sp[1]))
        print(self.twoSum(leftList, rightList))


if __name__ == '__main__':
    solution = Solution()
    solution.readInput('../input.txt')