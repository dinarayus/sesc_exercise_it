

INF = 9999999
# number of vertices in graph
N = 10
# creating graph by adjacency matrix method
    # A  B  C  D  E  F  G  H  I  K
G = [[0, 4, 3, 2, 0, 0, 0, 0, 0, 0], # A
    [4, 0, 2, 0, 1, 0, 0, 0, 0, 0],  # B
    [3, 2, 0, 6, 6, 4, 6, 0, 0, 0],  # C
    [2, 0, 6, 0, 0, 0, 4, 0, 0, 0],  # D
    [0, 1, 6, 0, 0, 3, 0, 1, 0, 8],  # E
    [0, 0, 4, 0, 3, 0, 3, 0, 2, 4],  # F
    [0, 0, 6, 4, 0, 3, 0, 0, 6, 0],  # G
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 1],  # H
    [0, 0, 0, 0, 0, 2, 6, 0, 0, 10], # I
    [0, 0, 0, 0, 8, 4, 0, 1, 10, 0]] # K

selected_node = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
no_edge = 0

selected_node[0] = True

# printing for edge and weight
print("Edge : Weight\n")
while (no_edge < N-1):

    minimum = INF
    a = 0
    b = 0
    for m in range(N-1):
        if selected_node[m]:
            for n in range(N):
                if ((not selected_node[n]) and G[m][n]):
                    # not in selected and there is an edge
                    if minimum > G[m][n]:
                        minimum = G[m][n]
                        a = m
                        b = n
    print(str(a) + "-" + str(b) + ":" + str(G[a][b]))
    selected_node[b] = True
    no_edge += 1

