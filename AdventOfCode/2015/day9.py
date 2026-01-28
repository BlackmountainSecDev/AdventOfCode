import heapq
from itertools import permutations
from unittest import result


def readTheFile(filename):

    try:
        with open(filename, 'r') as lines:
            return lines.read().split('\n')

    except FileNotFoundError:
        return []


def tsp(graph):
    #Travel Salesman Problem
    allNodes = list(graph.keys())

    shortest = float('infinity')
    bestRoute = None

    for route in permutations(allNodes):
        total = 0

        for i in range(len(route)-1):
            total += graph[route[i]][route[i+1]]

        # Ist diese Route besser?
        if total < shortest:
            shortest = total
            best_route = route

    return best_route, shortest


def tsp_reverse(graph):
    #Travel Salesman Problem
    allNodes = list(graph.keys())

    shortest = 0
    bestRoute = None

    for route in permutations(allNodes):
        total = 0

        for i in range(len(route)-1):
            total += graph[route[i]][route[i+1]]

        # Ist diese Route besser?
        if total > shortest:
            shortest = total
            best_route = route

    return best_route, shortest


def part1():
    content = readTheFile('Resources/day9.txt')

    if len(content) == 0:
        print('File not found!')
        return 0

    #building the graph
    graph = {}

    for line in content:
        startPoint, endPointHelper = line.split('to')
        startPoint = startPoint.strip()
        endPoint, distance = endPointHelper.split('=')
        endPoint = endPoint.strip()

        if startPoint not in graph.keys():
            graph[startPoint] = {}

        graph[startPoint][endPoint] = int(distance)


        if endPoint not in graph.keys():
            graph[endPoint] = {}

        graph[endPoint][startPoint] = int(distance)


    bestRoute, distance = tsp(graph)
    print(distance)


def part2():
    content = readTheFile('Resources/day9.txt')

    if len(content) == 0:
        print('File not found!')
        return 0

    #building the graph
    graph = {}

    for line in content:
        startPoint, endPointHelper = line.split('to')
        startPoint = startPoint.strip()
        endPoint, distance = endPointHelper.split('=')
        endPoint = endPoint.strip()

        if startPoint not in graph.keys():
            graph[startPoint] = {}

        graph[startPoint][endPoint] = int(distance)


        if endPoint not in graph.keys():
            graph[endPoint] = {}

        graph[endPoint][startPoint] = int(distance)


    bestRoute, distance = tsp_reverse(graph)
    print(distance)


if __name__ == '__main__':
    part1()
    part2()