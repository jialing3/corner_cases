# walk from bottom right to top left
# consider if current power level is negative

class Solution:
    def update_cell(self, last_cell, current_power):
        return (max(last_cell - current_power, 1)) if current_power > 0 else (last_cell - current_power)
        # can be combined into max(last_cell - current_power, 1), but code becomes less intuitive

    # @param {integer[][]} dungeon
    # @return {integer}
    def calculateMinimumHP(self, dungeon):
        m = len(dungeon)
        n = len(dungeon[0])
        row = [None for _ in range(n)]
        row[-1] = self.update_cell(1, dungeon[-1][-1])
        for j in range(n - 2, -1, -1):
            row[j] = self.update_cell(row[j + 1], dungeon[-1][j])
        for i in range(m - 2, -1, -1):
            row[-1] = self.update_cell(row[-1], dungeon[i][-1])
            for j in range(n - 2, -1, -1):
                if row[j] > row[j + 1]:
                    row[j] = self.update_cell(row[j + 1], dungeon[i][j])
                else:
                    row[j] = self.update_cell(row[j], dungeon[i][j])
        return row[0]
