from PIL import Image
from sys import argv

image_input_path = argv[1]
image_output_path = argv[2]

img = Image.open(image_input_path)

imgSmall = img.resize((16, 16), resample=Image.BILINEAR)

result = imgSmall.resize(img.size, Image.NEAREST)

result.save(image_output_path)