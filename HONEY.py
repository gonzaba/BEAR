import sys
import networkx as nx
from itertools import islice

numberOfGraphs = 0

#List of graphs. NOTE this is only the names of it. NOT the reference to the graph
graphList = []
#Here are the references to each graph created. This DOES NOT contain the names of it
ref = []
#List of attributes to be used for every graph created in the current running instance of BEAR.
attrs = []
#The link between graphList and ref is the index.


#Create graph
def createNewGraph():
    createGraph(input("What is going to be the name of the network? "))
def createGraph(name):
    global numberOfGraphs, ref, graphList
    # Add to the number of graphs one
    numberOfGraphs += 1
    graphName = name

    # While that name is already taken, keep asking the user to use another one
    while graphName in graphList:
        graphName = input("A network with that name already exists. Please choose another one. ")
    #Lets the user add attributes until they type END
    at = input("add a new attribute for this graph. type END when finished: ")
    while (not at == 'END'):
        attrs.append(at)
        at = input("add a new attribute for this graph. type END when finished: ")
    # create a new graph with the name given by the user
    locals()[graphName] = nx.Graph()
    # add the reference to the ref list
    ref.append(locals()[graphName])
    # add the name of the list to the graphList
    graphList.append(graphName)
    print("Created a new network: ", graphName)

def createGraphFromFile(name, fileName):
    global numberOfGraphs, ref, graphList, attrs
    # Add to the number of graphs one
    numberOfGraphs += 1

    graphName = name

    # While that name is already taken, keep asking the user to use another one
    while graphName in graphList:
        graphName = input("A network with that name already exists. Please choose another one. ")

    # create a new graph with the name given by the user
    locals()[graphName] = nx.Graph()
    # add the reference to the ref list
    ref.append(locals()[graphName])
    # add the name of the list to the graphList
    graphList.append(graphName)
    # print(graphList)
    # now its looking for the file
    file = open(fileName, 'r')

    # Read each individual line and create the person
    line1 = file.readline().strip()
    attrs = line1.split(',')
    for line in file:
        if line != '\n':
            line = line.strip()
            person = line.split(',')
            attributes= person[1:]
            locals()[graphName].add_node(person[0], Attributes=attributes)
    file.close()
    print("Created a new network: ", graphName)

def remove(node, graphName):
    global graphList, numberOfGraphs, ref
    graph = getGraph(graphName)
    graph.remove_node(node)
    print("Removed node "+node)

def getGraph(name):
    global graphList, numberOfGraphs, ref
    while name not in graphList:
        name = input("Network does not exists. Please try again. ")
    i = graphList.index(name)
    return ref[i]

def getNode(name):
    global ref
    for graph in ref :
        for node in graph.nodes :
            if(node == name) :
                return node
    print("Node not found")


#View the list graphs that currently exists.
def viewListOfGraphs():
   global graphList, numberOfGraphs
   print("LIST OF NETWORKS")
    #If this is true, then there are no graphs to display
   if numberOfGraphs ==0:
       print("There are no networks. Please create one.")
   else:
       print("There are", end, "= ")
       print(numberOfGraphs, end,"= ")
       print("networks.")
       print("They are", end,"= ")
       print(graphList)

def add(fileName, graphName):
    global attrs
    graph = getGraph(graphName)
    file = open(fileName, 'r')

    # Read each individual line and create the person
    for line in file:
        if line != '\n':
            line = line.strip()
            person = line.split(',')
            attributes = person[1:]
            graph.add_node(person[0], Attributes=attributes)
    file.close()

def addNode(graphName, nodeName):
    global attrs
    graph = getGraph(graphName)
    created= []
    for i in range(1, len(attrs)):
        created.append(input('enter value for '+attrs[i]+": "))
    graph.add_node(nodeName, Attributes=created[0:])
    print("Added node "+nodeName)

def operations(name):
    global graphList
    while name not in graphList:
        print("Network does not exist. Please try again. ")
        return
    print("Network Operations menu. Working on graph"+ name + "\n")
    flag = input('''Choose your option:
                [1] Union with another network
                [2] Disjoint Union with another network
                [3] Directed copy of this network
                [4] Undirected copy of this network.
                [5] Exit menu
                Enter your selection: ''')
    if(flag=='1'):
        union(name)
    elif(flag=='2'):
        disjointUnion(name)
    elif(flag=='3'):
        directedCopy(name)
    elif(flag=='4'):
        undirectedCopy(name)
    else: return



def displayGraph(graphName):
    global graphList, numberOfGraphs, ref
    i = graphList.index(graphName)
    print(ref[i].nodes(data=True))


def union(graph1):
    global graphList, numberOfGraphs, ref
    print("UNION OF NETWORKS")
    index1 =0
    index2 =0
    if numberOfGraphs < 2:
        print("There is only one network. Please create another network.")
    else:
        index1 = graphList.index(graph1)
        print(graphList)
        second = input("Which is the second network? ")
        while second not in graphList:
            second = input("Network does not exist. Please try again. ")
        index2 = graphList.index(second)

        graphName = input("What name will the union of networks have? ")

        numberOfGraphs += 1
        while graphName in graphList:
            graphName = input("A network with that name already exists. Please choose another one. ")

        locals()[graphName] = nx.union(ref[index1],ref[index2])
        ref.append(locals()[graphName])
        graphList.append(graphName)


def disjointUnion(graph1):
    global graphList, numberOfGraphs, ref
    print("DISJOINT UNION OF NETWORKS")
    index1 =0
    index2 =0
    if numberOfGraphs < 2:
        print("There is only one network. Please create another network.")
    else:
        print(graphList)
        index1 = graphList.index(graph1)
        second = input("Which is the second network? ")
        while second not in graphList:
            second = input("Network does not exist. Please try again. ")
        index2 = graphList.index(second)

        graphName = input("What name will the disjoint union of the networks have? ")

        numberOfGraphs += 1
        while graphName in graphList:
            graphName = input("A network with that name already exists. Please choose another one. ")

        locals()[graphName] = nx.disjoint_union(ref[index1],ref[index2])
        ref.append(locals()[graphName])
        graphList.append(graphName)


#convert_to_undirected
#returns  A deepcopy of the graph.
def undirectedCopy(graph1):
    global graphList, numberOfGraphs, ref
    print("UNDIRECTED COPY")
    index1 = 0
    if numberOfGraphs < 1:
        print("A network doesn't exist. Please try again after creating a network.")
    else:
        index1 = graphList.index(graph1)

        graphName = input("What name will the copy have? ")

        numberOfGraphs += 1
        while graphName in graphList:
            graphName = input("A network with that name already exists. Please choose another one. ")

        locals()[graphName] = nx.to_undirected(ref[index1])
        ref.append(locals()[graphName])
        graphList.append(graphName)


#Convert_to_directed
# Returns A directed graph with the same name, same nodes, and with each edge (u,v,data) replaced by two directed edges (u,v,data) and (v,u,data).
def directedCopy(graph1):
    global graphList, numberOfGraphs, ref
    print("DIRECTED COPY")
    index1 = 0
    if numberOfGraphs < 1:
        print("A network doesn't exist. Please try again after creating a network.")
        return
    else:
        while graph1 not in graphList:
            print("Network does not exist. Please try again. ")
            return
        index1 = graphList.index(graph1)

        graphName = input("What name will the copy have? ")

        numberOfGraphs += 1
        while graphName in graphList:
            graphName = input("A network with that name already exists. Please choose another one. ")

        locals()[graphName] = nx.to_directed(ref[index1])
        ref.append(locals()[graphName])
        graphList.append(graphName)



def subgraph():
    global graphList, numberOfGraphs, ref
    print("CREATE SUBNETWORK")
    if numberOfGraphs < 1:
        print("A network doesn't exist. Please create one.")
    else:
        print(graphList)
        first = input("Which network do you want to make a subnetwork? ")
        while first not in graphList:
            first = input("Network does not exists. Please try again. ")
        index1 = graphList.index(first)
        graphName = input("What name will the subnetwork have? ")
        numberOfGraphs += 1
        while graphName in graphList:
            graphName = input("A network with that name already exists. Please choose another one. ")
        # ask the user for the name of the file to use to create the graph
        fileName = input("File name to export list to use: ")
        fileName = fileName+".csv"
        # now its looking for the file
        file = open(fileName, 'r')
        lst = []
        g = nx.Graph()
        # Read each individual line and create the person
        for line in file:
             if line != '\n':
                 line = line.strip()
                 person = line.split(',')
                 personNode = g.add_node(person[0], age=person[1], gender=person[2], grade=person[3], vaccinated=person[4], infected=person[5])
                 lst.append(personNode)
        file.close()
        locals()[graphName] = ref[index1].subgraph(lst)
        ref.append(locals()[graphName])
        graphList.append(graphName)



