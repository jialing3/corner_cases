# LIFO

# the problem should be understood as any number of adjacent '/'s should be replaced with '/'

class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        while '//' in path:
            path = path.replace('//', '/')
        path = path.strip('/').split('/')
        simplified = []
        for current in path:
            if current == '.':
                continue
            elif current == '..':
                if len(simplified):
                    simplified.pop()
                else:
                    simplified = [] # root
            else:
                simplified.append(current)
        return '/' + '/'.join(simplified)
