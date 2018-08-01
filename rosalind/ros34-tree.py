#!/usr/bin/env python3
"""
Author: Ian Coleman
Purpose: Connect up a tree as per http://rosalind.info/problems/tree/
Input: from txt file --> Int N, series of tuples each on their own line
Output: Minimum number of edges needed to complete the tree described by input
"""

import pdb
from sys import argv

def get_tree_ints (file_path):
	"""
	Input: Txt file path, one int on first line, two on each subsequent
	Output: List of lists of ints, one sub-list per line of ints
	"""
	with open (file_path, 'r') as file_object:
		lines = file_object.readlines()
		lines = [i.strip() for i in lines] # strip 
		lines = [i.split(' ') for i in lines] # split
		lines = [[int(i) for i in j] for j in lines] # convert to int
		return(lines)

def edges_to_complete (tree_specs):
	"""
	Input: List of lists of ints, first is N (nodes), rest are edges
	Output: Int, minimum number of edges to complete tree
	"""
	edges = tree_specs[1:]
	nodes = tree_specs[0][0]

	# Create var to hold all connected edges, start it with first edge
	connected_edges = set(edges[0])
	min_new_edges = 0

	# Iterate through until all nodes are connected
	while len(connected_edges) != nodes:

		# find all nodes that are connected to current nodes
		temp_count = len(connected_edges) # this to inform breaking loop
		for edge in edges[1:]:
			if edge[0] in connected_edges or edge[1] in connected_edges:
				connected_edges = connected_edges | set(edge) # add in edge

		# when no more edges are currently connected  
		if len(connected_edges) == temp_count:

			# if all edges are now connected, exit
			if len(connected_edges) == nodes:
				break

			# else add a node that isn't connected, creating new edge
			for i in range(1, nodes + 1):
				if i not in connected_edges:
					min_new_edges += 1
					connected_edges = connected_edges | set([i])
					break

	print(min_new_edges)


if __name__ == "__main__":
	tree_specs = get_tree_ints(argv[1])
	edges_to_complete(tree_specs)