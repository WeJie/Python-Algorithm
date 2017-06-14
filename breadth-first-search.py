# -*- coding:utf-8 -*-

from collections import deque

graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['thom', 'jonny']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []


def find_the_closest_mango_seller(graph, start_man):
    print "searching graph:\n", graph
    print '---------------------'
    search_queue = deque()
    search_queue += graph[start_man]
    while search_queue:
        person = search_queue.popleft()
        print person
        if person_is_seller(person):
            print '---------------------'
            print person + "is a mango seller!"
            return True
        else:
            search_queue += graph[person]
    return False


def person_is_seller(name):
    return name[-1] == 'm'

find_the_closest_mango_seller(graph, 'you')

