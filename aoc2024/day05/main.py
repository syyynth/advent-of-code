from collections import defaultdict, deque

with open('input.txt') as f:
    data = f.read().split('\n\n')
    pairs = [tuple(map(int, line.split('|'))) for line in data[0].splitlines()]
    updates = [list(map(int, line.split(','))) for line in data[1].splitlines()]


def build_graph(pairs, update):
    graph = defaultdict(list)
    in_degree = defaultdict(int)

    update_set = set(update)
    for u, v in pairs:
        if u in update_set and v in update_set:
            graph[u].append(v)
            in_degree[v] += 1
            in_degree.setdefault(u, 0)

    return graph, in_degree


def topological_sort(graph, in_degree):
    queue = deque([node for node in in_degree if in_degree[node] == 0])
    topo_order = []

    while queue:
        node = queue.popleft()
        topo_order.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(topo_order) != len(in_degree):
        raise ValueError('Cycle detected in the graph')

    return topo_order


def process_update(update, pairs):
    graph, in_degree = build_graph(pairs, update)
    topo_order = topological_sort(graph, in_degree)
    index = {page: idx for idx, page in enumerate(topo_order)}

    for i in range(len(update) - 1):
        if index[update[i]] > index[update[i + 1]]:
            return False, topo_order[len(update) // 2]

    return True, topo_order[len(update) // 2]


def solve():
    part1_sum = 0
    part2_sum = 0

    for update in updates:
        is_valid, middle_page = process_update(update, pairs)

        if is_valid:
            part1_sum += middle_page
        else:
            part2_sum += middle_page

    return part1_sum, part2_sum


part1, part2 = solve()
print(f'part 1: {part1}')
print(f'part 2: {part2}')
