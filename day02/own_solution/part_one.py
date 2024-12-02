from typing import List

class Solution:

    def reportsCheck(self, report: List[int]) -> int:
        sum_safes = 0

        is_increasing = all(i < j for i, j in zip(report, report[1:]))
        is_decreasing = all(i > j for i, j in zip(report, report[1:]))

        if is_increasing or is_decreasing:
            is_safe = all(1 <= abs(i - j) <= 3 for i, j in zip(report, report[1:]))
            if is_safe:
                sum_safes += 1
        return sum_safes

    def readInput(self, filePath: str):
        reports = []
        with open(filePath, 'r') as file:
            lines = file.readlines()
            for line in lines:
                reports.append(list(map(int, line.split())))
        return reports


if __name__ == "__main__":
    solution = Solution()
    reports = solution.readInput('../input.txt')
    print(sum(solution.reportsCheck(report) for report in reports))
