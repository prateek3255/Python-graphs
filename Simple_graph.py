import path
from anaconda_navigator.static.fonts import PATH
class Graph:
    
    graph_dict={}
    
    def addEdge(self,node,neighbour):  
        if node not in self.graph_dict:
            self.graph_dict[node]=[neighbour]
        else:
            self.graph_dict[node].append(neighbour)
            
    def show_edges(self):
        for node in self.graph_dict:
            for neighbour in self.graph_dict[node]:
                print("(",node,", ",neighbour,")")
    
    def find_path(self,start,end,path=[]):
        path = path + [start]  
        if start==end:
            return path
        for node in self.graph_dict[start]:
            if node not in path:
                newPath=self.find_path(node,end,path)
                if newPath:
                    return newPath
                return None
    
    def BFS(self,s):
        visited={}
        for i in self.graph_dict:
            visited[i]=False
        queue=[]
        queue.append(s)
        visited[s]=True
        while len(queue)!=0:
            s=queue.pop(0)
            for node in self.graph_dict[s]:
                if visited[node]!=True:
                    visited[node]=True
                    queue.append(node)
            print(s,end=" ")
            
    def All_Paths(self,start,end,path=[]):
        path = path + [start]
        if start == end:
            return [path]
        paths = []
        for node in self.graph_dict[start]:
            if node not in path:
              newpaths = self.All_Paths(node, end, path)
              for newpath in newpaths:
                paths.append(newpath)
        return paths
    
    def Shortest_Path(self,start,end,path=[]):
        path=path+[start]
        if start==end:
            return path
        shortest=None
        for node in self.graph_dict[start]:
            if node not in path:
                newpath=self.Shortest_Path(node, end, path)
                if newpath:
                    if not shortest or len(shortest)>len(newpath):
                        shortest=newpath
        return shortest
    
    def DFS(self,s):
        visited={}
        for i in self.graph_dict:
            visited[i]=False
        stack=[s]
        visited[s]=True
        while stack:
            n=stack.pop(len(stack)-1)
            for i in self.graph_dict[n]:
                if not visited[i]:
                    stack.append(i)
                    visited[i]=True
            print(n)
        
        
        
g= Graph()
g.addEdge('1', '2')
g.addEdge('1', '3')
g.addEdge('2', '3')
g.addEdge('2', '1')
g.addEdge('3', '1')
g.addEdge('3', '2')
g.addEdge('3', '4')
g.addEdge('4', '3')
g.DFS('1')
