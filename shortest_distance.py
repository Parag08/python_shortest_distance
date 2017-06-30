graph = {'A':[{'B':1},{'C':5}],'B':[{'C':3},{'D':8}],'C':[{'A':5},{'E':3}],'D':[{'E':2},{'F':1},{'G':2}],'E':[{'F':4}],'F':[{'G':1},{'H':6}],'G':[{'H':4}],'H':[]}
#graph = {'A':[{'B':1},{'C':5}],'B':[{'C':3},{'D':8}],'C':[{'E':3}],'D':[{'E':2},{'F':1},{'G':2}],'E':[{'F':4}],'F':[{'G':1},{'H':6}],'G':[{'H':4}],'H':[]}
inf = 9999999
shortest_path = ''
shortest_distance = inf

def traverse(graph,distances,node,point_B,path):
    if (path.find(node) > 0):
        return
    else:
        path = path +'-'+ node
        distance = distances[node]
        for val in graph[node]:
            key,value = val.items()[0]
            if (distances[key]  > value + distance):
                 distances[key] = value + distance
            traverse(graph,distances,key,point_B,path)
        if(node == point_B):
            print path
            if (distances[point_B] < shortest_distance):
                global shortest_path 
                shortest_path  = path + '-]'
                global shortest_distance
                shortest_distance = distances[point_B]
            return



def find_shortest_distance(graph,point_A,point_B):
    distances = {}
    found_point_A = False
    found_point_B = False
    path = '['
    for val in graph:
        distances[val] = inf
        if(val == point_A):
            distances[val] = 0
            found_point_A = True
        elif(val == point_B):
            found_point_B = True
    if(found_point_B or found_point_A):
        traverse(graph,distances,'A',point_B,path)
        return distances[point_B]
    else:
        raise NameError("point_A or point_B not found")
        return


print(find_shortest_distance(graph,'A','H'))
print(shortest_path)
