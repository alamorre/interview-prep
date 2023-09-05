from typing import List 

class Course:
    def __init__(self, num, prereqs):
        self.num = num
        self.prereqs = prereqs
        
class Solution:
    def has_cycle(self, course, checked, ancestors):
        if checked[course.num]:
            return False
        if ancestors[course.num]:
            return True

        has_cycle = False
        ancestors[course.num] = True
        for prereq in course.prereqs:
            if self.has_cycle(prereq, checked, ancestors):
                has_cycle = True
                break # cycle found
        ancestors[course.num] = False
        
        checked[course.num] = True
        return has_cycle # no cycles
        
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Create a list of course objects
        course_objs = []
        for course_num in range(0, numCourses):
            cource_obj = Course(course_num, [])
            course_objs.append(cource_obj)
        
        # Add course pre-reqs for each Course object
        for prereq in prerequisites:
            latter_course = course_objs[prereq[0]]
            prereq_course = course_objs[prereq[1]]
            latter_course.prereqs.append(prereq_course) 
            
        # Look for cycles for each course
        ancestors = [False] * numCourses
        checked = [False] * numCourses
        for course_obj in course_objs:
            if self.has_cycle(course_obj, checked, ancestors):
                return False
        
        # No course is part of a cycle
        return True

print(Solution().canFinish(100, [[1,0],[2,0],[2,1],[3,1],[3,2],[4,2],[4,3],[5,3],[5,4],[6,4],[6,5],[7,5],[7,6],[8,6],[8,7],[9,7],[9,8],[10,8],[10,9],[11,9],[11,10],[12,10],[12,11],[13,11],[13,12],[14,12],[14,13],[15,13],[15,14],[16,14],[16,15],[17,15],[17,16],[18,16],[18,17],[19,17],[19,18],[20,18],[20,19],[21,19],[21,20],[22,20],[22,21],[23,21],[23,22],[24,22],[24,23],[25,23],[25,24],[26,24],[26,25],[27,25],[27,26],[28,26],[28,27],[29,27],[29,28],[30,28],[30,29],[31,29],[31,30],[32,30],[32,31],[33,31],[33,32],[34,32],[34,33],[35,33],[35,34],[36,34],[36,35],[37,35],[37,36],[38,36],[38,37],[39,37],[39,38],[40,38],[40,39],[41,39],[41,40],[42,40],[42,41],[43,41],[43,42],[44,42],[44,43],[45,43],[45,44],[46,44],[46,45],[47,45],[47,46],[48,46],[48,47],[49,47],[49,48],[50,48],[50,49],[51,49],[51,50],[52,50],[52,51],[53,51],[53,52],[54,52],[54,53],[55,53],[55,54],[56,54],[56,55],[57,55],[57,56],[58,56],[58,57],[59,57],[59,58],[60,58],[60,59],[61,59],[61,60],[62,60],[62,61],[63,61],[63,62],[64,62],[64,63],[65,63],[65,64],[66,64],[66,65],[67,65],[67,66],[68,66],[68,67],[69,67],[69,68],[70,68],[70,69],[71,69],[71,70],[72,70],[72,71],[73,71],[73,72],[74,72],[74,73],[75,73],[75,74],[76,74],[76,75],[77,75],[77,76],[78,76],[78,77],[79,77],[79,78],[80,78],[80,79],[81,79],[81,80],[82,80],[82,81],[83,81],[83,82],[84,82],[84,83],[85,83],[85,84],[86,84],[86,85],[87,85],[87,86],[88,86],[88,87],[89,87],[89,88],[90,88],[90,89],[91,89],[91,90],[92,90],[92,91],[93,91],[93,92],[94,92],[94,93],[95,93],[95,94],[96,94],[96,95],[97,95],[97,96],[98,96],[98,97],[99,97]]))

"""
I do believe this solution is still fine bc it's O(n)
Two builder loops and a DFS on a DAG

Use this example to build a DAG
- checked base case -> return false
- ancestors base case -> return true
- since numCourses is like 100 max just make a flat list (set would work too)
Why would checked and answers both be needed?
"""
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {} # node: neighbours
        for num in range(numCourses):
            graph[num] = []
        for prerequisite in prerequisites:
            graph[prerequisite[1]].append(prerequisite[0])
                    
        def backtrack_is_dag(num, path) -> bool:
            nonlocal graph
            if num in path: return False # cycle!
            path.add(num)
            for neighbour in graph[num]:
                if not backtrack_is_dag(neighbour, path):
                    return False
            path.remove(num)
            return True

        for num in range(numCourses):
            if not backtrack_is_dag(num, set()):
                return False
        return True
        