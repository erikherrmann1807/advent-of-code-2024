class Solution:
    def calculate_total_distance(self, left_list, right_list):
        # Sort both lists
        left_sorted = sorted(left_list)
        right_sorted = sorted(right_list)

        # Calculate the total distance
        total_distance = sum(abs(l - r) for l, r in zip(left_sorted, right_sorted))

        return total_distance

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
