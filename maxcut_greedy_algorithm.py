# --------------------------------------------------
'''Brute force algorithm tries all binary combinations for n nodes -> O(2^n)'''
# --------------------------------------------------
procedure brute_maxcut(G):
	Input: Graph G = (V, E) in an adjacency list
	Output: Binary array of the coloring of nodes
	
	coloring = [0] * Length(V) (list of size V, all values start at 0 == ‘white’)
	current_cut = 0
	max_coloring = [0] * Length(V) (only stores that coloring with the highest result)
	max_cut = 0
	
	while (sum(coloring)) < length(V):
		coloring = Increment the rightmost element of the array by 1. (If the number is already 1, then you carry, similar to binary addition.) 
		changed = index of changed value
	
		Evaluate the state by checking the edges of the node that was just colored.
		current_cut += evaluate_state(coloring, changed)
		If (current_cut > max_cut):
			max_cut = current_cut
			max_coloring = coloring
	
procedure evaluate_state(G, coloring, changed):
	Input: coloring: Graph G, current binary list, changed: index of changed node
	Output: The # of edges being added by the cut, i.e. the # of edges between the sets.
	
	edge_count = 0
	for edge in range(len(G[changed])): (coloring is indexed the same)
		check to see if the edges contain alternating colors
		if (coloring[changed] != coloring[edge]):
			edge_count += 1
	
	return edge_count


# --------------------------------------------------
''' initialize 2^(n / 4) random lists, then evaluate each one. The best one is output'''
# --------------------------------------------------
procedure randomized_cut(G):
	Input: Graph G = (V, E) in adjacency list
	Output: list of colorings as binary; max_cut: number of edges between sets
	
	current_cut = 0
	max_coloring = [0] * Length(V) # (only stores that coloring with the highest result)
	max_cut = 0
	
	random_lists = 2^(n / 4) # random lists to evaluate
	
	for list in random_lists:
		current_cut = evaluate(random_lists)
		if (current_cut > max_cut):
			max_cut = current_cut
			max_coloring = list
	
	return max_colorings, max_cut

procedure evaluate(G, coloring):
	Input: Graph G, coloring: binary list of node colorings, 1 = “black”, 0 = “white”
	Output: # of edges between the sets given a binary list
	
	cut_count = 0
	
	for node in range(len(coloring)):
		for edge in range(len(G[node])):
			node color != other node color:
				cut_count += 1
	
	return cut_count


# --------------------------------------------------
''' Greedy Algorithm using a priority queue'''
# --------------------------------------------------
procedure greedy_one(G):
	Input: graph G
	Output: list of colorings as binary, # of edges between sets
	
	coloring = [0] * Length(V) (list of size V, all values start at 0 == ‘white’)
	current_cut = 0
	max_cut = 0
	max_coloring = [0] * Length(V) # (only stores that coloring with the highest result)
	priority = [] # (list ordered by vertices of highest to lowest degree)
	
	for node in priority:
		change node from 0 to 1 in max_coloring
	  changed = index of changed value
	
		# Evaluate the state by checking the edges of the node that was just colored.
		current_cut += evaluate_state(coloring, changed)
		If (current_cut > max_cut):
			max_cut = current_cut
			max_coloring = coloring 
	
		If the node was a bad choice undo the flip

procedure evaluate_state(G, coloring, changed):
	Input: coloring: Graph G, current binary list, changed: index of changed node
	Output: The # of edges being added by the cut, i.e. the # of edges between the sets.
	
	edge_count = 0
	for edge in range(len(G[changed])): (coloring is indexed the same)
		check to see if the edges contain alternating colors
		if (coloring[changed] != coloring[edge]):
			edge_count += 1
	
	return edge_count
