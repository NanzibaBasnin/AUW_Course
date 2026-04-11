import sys 
from PIL import Image

images = []

print(sys.argv[0])

for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)

images[0].save(
    "costumes.gif", save_all = True, append_images = [images[1]], duration = 200, loop = 0
)
