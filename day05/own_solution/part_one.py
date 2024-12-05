class Solution:

    def solve(self, order_rules, pages):
        result = 0
        for page in pages:
            isCorrect = True
            page = page.split(",")
            for i in range(len(page)):
                for j in range(i + 1, len(page)):
                    combined = page[i] + "|" + page[j]
                    if combined not in order_rules:
                        isCorrect = False
            if isCorrect:
                result += self.getMiddleValue(page)
        print(result)

    def getMiddleValue(self, page):
        middle = page[len(page) // 2]
        middle = int(middle)
        print(middle)
        return middle

    def readInputs(self, order_rules, pages):
        with open(order_rules) as file1:
            order_lines = file1.readlines()
        order_lines = [line.strip() for line in order_lines]

        with open(pages) as file2:
            pages = file2.readlines()
        pages = [line.strip() for line in pages]
        return order_lines, pages


if __name__ == "__main__":

    solution = Solution()
    order_rules, pages = solution.readInputs("../order_rules.txt", "../pages.txt")
    solution.solve(order_rules, pages)