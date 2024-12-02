from typing import List


# Used copilot for part two, because I was stuck on how to implement the solution
class Solution:

    def is_safe_report(self, report: List[int]) -> bool:
        is_increasing = all(i < j for i, j in zip(report, report[1:]))
        is_decreasing = all(i > j for i, j in zip(report, report[1:]))
        is_safe = all(1 <= abs(i - j) <= 3 for i, j in zip(report, report[1:]))
        return (is_increasing or is_decreasing) and is_safe

    def reportsCheck(self, report: List[int]) -> int:
        if self.is_safe_report(report):
            return 1

        for i in range(len(report)):
            modified_report = report[:i] + report[i+1:]
            if self.is_safe_report(modified_report):
                return 1

        return 0

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