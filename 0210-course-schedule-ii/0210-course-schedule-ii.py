from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph={i:[] for i in range(numCourses)}
        order=[]
        indegree=[0]*numCourses
        for course,prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course]+=1
        queue=deque([i for i in range(numCourses) if indegree[i]==0])
        completed=0
        while queue:
            node=queue.popleft()
            order.append(node)
            completed+=1
            for neighbor in graph[node]:
                indegree[neighbor]-=1
                if indegree[neighbor]==0:
                    queue.append(neighbor)
        if len(order)==numCourses:
            return order
        return []

        