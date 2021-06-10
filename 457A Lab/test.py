
from PIL import Image, ImageDraw

from maze1blackspots import blackspots



def create_image_with_text(wh, text):
    width, height = wh
    img = Image.new('RGB', (300, 200), "yellow")
    draw = ImageDraw.Draw(img)
    draw.text((width, height), text,  fill="black")
    return img
# Create the frames

def createFrame(image, pixel):
    
    newImage = image.copy()
    pixels = newImage.load()
    pixels[pixel] = (255,0,0)
    return newImage


def createImage(x,y,start,goal):
    im = Image.new("RGB", (x, y), "#FFFFFF")
    pixels = im.load()

    pixels[start] = (255,0,0)
    pixels[goal] = (0,255,0)

    for pixel in blackspots: # add blackspots to the image and to the visited nodes
        pixels[pixel] = (0,0,0)
        # visited.add(pixel)
    return im


# frames = []
# x, y = 0, 0
# for i in range(100):
#     new_frame = create_image_with_text((x-100,y), "HELLO")
#     frames.append(new_frame)
#     x += 4
#     y += 1
 
# # Save into a GIF file that loops forever
# frames[0].save('moving_text.gif', format='GIF',
#                append_images=frames[1:], save_all=True, duration=30, loop=0)


frames = []
image  = createImage(25,25,(0,0), (2,11))
print("YOLO")
print(image)
frames.append(image)
image = createFrame(image,(0,1))
print("Trying")
print(image)
frames.append(image)
image = createFrame(image,(0,2))
frames.append(image)
image = createFrame(image,(0,3))
frames.append(image)
image = createFrame(image,(0,4))
frames.append(image)

frames[0].save('moving_text.gif', format='GIF',
               append_images=frames[1:], save_all=True, duration=100, loop=0)
