```
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
```
