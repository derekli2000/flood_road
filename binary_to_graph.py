import cv2
import numpy as np
from PIL import Image
import pprint
from pathfinding.finder.bi_a_star import BiAStarFinder as AFinder
# from pathfinding.finder.dijkstra import DijkstraFinder as AFinder
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid

def img2graph(img, img2, a, b):
    # FLOODED
    im1 = Image.open(img)
    im1 = im1.convert('L')
    im1 = im1.resize( (256,256) )

    # PRE
    im2 = Image.open(img2)
    im2 = im2.convert('L')
    im2 = im2.resize( (256,256) )
  
    matrix1 = np.array(im1)
    matrix2 = np.array(im2)
    

    graph = np.zeros(matrix1.shape, dtype=np.uint8)
    graph[matrix2 > 0] = 255
    graph[matrix1 > 0] = 1
    



    grid = Grid(matrix=graph)
    start = grid.node( a[0]//2, a[1]//2)
    end = grid.node( b[0]//2, b[1]//2)
    finder = AFinder(diagonal_movement=DiagonalMovement.always)

    path, runs = finder.find_path(start, end, grid)
    print('operations:', runs, 'path length:', len(path))
    out = np.zeros(matrix1.shape,dtype=np.uint8)
    for i in path:
        y = i[0]
        x = i[1]
        out[(x,y)] = 255
    

    # cv2.imwrite("out.jpg", out)

    out2 = np.zeros((*matrix1.shape,3), dtype=np.uint8)
    
    out2[matrix2 > 0] = (0, 50, 255) 
    out2[matrix1 > 0] = (100,100,100)
    out2[out >= 1] = (0, 255, 0)

    cv2.imwrite("out.jpg", out2)

# img2graph('tile1.jpg', (78,36), (94,161))


background_background = '/Users/derekli/Desktop/flood_road/74604684_622466278290362_5068941602697773056_n (1).png'
path = '/Users/derekli/Desktop/flood_road/74604684_622466278290362_5068941602697773056_n.png'
img2graph(path, background_background, (248,82), (2,488))