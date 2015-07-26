# cycle detection
# example: 4, [[0,1],[3,1],[1,3],[3,2]]

class Solution:
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {boolean}
    def canFinish(self, numCourses, prerequisites):
        if numCourses < 2 or len(prerequisites) < 2: # no cycle
            return True

        while True:
            can_trim = False
            visited = [False] * numCourses

            for course_pair in prerequisites:
                visited[course_pair[0]] = True # mark courses dependent on others

            for course_pair in prerequisites:
                if visited[course_pair[1]] is False: # not dependent on others
                    can_trim = True
                    prerequisites.remove(course_pair) # start deleting from the end

            if prerequisites==[]: # everything is trimmed away
                return True
            elif not can_trim: # things are NOT trimmed away but can more trimming be done?
                return False   
