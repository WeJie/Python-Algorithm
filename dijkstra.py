#! /usr/env/bin python

graph = {
    "start": {
        "a": 6,
        "b": 2
    },
    "a": {
        "fin": 1
    },
    "b": {
        "a": 3,
        "fin": 5
    },
    "fin": {}
}

infinity = float("inf")
costs = {
    "a": 6,
    "b": 2,
    "fin": infinity
}

parents = {
    "a": "start",
    "b": "start",
    "fin": None
}

processed = []

def dijktra():
    """ find lowest cost path"""

    node = find_lowest_cost_node(costs)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                # update neighbor's cost
                costs[n] = new_cost
                # set current node as the lowset cost neighbor's parent 
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs)
    trace(parents, 'fin')
     

def find_lowest_cost_node(costs): 
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

def trace(parents, final_point):
    print final_point
    node = final_point
    while parents.get(node, None):
        node = parents.get(node, None)
        print node 
    print 'trace done'

if __name__ == '__main__':
    dijktra()




