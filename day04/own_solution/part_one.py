# Solved this one using copilot's help
class Solution:
    def count_word_occurrences(self, grid, word):
        rows = len(grid)
        cols = len(grid[0])
        word_len = len(word)

        directions = [
            (0, 1), (0, -1), (1, 0), (-1, 0),
            (1, 1), (1, -1), (-1, 1), (-1, -1)
        ]

        def search_from(x, y, dx, dy):
            for i in range(word_len):
                nx, ny = x + i * dx, y + i * dy
                if nx < 0 or ny < 0 or nx >= rows or ny >= cols or grid[nx][ny] != word[i]:
                    return False
            return True

        count = 0
        for i in range(rows):
            for j in range(cols):
                for dx, dy in directions:
                    if search_from(i, j, dx, dy):
                        count += 1

        return count

    def read_input(self, file_path):
        with open(file_path, "r") as file:
            return [line.strip() for line in file]

if __name__ == "__main__":
    solution = Solution()
    print(solution.count_word_occurrences(solution.read_input("../input.txt"), "XMAS"))