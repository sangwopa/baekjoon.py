import sys

V, E = map(int,sys.stdin.readline().split())
K = str(sys.stdin.readline()).strip()

graph = {}

for i in range(V):
    graph[str(i+1)] = {}
    
for i in range(E):
    div = list(map(int,sys.stdin.readline().split()))
    graph[str(div[0]).strip()][str(div[1]).strip()] = div[2]

import heapq

def dijkstra(graph, first):
    distance = {node:float('inf') for node in graph}
    distance[first] = 0 # 첫 번째 노드거리 0    
    queue = []
    heapq.heappush(queue, [distance[first], first]) # 우선순위 큐에 첫번째 값 넣어줌

    # queue에 데이터 없을 때 까지 반복
    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if distance[current_node] < current_distance: # 우선순위 큐의 값이 더 클경우 반복문 실행할 필요 없음
            continue

        for next_node, weight in graph[current_node].items():
            total_distance = current_distance + weight

            if total_distance < distance[next_node]:
                distance[next_node] = total_distance
                heapq.heappush(queue, [total_distance, next_node])

    return distance

con = dijkstra(graph, K)

for i in range(len(con)):
    if con[str(i+1)] == float('inf'):
        print('INF')
    else:
        print(con[str(i+1)])