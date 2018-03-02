# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 11:56:26 2018

@author: Kristin
"""

"""
Imports a directionally connected nodes list

(E.g. physics citations (used by class 5 of Coursera's: Algorithmic Thinking, Rice University)
"""

# general imports
import urllib
import matplotlib.pyplot as plt
import numpy as np
from Collections import Counter
#%matplotlib inline
###################################

# Code for loading citation graph
CITATION_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_phys-cite.txt"


def load_digraph(graph_url):
    """
    Function that loads a directional node graph given the URL
    for a text representation of the graph
    
    Returns a dictionary that models a digraph
    """
    
    graph_file = urllib.request.urlopen(graph_url)
    graph_lines = graph_file.readlines()
    graph_lines = graph_lines[ : -1]
    
    print("Loaded graph with", len(graph_lines), "nodes")
    
    digraph = {}
    #convert first item in each line to a from_node
    # and all other items in a line to to_nodes 
    # output format = {from_node: {to_nodes}}
    for line in graph_lines:
        to_nodes = line.split()
        from_node = int(to_nodes[0])
        digraph[from_node] = set([])
        for to_node in to_nodes[1 : -1]:
            digraph[from_node].add(int(to_node))

    return digraph


def compute_degrees(graph):
    """
    Function determines counts of directional node
    connections for each node - an "in-degree distribution" 
    for the network.
    
    Returns a list of counts per node
    """
    counts = dict([(x,0) for x in graph])
    for key,values in graph.items():
        counts[key]=len(values)
    counts = {key:value for key, value in counts.items() if value > 0}
    return counts
        
def plot_in_degrees(counts,name):
    """
    Plot the degrees (connected nodes count for each from_node) 
    against the number of occurences of that number of degrees (density)
    
    """
    x,y = zip(*counts.items()) #x = original node number (not used in plot)
    #normalize counts
    s = np.sum(y)
    norm_y = [count/s for count in y]
    #count freq each level of connectedness occurs 
    freq = Counter(norm_y)
    #create new x, y for plot
    x,y = zip(*freq.items()) 
    #create a log/log plot of distribution
    plt.figure(figsize=(12,8))
    plt.scatter(np.log10(x),np.log10(y),marker='.')
    plt.title('In-Degree Distribution of Nodes (log/log) for %s' % name)
    plt.xlabel('Number of In-Degrees')
    plt.ylabel('Freq of In-Degrees')
    plt.show()


#Loads a citation graph and plots its in-degree distribution as a log/log plot
#Need to add a generic function to take in other digraphs    
if __name__ == '__main__':
    citation_graph = load_digraph(CITATION_URL)
    counts = compute_degrees(citation_graph)
    plot_in_degrees(counts,'Citations')
