import networkx as nx

numberOfGraphs = 0

#List of graphs. NOTE this is only the names of it. NOT the reference to the graph
graphList = []
#Here are the references to each graph created. This DOES NOT contain the names of it
ref = []

#The link between graphList and ref is the index.


#Create graph
def createGraph():
        global numberOfGraphs, ref, graphList
        #Add to the number of graphs one
        numberOfGraphs += 1

        graphName = input("What is going to be the name of the graph? \n")

        #While that name is already taken, keep asking the user to use another one
        while graphName in graphList:
            graphName = input("A graph with that name already exists. Please choose another one.\n")

        #create a new graph with the name given by the user
        locals()[graphName]= nx.Graph()
        #add the reference to the ref list
        ref.append(locals()[graphName])
        #add the name of the list to the graphList
        graphList.append(graphName)
        #print(graphList)

        # ask the user for the name of the file to use to create the graph
        fileName = input("File Name to use: \n")
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
                locals()[graphName].add_node(person[0], age=person[1], gender=person[2], grade=person[3], vaccinated=person[4], infected=person[5])
                #print(locals()[graphName].nodes(data=True))
        file.close()

#View the list graphs that currently exists.
def viewListOfGraphs():
   global graphList, numberOfGraphs
    #If this is true, then there are no graphs to display
   if numberOfGraphs ==0:
       print("There are no graphs. Please create one.")
   else:
       print("There are", end =" ")
       print(numberOfGraphs, end =" ")
       print("graphs.")
       print("They are", end =" ")
       print(graphList)


def displayGraph():
    global graphList, numberOfGraphs, ref
    if numberOfGraphs == 0:
        print("There are no graphs. Please create one.")
    print(graphList)
    graphName = input("Which graph do you want to display?\n")
    while graphName not in graphList:
        print("Graph does not exists. Please try again. \n")
    i = graphList.index(graphName)
    print(ref[i].nodes(data=True))


def union():
    global graphList, numberOfGraphs, ref
    index1 =0
    index2 =0
    if numberOfGraphs < 2:
        print("There is only one graph. Please create another graph.")
    else:
        print(graphList)
        first = input("Which is the first graph? \n")
        index1 = graphList.index(first)
        second = input("Which is the second graph? \n")
        index2 = graphList.index(second)

        graphName = input("What name will the union of graphs be?")

        numberOfGraphs += 1
        while graphName in graphList:
            graphName = input("A graph with that name already exists. Please choose another one.\n")

        locals()[graphName] = nx.union(ref[index1],ref[index2])
        ref.append(locals()[graphName])
        graphList.append(graphName)


def disjointUnion():
    global graphList, numberOfGraphs, ref
    index1 =0
    index2 =0
    if numberOfGraphs < 2:
        print("There is only one graph. Please create another graph.")
    else:
        print(graphList)
        first = input("Which is the first graph? \n")
        index1 = graphList.index(first)
        second = input("Which is the second graph? \n")
        index2 = graphList.index(second)

        graphName = input("What name will the disjoint_union of graphs be?")

        numberOfGraphs += 1
        while graphName in graphList:
            graphName = input("A graph with that name already exists. Please choose another one.\n")

        locals()[graphName] = nx.disjoint_union(ref[index1],ref[index2])
        ref.append(locals()[graphName])
        graphList.append(graphName)


#convert_to_undirected
#returns  A deepcopy of the graph.
def undirectedCopy():
    global graphList, numberOfGraphs, ref
    index1 = 0
    if numberOfGraphs < 1:
        print("A graph doesn't exist. Please create one.")
    else:
        print(graphList)
        first = input("Which graph do you want to convert to undirected? \n")
        index1 = graphList.index(first)

        graphName = input("What name will the copy have?")

        numberOfGraphs += 1
        while graphName in graphList:
            graphName = input("A graph with that name already exists. Please choose another one.\n")

        locals()[graphName] = nx.convert_to_undirected(ref[index1])
        ref.append(locals()[graphName])
        graphList.append(graphName)


#Convert_to_directed
# Returns A directed graph with the same name, same nodes, and with each edge (u,v,data) replaced by two directed edges (u,v,data) and (v,u,data).
def directedCopy():
    global graphList, numberOfGraphs, ref
    index1 = 0
    if numberOfGraphs < 1:
        print("A graph doesn't exist. Please create one.")
    else:
        print(graphList)
        first = input("Which graph do you want to convert to directed? \n")
        index1 = graphList.index(first)

        graphName = input("What name will the copy have?")

        numberOfGraphs += 1
        while graphName in graphList:
            graphName = input("A graph with that name already exists. Please choose another one.\n")

        locals()[graphName] = nx.convert_to_directed(ref[index1])
        ref.append(locals()[graphName])
        graphList.append(graphName)



def subgraph():
    global graphList, numberOfGraphs, ref
    if numberOfGraphs < 1:
        print("A graph doesn't exist. Please create one.")
    else:
        print(graphList)
        first = input("Which graph do you want to make a subgraph? \n")
        index1 = graphList.index(first)
        graphName = input("What name will the subgraph have?")
        numberOfGraphs += 1
        while graphName in graphList:
            graphName = input("A graph with that name already exists. Please choose another one.\n")
        # ask the user for the name of the file to use to create the graph
        fileName = input("File name to export list to use: \n")
        # now its looking for the file
        file = open(fileName, 'r')
        lst = []
        # Read each individual line and create the person
        for line in file:
             if line != '\n':
                 line = line.strip()
                 person = line.split(',')
                 lst.append(person)
                 locals()[graphName].add_node(person[0], age=person[1], gender=person[2], grade=person[3], vaccinated=person[4], infected=person[5])
        file.close()
        locals()[graphName] = ref[index1].subgraph(lst)
        ref.append(locals()[graphName])
        graphList.append(graphName)


#testers
createGraph()
createGraph()
displayGraph()
union()
viewListOfGraphs()
displayGraph()
subgraph()

#Create new Graph
#R =nx.Graph()
#Graph is the union of G and M. AKA combining both lists.
#R = nx.union(G,M)

#print (R.nodes(data=True))



