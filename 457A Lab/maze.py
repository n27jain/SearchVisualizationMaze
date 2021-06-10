

from maze1blackspots import blackspots
from PIL import Image, ImageDraw

    
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

def saveGif(imageList, name):
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



def AStar(queue,endpoint,visited, im, imageList,parents,grid_y,grid_x):
    pass





def runTest(grid_x,grid_y,sPX,sPY,gPX,gPY, title):
    
    sP = (sPX,sPY)
    gP = (gPX,gPY)

    visited = set() # hasmap set for faster searching 
    queue = [] # a simple list that will not have many items 

    visited.add(sP)
    queue.append(sP) 

    #create 2d array of parents for each node child
    parents = []
    for i in range(grid_x):
        row = []
        for j in range(grid_y):
            row.append(None)
        parents.append(row)

    imageList = []
    image = createImage(grid_x,grid_y,sP,gP,visited,imageList)
    tupleListPath = []
    found_sol = breath_first(queue,gP,visited, image, imageList,parents,grid_y,grid_x)
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

    saveGif(imageList, "BFS_"+title)

    #DFS TIME!
    
    #cleanup vars for DFS
    visited = set() # hasmap set for faster searching 
    queue = [] # a simple list that will not have many items 

    visited.add(sP)
    queue.append(sP) 

    #create 2d array of parents for each node child
    parents = []
    for i in range(grid_x):
        row = []
        for j in range(grid_y):
            row.append(None)
        parents.append(row)

    imageList = []
    image = createImage(grid_x,grid_y,sP,gP,visited,imageList)
    tupleListPath = []
    found_sol = depth_first(queue,gP,visited, image, imageList,parents,grid_y,grid_x)

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

    saveGif(imageList, "DFS_"+title)
    

    #manhattan time!

    manScore = []




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
