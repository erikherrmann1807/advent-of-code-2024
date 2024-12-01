from typing import List


class Solution:

    def similarityScore(self, leftList: List[int], rightList: List[int]) -> int:
        similarityScore = 0
        for i in leftList:
            counter = 0
            for j in rightList:
                if i == j:
                    counter += 1
            similarityScore += i * counter
        return similarityScore

    def readInput(self, filePath: str):
        leftList = []
        rightList = []
        with open(filePath, 'r') as file:
            lines = file.readlines()
            for line in lines:
                sp = line.split()
                leftList.append(int(sp[0]))
                rightList.append(int(sp[1]))
        print(self.similarityScore(leftList, rightList))


if __name__ == '__main__':
    solution = Solution()
    solution.readInput('input.txt')