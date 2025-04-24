# 4-node cycle graph (C4) -  bipartite
graph = {
    0: [1, 3],
    1: [0, 2],
    2: [1, 3],
    3: [0, 2]
}

# This graph would return false (not bipartite - it has an odd cycle)
# graph = {
#     0: [1, 2],
#     1: [0, 2],
#     2: [0, 1]
# }

#Two Disconnected Components
#graph = {
#    0: [1],
#    1: [0],
#    2: [3],
#    3: [2]
#}

#Odd Cycle (C5)
#graph = {
#    0: [1, 4],
#    1: [0, 2],
#    2: [1, 3],
#    3: [2, 4],
#    4: [3, 0]
#}