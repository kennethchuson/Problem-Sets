def solve(graph):

    res = ""
    res2 = ""
    sub_one = []
    sub_two = []
    count_empty = 0 
    for row in range(len(graph)):
        for col in range(len(graph[row])):
            dfs = explore(row, col, len(graph), len(graph[0]), graph)
            if dfs != 0:
                res = str(dfs) + "#"
                sub_one.append(res)
            else:
                count_empty += 1
                res2 = str(count_empty) + "."
                
    sub_two.append(res2) 
    return [sub_one, sub_two]


def explore(row, col, n, m, graph):
    
    size = 1 
    
    if row < 0 or col < 0 or row >= n or col >= m or graph[row][col] == ".":
        return 0
    
    graph[row][col] = "."


    size += explore(row + 1, col, n, m, graph)
    size += explore(row, col + 1, n, m, graph)
    size += explore(row - 1, col, n, m, graph)
    size += explore(row, col - 1, n, m, graph)

    return size




graph = [
    [".", "#", ".", "."],
    [".", "#", ".", "#"],
    [".", ".", ".", "#"],
    ["#", ".", "#", "#"],
    ["#", "#", ".", "."],
]



out = solve(graph)

print(out)
