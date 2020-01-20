# Minesweeper
Minesweeper is a popular game on Windows. You can try playing the game under: http://minesweeperonline.com/. 
The target of the game is to guess where the mines are located within a board. The game is played as follows:
The player is given a square board of tiles (N x N). All tiles are hidden and their values are not shown. 
A tile can contain one of the following values: a mine, blank, or a number that indicates how many mines are in the neighborhood 
(8 neighbors) of the tile.

The player then is given the chance to choose a tile (row and column position). Depending
on what is under that chosen tile, three outcomes exists:
- there is a mine, the game is lost
- it is a tile number, so that tile is uncovered (showing the number to the player) - the game continues
- it is a blank tile, then all adjacent tiles that are blank or the ones that have numbers are revealed 
  (all blank tiles in the neighborhood are uncovered until a boundary is reached or a number is reached along the path) 
   Then the game continues.
The game is won only when all tiles (except the ones with the mines) are uncovered.
