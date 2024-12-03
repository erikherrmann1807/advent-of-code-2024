import re

class Solution:

    def checkPattern(self, pattern: str, input: str):
        matches = re.findall(pattern, input)
        print(matches)
        return matches

    def solveInstructions(self, instructions: list):
        pairs = []
        mul = []
        enabled = True
        for instruction in instructions:
            if 'do()' in instruction:
                enabled = True
            elif "don't()" in instruction:
                enabled = False
            elif 'mul' in instruction and enabled:
                temp = re.findall(r'\d+', instruction)
                res = list(map(int, temp))
                pairs.append(res)
        for pair in pairs:
            mul.append(pair[0] * pair[1])
        result = sum(mul)
        print(result)

    def readInput(self, filePath: str):
        with open(filePath, 'r') as file:
            file_content = ''
            line = file.readline()
            while line:
                file_content += line
                line = file.readline()
        return file_content

if __name__ == "__main__":
    pattern = r'mul\(\d+,\d+\)|do\(\)|don\'t\(\)'
    solution = Solution()
    solution.solveInstructions(solution.checkPattern(pattern, solution.readInput('../input.txt')))