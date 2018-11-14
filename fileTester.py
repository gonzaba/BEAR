"""
This example is creating a graph that is centered around behaviors of diseases.
We are verifying where the connection might be. (If from the last place visited and/if
the number of vaccines a person has helps prevent getting the disease.
"""
import networkx as nx


#Create empty graph with no nodes and no edges
G=nx.Graph()
M =nx.Graph()

#ask the user for the name of the file to use to create the graph
fileName = input("Complete File Name to use: \n")
fileName2 = input("Second File Name to use: \n")

#now its looking for the file
file = open(fileName, 'r')

#Read each individual line and create the person
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
        G.add_node(person[0], age=person[1], gender=person[2], grade=person[3], vaccinated=person[4],infected=person[5])


file.close()

#print G.nodes(data=True)

# now its looking for the file
file = open(fileName2, 'r')

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
        M.add_node(person[0], age=person[1], gender=person[2], grade=person[3], vaccinated=person[4], infected=person[5])

file.close()

#Create new Graph
R =nx.Graph()
#Graph is the union of G and M. AKA combining both lists.
R = nx.union(G,M)

print (R.nodes(data=True))



