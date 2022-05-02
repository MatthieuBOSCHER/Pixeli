from PIL import Image
import argparse


# Create parser and create arguments
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--format", help="Format to be resized", default="(32, 32)")
parser.add_argument('paths', nargs='*')

# Parse argumuments
args = parser.parse_args()
arg_format = args.format[1:-1]

# Define input and output path
img_resolution = tuple(map(int, arg_format.split(',')))
image_input_path = f"./image_input/{args.paths[0]}"


# Set output file format if defined as png of jpg
try:
    img_output_format = "."+args.paths[1].split(".")[1]
except IndexError:
    img_output_format = None

img_output_filename = args.paths[1].split(".")[0]

if img_output_format:
    image_output_path = f"./image_output/{img_output_filename}_{img_resolution[0]}x{img_resolution[1]}{img_output_format}"
else:
    image_output_path = f"./image_output/{img_output_filename}_{img_resolution[0]}x{img_resolution[1]}.png"

# open input img, resize and save
img = Image.open(image_input_path)
imgSmall = img.resize(img_resolution, resample=Image.BILINEAR)
result = imgSmall.resize(img.size, Image.NEAREST)
result.save(image_output_path)
