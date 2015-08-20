class Solution:
    def prune(self, cell):
        # fix one variable, maximize the other
        tmp_dict = {}
        for running_total, path_min in cell:
            if running_total not in tmp_dict:
                tmp_dict[running_total] = path_min
            else:
                tmp_dict[running_total] = max(path_min, tmp_dict[running_total])
        cell = tmp_dict.items()
        tmp_dict = {}
        for running_total, path_min in cell:
            if path_min not in tmp_dict:
                tmp_dict[path_min] = running_total
            else:
                tmp_dict[path_min] = max(running_total, tmp_dict[path_min])
        cell = [(v, k) for k, v in tmp_dict.items()]
        return cell


    # @param {integer[][]} dungeon
    # @return {integer}
    def calculateMinimumHP(self, dungeon):
        m = len(dungeon)
        n = len(dungeon[0])

        # each cell contains an array of (running_total, path_min) for all possible paths
        row = [[] for _ in range(n)]
        # first row
        row[0].append((dungeon[0][0], dungeon[0][0]))
        for j in range(1, n):
            for running_total, path_min in row[j - 1]:
                running_total += dungeon[0][j]
                path_min = min(path_min, running_total)
                row[j].append((running_total, path_min))
        # other rows
        for i in range(1, m):
            # first col
            cell = []
            for running_total, path_min in row[0]:
                running_total += dungeon[i][0]
                path_min = min(path_min, running_total)
                cell.append((running_total, path_min))
            row[0] = cell
            # other cols
            for j in range(1, n):
                cell = []
                for running_total, path_min in row[j]:
                    running_total += dungeon[i][j]
                    path_min = min(path_min, running_total)
                    cell.append((running_total, path_min))
                for running_total, path_min in row[j - 1]:
                    running_total += dungeon[i][j]
                    path_min = min(path_min, running_total)
                    cell.append((running_total, path_min))
                # pick the path that could maximize min(path_min, running_total + constant) in the next step
                cell = list(set(cell))
                row[j] = self.prune(cell)

        running_total_s, path_min_s = zip(*row[-1])
        best_global_min = max(path_min_s)
        if best_global_min > 0:
            return 1
        else:
            return 1 - best_global_min
