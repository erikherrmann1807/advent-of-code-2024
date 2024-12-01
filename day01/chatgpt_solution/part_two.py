from collections import Counter

class Solution:
    def calculate_total_distance(self, left_list, right_list):
        # Step 1: Count occurrences in the right list
        right_count = Counter(right_list)

        # Step 2: Compute similarity score
        similarity_score = sum(num * right_count[num] for num in left_list)

        return f"Similarity Score: {similarity_score}"

    def readInput(self, filePath: str):
        leftList = []
        rightList = []
        with open(filePath, 'r') as file:
            lines = file.readlines()
            for line in lines:
                sp = line.split()
                leftList.append(int(sp[0]))
                rightList.append(int(sp[1]))
        print(self.calculate_total_distance(leftList, rightList))

if __name__ == '__main__':
    solution = Solution()
    solution.readInput('../input.txt')
