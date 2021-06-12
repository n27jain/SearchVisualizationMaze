

from maze1blackspots import blackspots
from PIL import Image, ImageDraw

def manhattanScore(p1,p2):
    x1 = p1[0]
    y1 = p1[1]
    x2 = p2[0]
    y2 = p2[1]
    return abs(x1-x2) + abs(y1-y2)

class Node:
    def __init__(self,point,goal,g):
        self.coordinate = point
        self.g = g
        self.h = manhattanScore(point,goal)
        self.cost = self.g + self.h

    
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
 
def breath_first(queue,endpoint,visited, im, imageList,parents,grid_y,grid_x):
    
    while queue:
        point = queue.pop(0)
        x = point[0]
        y = point[1]
        # print(x,y)
        #child right

        x1 = int(x) + 1
        y1 = int(y)
        newPixel = (x1,y1)
        if(newPixel == endpoint):
            parents[x1][y1] = point
            return True
        if( x1 < grid_x):
            if  (not (newPixel in visited)):
                im  = createFrame(im, newPixel, imageList)
                queue.append(newPixel)
                parents[x1][y1] = point
                visited.add(newPixel)

        #child left
        x1 = x + -1
        y1 = y 
        newPixel = (x1,y1)
        if(newPixel == endpoint):
            parents[x1][y1] = point
            return True
        if( x1 >= 0):
            if  (not (newPixel in visited)):
                im  = createFrame(im, newPixel, imageList)
                queue.append(newPixel)
                parents[x1][y1] = point
                visited.add(newPixel)
        #child up
        x1 = x 
        y1 = y + 1
        newPixel = (x1,y1)
        if(newPixel == endpoint):
            parents[x1][y1] = point
            return True
        if( y1 < grid_y):   
            if  (not (newPixel in visited)):
                im  = createFrame(im, newPixel, imageList)
                queue.append(newPixel)
                parents[x1][y1] = point
                visited.add(newPixel)
        #child down
        x1 = x 
        y1 = y - 1
        newPixel = (x1,y1)
        if(newPixel == endpoint):
            parents[x1][y1] = point
            return True
        if( y1 >= 0):
            if  (not (newPixel in visited)):
                im  = createFrame(im, newPixel, imageList)
                queue.append(newPixel)
                parents[x1][y1] = point
                visited.add(newPixel)
    return False

def depth_first(queue,endpoint,visited, im, imageList,parents,grid_y,grid_x):
    
    while queue:
        point = queue.pop(-1)
        im  = createFrame(im, point, imageList)
        x = point[0]
        y = point[1]
        # print(x,y)
        #child right

        x1 = int(x) + 1
        y1 = int(y)
        newPixel = (x1,y1)
        if(newPixel == endpoint):
            parents[x1][y1] = point
            return True
        if( x1 < grid_x):
            if  (not (newPixel in visited)):
                queue.append(newPixel)
                parents[x1][y1] = point
                visited.add(newPixel)

        #child left
        x1 = x + -1
        y1 = y 
        newPixel = (x1,y1)
        if(newPixel == endpoint):
            parents[x1][y1] = point
            return True
        if( x1 >= 0):
            if  (not (newPixel in visited)):
                queue.append(newPixel)
                parents[x1][y1] = point
                visited.add(newPixel)
        #child up
        x1 = x 
        y1 = y + 1
        newPixel = (x1,y1)
        if(newPixel == endpoint):
            parents[x1][y1] = point
            return True
        if( y1 < grid_y):   
            if  (not (newPixel in visited)):
                queue.append(newPixel)
                parents[x1][y1] = point
                visited.add(newPixel)
        #child down
        x1 = x 
        y1 = y - 1
        newPixel = (x1,y1)
        if(newPixel == endpoint):
            parents[x1][y1] = point
            return True
        if( y1 >= 0):
            if  (not (newPixel in visited)):
                # im  = createFrame(im, newPixel, imageList)
                queue.append(newPixel)
                parents[x1][y1] = point
                visited.add(newPixel)
    return False


def AStar(queue,endpoint,visited, im, imageList,parents,grid_y,grid_x):

    while queue: 

        # pop from queue that has node of least cost
        scoreMin = int('inf')
        nodeToExpand = None
        for node in queue: 
            if node.g + node.h < scoreMin:
                nodeToExpand = node
                scoreMin =  node.g + node.h
        
        # once we have the node with the least score in the queue, we must pop it and then check it's childern
        queue.pop(nodeToExpand)
        newG = nodeToExpand.g + 1 # increase actual distance score by 1 
        parentPoint = nodeToExpand.coordinate

        #child right
        childPoint = (parentPoint[0]+1, parentPoint[1])
        if(childPoint == endpoint): # if this is the goal node set the parent of the goal node to this node
            parents[childPoint[0]][childPoint[1]] = nodeToExpand.coordinate
            return True
        if(childPoint[0] < grid_x): # make sure we are not out of bounds
            # check the visted list to see if our node already exists
            foundNode  = None
            for node in visited:
                if node.coordinate == childPoint: 
                    foundNode = Node
            if(foundNode):# if the child node is in our visited list...
                #if the oldcost is more that the newcost we should update it
                childNode = Node(childPoint,endpoint,newG)
                if(foundNode.cost > childNode.cost):
                    visited.pop(foundNode)
                    visited.a
                im = createFrame(image=im,newPixel=childPoint, imageList=imageList)
                queue.append(childNode)

        #child left
        childPoint = (parentPoint[0]+1, parentPoint[1])
        #child down
        childPoint = (parentPoint[0], parentPoint[1]-1)
        #child up
        childPoint = (parentPoint[0]+1, parentPoint[1]+1)


        continue





def runTest(grid_x,grid_y,sPX,sPY,gPX,gPY, title):
    
    sP = (sPX,sPY)
    gP = (gPX,gPY)

    visited = set() # hasmap set for faster searching 
    queue = [] # a simple list that will not have many items 

    visited.add(sP)
    queue.append(sP) 

    #create 2d array of parents for each node child
    parents = []
    manScore = []
    for i in range(grid_x):
        row = []
        for j in range(grid_y):
            row.append(None)
        parents.append(row)

    
    imageList = []
    image = createImage(grid_x,grid_y,sP,gP,visited,imageList)
    
    #BFS
    #duplicate the data from above to reuse again later
    imageCopy = image.copy()
    newImageList = imageList
    newParents = parents
    newVisited = visited # hasmap set for faster searching 
    newQueue = queue # a simple list that will not have many items 


    found_sol = breath_first(newQueue,gP,newVisited, imageCopy, newImageList,newParents,grid_y,grid_x)
    tupleListPath = []
    if(found_sol):
        tupleListPath.append((gP[0],gP[1]))
        parent = parents[gP[0]][gP[1]]
        
        backup = parent
        while parent:
            backup = parent
            tupleListPath.append(backup)
            parent = parents[parent[0]][parent[1]]

        while(tupleListPath):
            print(tupleListPath.pop())

    saveGif(imageList, "BFS_"+title, grid_y,grid_x)

    #DFS TIME!

    #cleanup vars for DFS
    imageCopy = image.copy()
    newImageList = imageList
    newParents = parents
    newVisited = visited # hasmap set for faster searching 
    newQueue = queue # a simple list that will not have many items 
    
    found_sol = depth_first(newQueue,gP,newVisited, imageCopy, newImageList,newParents,grid_y,grid_x)
    tupleListPath = []
    if(found_sol):
        tupleListPath.append((gP[0],gP[1]))
        parent = parents[gP[0]][gP[1]]
        
        backup = parent
        while parent:
            backup = parent
            tupleListPath.append(backup)
            parent = parents[parent[0]][parent[1]]

        while(tupleListPath):
            print(tupleListPath.pop())

    saveGif(imageList, "DFS_"+title, grid_y,grid_x)
    

    #manhattan time!

    imageCopy = image.copy()
    newImageList = imageList
    newParents = parents

    newVisited = set() # hasmap set for faster searching 
    newQueue = [] 
    #add nodes instead of regular coordinates
    startNode = Node(sP,gP,0)

    newVisited.add(startNode)
    newQueue.append(startNode)

    found_sol = AStar(newQueue,gP,newVisited, imageCopy, newImageList,newParents,grid_y,grid_x)
    tupleListPath = []

    if(found_sol):
        tupleListPath.append((gP[0],gP[1]))
        parent = parents[gP[0]][gP[1]]
        backup = parent
        while parent:
            backup = parent
            tupleListPath.append(backup)
            parent = parents[parent[0]][parent[1]]

        while(tupleListPath):
            print(tupleListPath.pop())

    saveGif(imageList, "A*_"+title, grid_y,grid_x)



    




#requirements

#1.) BFS
    #Create a list of tuples for the optimal path found
    #Generate a gif to show the work done and the path taken at the end 
    
#1.1 Starting at S (2,11) and ending at E1 (23,19)
runTest(25,25,2,11,23,19,"02_11_23_19.gif")
#1.2 Starting at S (2,11) and ending at E2 (2,21)
runTest(25,25,2,11,2,21,"02_11_02_21.gif")
#1.3 (0,0) - (24,24)
runTest(25,25,0,0,24,24,"00_00_24_24.gif")
