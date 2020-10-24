# P. Gitschner   October 2020
# Given a pyramid.  10 nodes. 4 levels. Goal = No adjacencies on perimeter only.

# POSSIBLE STORY: Post minimum senties to patrol around 3 sided 9 tower perimeter. 
# Assigned every second watchtower to patrol back and forth 
# between start tower and next highest two protecting central building #5.

#Viz	     1
#        2       3				
#     4      5*      6
# 7       8      9      10

import networkx as nx
import dwave_networkx as dnx
from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite

sampler = EmbeddingComposite(DWaveSampler())


G = nx.Graph()
# clockwize from 1
G.add_edges_from([(1,3),(3,6),(6,10),(10,9),(9,8),(8,7),(7,4),(4,2),(2,1)])



S = dnx.maximum_independent_set(G, sampler=sampler, num_reads = 10)

print("----------------------------------------")
print("Minimum Sentry set size     ", len (S))
print ("Starting Tower Assignments this run   ",S)
print("----------------------------------------")
