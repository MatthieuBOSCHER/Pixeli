from PIL import Image
import argparse


def main():
    args = get_arguments()

    img_resolution = get_resolution_as_tuple(args.format[1:-1])
    img_file_format = get_output_file_format(args.paths[1])

    img_input_filename = get_input_filename(args.paths[0])
    img_output_filename = get_output_filename(args.paths[1].split(".")[0], img_file_format, img_resolution)

    resize_image(img_input_filename, img_output_filename, img_resolution)


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--format", help="Format to be resized", default="(32, 32)")
    parser.add_argument('paths', nargs='*')
    args = parser.parse_args()
    return args


def get_resolution_as_tuple(arg_format):
    img_resolution = tuple(map(int, arg_format.split(',')))
    return img_resolution


def get_output_file_format(arg_output_path):
    try:
        img_file_format = "."+arg_output_path.split(".")[1]
    except IndexError:
        img_file_format = None
    return img_file_format


def get_input_filename(arg_input_path):
    img_input_filename = f"./image_input/{arg_input_path}"
    return img_input_filename


def get_output_filename(img_output_filename, img_output_format, img_resolution):
    if img_output_format:
        return f"./image_output/{img_output_filename}_{img_resolution[0]}x{img_resolution[1]}{img_output_format}"
    return f"./image_output/{img_output_filename}_{img_resolution[0]}x{img_resolution[1]}.png"


def resize_image(image_input_filename, img_output_filename, img_resolution):
    img = Image.open(image_input_filename)
    img_small = img.resize(img_resolution, resample=Image.BILINEAR)
    result = img_small.resize(img.size, Image.NEAREST)
    result.save(img_output_filename)


if __name__ == "__main__":
    main()
