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
fileName2 = input("SECOND")

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
    # 3- Birth Place
    # 4- Current Location
    # 5- Number of Vaccines
    # 6- Race
    # 7- Last Trip
    # 8-Place Last Visited

        #print(person)
        G.add_node(person[0], age = person[1], gender = person[2], birthplace = person[3], currentLocation = person[4], numVaccines = person[5], race = person[6], lastTrip = person[7], placeVisited = person[8])



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
        # 3- Birth Place
        # 4- Current Location
        # 5- Number of Vaccines
        # 6- Race
        # 7- Last Trip
        # 8-Place Last Visited

        # print(person)
        M.add_node(person[0], age=person[1], gender=person[2], birthplace=person[3], currentLocation=person[4],
                   numVaccines=person[5], race=person[6], lastTrip=person[7], placeVisited=person[8])

file.close()


R =nx.Graph()
R = nx.union(G,M)

print (R.nodes(data=True))


