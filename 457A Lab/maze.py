

from maze1blackspots import blackspots
from PIL import Image

im= Image.new("RGB", (25, 25), "#FFFFFF")
pixels = im.load()


for pixel in blackspots:
    pixels[pixel] = (0,0,0)





# pixels[10,10] = ()



out = im.transpose(Image.FLIP_TOP_BOTTOM)
out.show()
# for i in range(25):
    


def breath_first(start,end,visited,queue):
    







#output

# list of steps to path
# cost of pat
# number of nodes explored