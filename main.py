from PIL import Image
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("-f", "--format", help="Format to be resized", default=(32, 32))

parser.add_argument('paths', nargs='*')

args = parser.parse_args()

arg_format = args.format[1:-1]

img_resolution = tuple(map(int, arg_format.split(', ')))

image_input_path = f"./image_input/{args.paths[0]}"
image_output_path = f"./image_output/{args.paths[1]}_{img_resolution[0]}x{img_resolution[1]}.png"

img = Image.open(image_input_path)

imgSmall = img.resize(img_resolution, resample=Image.BILINEAR)

result = imgSmall.resize(img.size, Image.NEAREST)

result.save(image_output_path)