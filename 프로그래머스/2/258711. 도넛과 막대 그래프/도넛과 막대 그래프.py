def solution(edges):
    
    def convertNodeData(edges):
        nodes = {}
        for a,b in edges:
            if not nodes.get(a):
                nodes[a] = [0,0]
            if not nodes.get(b):
                nodes[b] = [0,0]
            nodes[a][0] += 1 # 나가는 거
            nodes[b][1] += 1 # 들어가는 거
        
        return nodes
    def findSolution(nodes):
        answer = [0,0,0,0]
        
        for key, values in nodes.items():
            if values[0] >= 2 and values[1] == 0:
                answer[0] = key
            elif values[0] == 0 and values[1] > 0:
                answer[2] += 1
            elif values[0] >= 2 and values[1] >= 2:
                answer[3] += 1
        answer[1] = (nodes[answer[0]][0] - answer[2] - answer[3])
        return answer
    nodes = convertNodeData(edges)
    
        
    return findSolution(nodes)