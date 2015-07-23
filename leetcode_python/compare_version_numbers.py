class Solution:
    # @param {string} version1
    # @param {string} version2
    # @return {integer}
    def compareVersion(self, version1, version2):
        version1 = [int(_) for _ in version1.split('.')]
        version2 = [int(_) for _ in version2.split('.')]
        return self.recurse(version1, version2)


    def recurse(self, version1, version2):
        if version1 == [] and version2 == []:
            return 0
        elif version1 == []:
            if version2[0] == 0:
                return 0
            else:
                return -1
        elif version2 == []:
            if version1[0] == 0:
                return 0
            else:
                return 1
        else:
            if version1[0] < version2[0]:
                return -1
            elif version1[0] > version2[0]:
                return 1
            else:
                return self.recurse(version1[1:], version2[1:])
