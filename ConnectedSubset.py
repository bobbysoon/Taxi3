#!/usr/bin/python

from random import choice as Choice

def ConnectedSubset(taxi):
	cells= {c for c in taxi.centroids if c.isClosed}
	goal= len(cells)/2
	while len(cells)>goal:
		choice= Choice(list(cells))
		_cells_= cells-{choice}

		testing= {_cells_.pop()}
		tested=set()
		while testing:
			cell=testing.pop()
			na= (cell.neighbors - tested) & _cells_
			testing |= na
			_cells_ -= na
			tested |= na

		if not _cells_:
			cells.remove(choice)
	return cells

