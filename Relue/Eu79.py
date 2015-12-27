# should have done a topological sort

class Solution:
    def __init__(self):
        self.keylog = self.get_keylog()
        self.first, self.last, self.all_nums, self.count_of_n1_before_n2 = self.get_first_last_and_counts()
        self.guess = [self.first, self.last]

    def check(self):
        for k in self.keylog:
            inds = []
            for num in k:
                if num in self.guess:
                    inds.append(self.guess.index(num))
                else:
                    print(k)
                    break
            if sorted(inds) != inds:
                print(k)
        else:
            print('check passed')

    def make_a_guess(self):
        last = self.guess.pop()
        candidates = self.all_nums

        for i in range(6):
            candidates.remove(self.guess[i])
            flags = {} # flags[n1][n2] indicates whether n1 can go before n2
            for n1 in candidates:
                if n1 != last:
                    flags[n1] = {}
                for n2 in candidates:
                    if n1 != n2 and last not in (n1, n2):
                        n1_before_n2 = self.count_of_n1_before_n2[n1].get(n2, 0)
                        n2_before_n1 = self.count_of_n1_before_n2[n2].get(n1, 0)
                        flags[n1][n2] = True if n1_before_n2 >= n2_before_n1 else False
            selected = list(filter(lambda x: all(x[1].values()), flags.items()))[0][0]
            self.guess.append(selected)

        self.guess.append(last)
        print(''.join(self.guess))
        return

    def get_keylog(self):
        keylog = set()
        with open('p079_keylog.txt') as f:
            for row in f.readlines():
                row = tuple(list(row.strip()))
                keylog.add(row)
        return sorted(keylog)

    def get_first_last_and_counts(self):
        count_of_n1_before_n2 = {}
        non_first = set()
        non_last = set()
        all_nums = set()
        
        for k in self.keylog:
            for n1, n2 in zip(k[:-1], k[1:]):
                if n1 not in count_of_n1_before_n2:
                    count_of_n1_before_n2[n1] = {}
                if n2 not in count_of_n1_before_n2[n1]:
                    count_of_n1_before_n2[n1][n2] = 0
                count_of_n1_before_n2[n1][n2] += 1
            for n in k[1:]:
                non_first.add(n)
            for n in k[:-1]:
                non_last.add(n)
            for n in k:
                all_nums.add(n)

        first = (all_nums - non_first).pop()
        last = (all_nums - non_last).pop()
        return first, last, all_nums, count_of_n1_before_n2

if __name__ == '__main__':
    sol = Solution()
    sol.make_a_guess()
    sol.check()
