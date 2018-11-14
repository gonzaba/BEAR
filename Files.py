import networkx as nx

numberOfGraphs = 0
graphList = []

def createGraph():
        global numberOfGraphs
        global graphList
        numberOfGraphs += 1
        graphName = input("What is going to be the name of the graph? \n")

        while graphName in graphList:
            graphName = input("A graph with that name already exists. Please choose another one.\n")

        locals()[graphName]= nx.Graph()
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
                locals()[graphName].add_node(person[0], age=person[1], gender=person[2], grade=person[3], vaccinated=person[4],
                           infected=person[5])

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







createGraph()
viewListOfGraphs()
createGraph()


#Create new Graph
#R =nx.Graph()
#Graph is the union of G and M. AKA combining both lists.
#R = nx.union(G,M)

#print (R.nodes(data=True))



