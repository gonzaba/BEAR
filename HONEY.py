import sys
import networkx as nx

numberOfGraphs = 0

#List of graphs. NOTE this is only the names of it. NOT the reference to the graph
graphList = []
#Here are the references to each graph created. This DOES NOT contain the names of it
ref = []

#The link between graphList and ref is the index.


#Create graph
def createNewGraph():
    createGraph(input("What is going to be the name of the network? "))

def createGraph(name):
    global numberOfGraphs, ref, graphList
    # Add to the number of graphs one
    numberOfGraphs += 1

    print("CREATE NEW NETWORK")
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

def createGraphFromFile(name, fileName):
    global numberOfGraphs, ref, graphList
    # Add to the number of graphs one
    numberOfGraphs += 1

    print("CREATE NEW NETWORK")
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
    for line in file:
        if line != '\n':
            line = line.strip()
            person = line.split(',')
            # 0- Name
            # 1- Age
            # 2- Gender
            # 3- Grade
            # 4- Vaccinated
            # 5- Infected

            # print(person)
            locals()[graphName].add_node(person[0], age=person[1], gender=person[2], grade=person[3],
                                         vaccinated=person[4], infected=person[5])
            # print(locals()[graphName].nodes(data=True))
    file.close()


def remove(node, graph):
    graph.remove_node(self, name)

def getGraph(name):
    global graphList, ref
    while graphName not in graphList:
        graphName = input("Network does not exists. Please try again. ")

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
    file = open(fileName, 'r')

    # Read each individual line and create the person
    for line in file:
        if line != '\n':
            line = line.strip()
            person = line.split(',')
            # 0- Name
            # 1- Age
            # 2- Gender
            # 3- Grade
            # 4- Vaccinated
            # 5- Infected

            # print(person)
            locals()[graphName].add_node(person[0], age=person[1], gender=person[2], grade=person[3],
                                         vaccinated=person[4], infected=person[5])
            # print(locals()[graphName].nodes(data=True))
    file.close()


def displayGraph(graphName):
    global graphList, numberOfGraphs, ref
    i = graphList.index(graphName)
    print(ref[i].nodes(data=True))


def union():
    global graphList, numberOfGraphs, ref
    print("UNION OF NETWORKS")
    index1 =0
    index2 =0
    if numberOfGraphs < 2:
        print("There is only one network. Please create another network.")
    else:
        print(graphList)
        first = input("Which is the first network? ")
        while first not in graphList:
            first = input("Network does not exists. Please try again. ")
        index1 = graphList.index(first)
        second = input("Which is the second network? ")
        while second not in graphList:
            second = input("Network does not exists. Please try again. ")
        index2 = graphList.index(second)

        graphName = input("What name will the union of networks be? ")

        numberOfGraphs += 1
        while graphName in graphList:
            graphName = input("A network with that name already exists. Please choose another one. ")

        locals()[graphName] = nx.union(ref[index1],ref[index2])
        ref.append(locals()[graphName])
        graphList.append(graphName)


def disjointUnion():
    global graphList, numberOfGraphs, ref
    print("DISJOINT UNION OF NETWORKS")
    index1 =0
    index2 =0
    if numberOfGraphs < 2:
        print("There is only one network. Please create another network.")
    else:
        print(graphList)
        first = input("Which is the first network? ")
        while first not in graphList:
            first = input("Network does not exists. Please try again. ")
        index1 = graphList.index(first)
        second = input("Which is the second network? ")
        while second not in graphList:
            second = input("Network does not exists. Please try again. ")
        index2 = graphList.index(second)

        graphName = input("What name will the disjoint_union of networks be? ")

        numberOfGraphs += 1
        while graphName in graphList:
            graphName = input("A network with that name already exists. Please choose another one. ")

        locals()[graphName] = nx.disjoint_union(ref[index1],ref[index2])
        ref.append(locals()[graphName])
        graphList.append(graphName)


#convert_to_undirected
#returns  A deepcopy of the graph.
def undirectedCopy():
    global graphList, numberOfGraphs, ref
    print("UNDIRECTED COPY")
    index1 = 0
    if numberOfGraphs < 1:
        print("A network doesn't exist. Please create one.")
    else:
        print(graphList)
        first = input("Which network do you want to convert to undirected? ")
        while first not in graphList:
            first = input("Network does not exists. Please try again. ")
        index1 = graphList.index(first)

        graphName = input("What name will the copy have? ")

        numberOfGraphs += 1
        while graphName in graphList:
            graphName = input("A network with that name already exists. Please choose another one. ")

        locals()[graphName] = nx.convert_to_undirected(ref[index1])
        ref.append(locals()[graphName])
        graphList.append(graphName)


#Convert_to_directed
# Returns A directed graph with the same name, same nodes, and with each edge (u,v,data) replaced by two directed edges (u,v,data) and (v,u,data).
def directedCopy():
    global graphList, numberOfGraphs, ref
    print("DIRECTED COPY")
    index1 = 0
    if numberOfGraphs < 1:
        print("A network doesn't exist. Please create one.")
    else:
        print(graphList)
        first = input("Which network do you want to convert to directed? ")
        while first not in graphList:
            first = input("Network does not exists. Please try again. ")
        index1 = graphList.index(first)

        graphName = input("What name will the copy have? ")

        numberOfGraphs += 1
        while graphName in graphList:
            graphName = input("A network with that name already exists. Please choose another one. ")

        locals()[graphName] = nx.convert_to_directed(ref[index1])
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





#Create new Graph
#R =nx.Graph()
#Graph is the union of G and M. AKA combining both lists.
#R = nx.union(G,M)

#print (R.nodes(data=True))



