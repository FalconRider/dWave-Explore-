#IDENTIFICATION DIVISION 

#QUANTUM WASPS  Version 2
# P. Gitschner   October 2020


#  new---------------------------------------------------------
#It came back with # 1 solution only,  I tried 5 times but it always did  5 nests at 1,3,5,7,9.
#till I figure3d it out. I missed the diagonal constaints, from the corners to tree 5 so
#Ok tree 5 is farther away. I get it.

# So this version I get them fussy adding pairs (5,1) (5,3) (5,7) and (5,9)
# ----------------------------------------------------------------

#A deriivative inspired by Victoria G's antennas problem.
#Just for practice at putting what sounds like a real problem into  a Qubo and getting it to run on Leap.
#This may not work or be screwed up logic but what the hay!

#STORY

#Quantum Wasps are territorial. THey will not build a nest next to a tree that already 
#has a Quantum Wasps nest. Farmer Weber has an apple orchard of 9 grid spaced trees.
#How many Wasps nests  can his orchard hold, how many configurations  and what are the tree configurations?

#NOW. I should get 4 nests, 2 possible configs. 4 corners or a 4 mid sides in a cross pattern.
# I'll run it a bunch of times and see if i see both.


#THE GRID
#A 9 node grid like a dial pad
#1   2   3
#4   5   6
#7   8   9

#The array pairs would represent illegible edges.
#Eligible edges would not be noted.
#The array pairs would be (1,2)(2,3)(4,5)(5,6)(7,8)(8,9)(1,4)(2,5)(3,6)(4,7)(5,8)(6,9)
#So 9 nodes, 12 edges




#ENVIROMENT DIVISION 

import networkx as nx
import dwave_networkx as dnx
#import matplotlib.pyplot as plt no plot yet
from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite
sampler = EmbeddingComposite(DWaveSampler())


#DATA DIVISION 


G = nx.Graph()
G.add_edges_from([(1,2),(2,3),(4,5),(5,6),(7,8),(8,9),(1,4),(2,5),(3,6),(4,7),(5,8),(6,9),(5,1), (5,3) ,(5,7), (5,9)])




#PROCEDURE DIVISION 
#yes, this is a Cobol gag ; )

S = dnx.maximum_independent_set(G, sampler=sampler, num_reads = 10)


# anda some Printed output, skip graph for tis version
print("----------------------RETURNED-----------------------------------")
print (" ")
print("Maximum independant set size found this run", len (S))
print (" ")
print (" A Set is - -  ")
print (S)
print("---------------------------------------------------------")
