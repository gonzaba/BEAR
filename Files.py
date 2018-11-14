import networkx as nx

numberOfGraphs = 0
graphList = []
ref = []

def createGraph():
        global numberOfGraphs, ref
        global graphList
        numberOfGraphs += 1
        graphName = input("What is going to be the name of the graph? \n")

        while graphName in graphList:
            graphName = input("A graph with that name already exists. Please choose another one.\n")

        locals()[graphName]= nx.Graph()
        ref.append(locals()[graphName])
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

def viewListOfGraphs():
   global graphList, numberOfGraphs

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




createGraph()
createGraph()
displayGraph()
union()
viewListOfGraphs()
displayGraph()

#Create new Graph
#R =nx.Graph()
#Graph is the union of G and M. AKA combining both lists.
#R = nx.union(G,M)

#print (R.nodes(data=True))



