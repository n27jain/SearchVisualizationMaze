
from maze1blackspots import blackspots
from PIL import Image, ImageDraw
import sys
class Node:
    def __init__(self,point,goal):
        self.cor = point
        self.g = 0
        #manhattanScore
        x1 = self.cor[0]
        y1 = self.cor[1]
        x2 = goal[0]
        y2 = goal[1]
        self.h = abs(x1-x2) + abs(y1-y2)
        self.cost = 0
        self.parent = None
        
def createImage(x,y,start,goal,visited,imageList):
    im = Image.new("RGB", (x, y), "#FFFFFF")
    pixels = im.load()

    pixels[start] = (255,0,255)
    pixels[goal] = (0,255,0)

    for pixel in blackspots: # add blackspots to the image and to the visited nodes
        pixels[pixel] = (0,0,0)
        visited.add(pixel)
        imageList.append(im)
    return im

def createFrame(image, newPixel, imageList):
    newImage = image.copy()
    pixels = newImage.load()
    pixels[newPixel] = (255,0,0)
    imageList.append(newImage)
    return newImage

def saveImage(image):
    out = image.transpose(Image.FLIP_TOP_BOTTOM)
    out.show()

def saveGif(imageList, name, grid_y,grid_x):

    # image = imageList[0].transpose(Image.FLIP_TOP_BOTTOM)
    # image.show()
    for i in range(len(imageList)):
        imageList[i] = imageList[i].transpose(Image.FLIP_TOP_BOTTOM)
        # out = image.resize((grid_y*5,grid_x*5))
    imageList[0].save(name, format='GIF',
               append_images=imageList[1:], save_all=True, duration=10, loop=0)

def createFrame(image, newPixel, imageList):
    newImage = image.copy()
    pixels = newImage.load()
    pixels[newPixel] = (255,0,0)
    imageList.append(newImage)
    return newImage
 
 #manhattan time!

def saveGif(imageList, name, grid_y,grid_x):
    
    # image = imageList[0].transpose(Image.FLIP_TOP_BOTTOM)
    # image.show()
    for i in range(len(imageList)):
        imageList[i] = imageList[i].transpose(Image.FLIP_TOP_BOTTOM)
        # out = image.resize((grid_y*5,grid_x*5))
    imageList[0].save(name, format='GIF',
               append_images=imageList[1:], save_all=True, duration=10, loop=0)


def investigate(childPoint,parentPoint,gP,open,closed,nodes,newG):
# if goal is reached
    if(childPoint == gP ):
        nodes[childPoint[0]][childPoint[1]].parent = parentPoint
        return True
    # make sure the node is not in the closed list
    if(not (childPoint in closed)):
        #if it exists in the open list then we need to compare current with old
        if(childPoint in open):
            # and if it does, then compare current score with old score
            childNode = nodes[childPoint[0]][childPoint[1]]
            if(childNode.g > newG):
                newNode = Node(childPoint,gP)
                newNode.g = newG
                newNode.cost = newNode.g + newNode.h
                newNode.parent = parentPoint
                nodes[childPoint[0]][childPoint[1]] = newNode
            # leave it in the open pile no need to add it back
        else: #otherwise we need to add it to the open list as well
            newNode = Node(childPoint,gP)
            newNode.g = newG
            newNode.cost = newNode.g + newNode.h
            newNode.parent = parentPoint
            nodes[childPoint[0]][childPoint[1]] = newNode
            open.add(childPoint)
    return False

def AStar(open,closed,nodes,gP,grid_y,grid_x,image,imageList):
    while open: # while we have nodes to check out
        # print(open)
        #find node of least current cost
        scoreMin = sys.maxsize
        nodeToExpand = Node
        for cor in open: 
            node = nodes[cor[0]][cor[1]]
            if(node.cost < scoreMin):
                nodeToExpand = node
                scoreMin = node.cost
        image = createFrame(image, nodeToExpand.cor, imageList)
        #pop this node from open to closed
        closed.add(nodeToExpand.cor)
    
        open.remove(nodeToExpand.cor)
        newG = nodeToExpand.g + 1
        parentPoint = nodeToExpand.cor

        if(parentPoint == (24,23)): shouldWork = True

        #check all of the childern and add them to open list if they are not in closed list
        #child right
        childPoint = (parentPoint[0]+1, parentPoint[1])
        if(childPoint[0] < grid_x): # make sure we are not out of bounds
            if (investigate(childPoint,parentPoint,gP,open,closed,nodes,newG) ):
                return True

        #child left
        childPoint = (parentPoint[0]-1, parentPoint[1])
        if(childPoint[0] >= 0): # make sure we are not out of bounds
            if (investigate(childPoint,parentPoint,gP,open,closed,nodes,newG) ):
                return True
        #child up
        childPoint = (parentPoint[0], parentPoint[1]+1)
        if(childPoint[1] < grid_y): # make sure we are not out of bounds
            if (investigate(childPoint,parentPoint,gP,open,closed,nodes,newG) ):
                return True   
        #child down
        childPoint = (parentPoint[0], parentPoint[1]-1)
        if(childPoint[1] >= 0): # make sure we are not out of bounds
             if (investigate(childPoint,parentPoint,gP,open,closed,nodes,newG) ):
                    return True



    
def runTest(grid_x,grid_y,sPX,sPY,gPX,gPY, title):

    sP = (sPX,sPY)
    gP = (gPX,gPY)

    open = set() # this is the list if nodes that are open
    closed = set() # these are the closed nodes
    nodes = []

    imageList = []
    image = createImage(grid_x,grid_y,sP,gP,closed,imageList)
    
    for i in range(grid_x):
        row = []
        for j in range(grid_y):
            newNode = Node((i,j),gP)
            row.append(newNode)
        nodes.append(row)

    nodes[sPX][sPY].cost = nodes[sPX][sPY].g + nodes[sPX][sPY].h
    open.add(sP)
    found_sol = AStar(open,closed,nodes,gP,grid_y,grid_x,image,imageList)
    print("here")
    saveGif(imageList, "Astar_.gif", grid_y,grid_x)
    tupleListPath = []

    if(found_sol):
        tupleListPath.append((gP[0],gP[1]))
        parent = nodes[gP[0]][gP[1]].parent
        backup = parent
        while parent:
            backup = parent
            tupleListPath.append(backup)
            parent = nodes[backup[0]][backup[1]].parent
        print("Here")
        while(tupleListPath):
            print(tupleListPath.pop())
    else:
        print("failed")

    # saveGif(imageList, "A*_"+title, grid_y,grid_x)

runTest(25,25,0,0,24,24,"02_11_23_19.gif")