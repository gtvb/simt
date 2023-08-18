import argparse
from PIL import Image, ImageFilter

available_filters = {
        "BLUR": ImageFilter.BLUR,
        "CONTOUR": ImageFilter.CONTOUR,
        "DETAIL": ImageFilter.DETAIL,
        "EDGE_ENHANCE": ImageFilter.EDGE_ENHANCE,
        "EDGE_ENHANCE_MORE": ImageFilter.EDGE_ENHANCE_MORE,
        "EMBOSS": ImageFilter.EMBOSS,
        "FIND_EDGES": ImageFilter.FIND_EDGES,
        "SHARPEN": ImageFilter.SHARPEN,
        "SMOOTH": ImageFilter.SMOOTH,
        "SMOOTH_MORE": ImageFilter.SMOOTH_MORE
    }

def resize_command(args):
    width, height = map(int, args.size.split("x"))
    print(f"Resizing {args.infile} to width: {width}, height: {height}")
    try:
        with Image.open(args.infile) as img:
            out = img.resize((width, height))
            out.save(args.outfile)
    except OSError:
        print("Could not open image specified in path")
        exit(1)

def change_format_command(args):
    print(f"Changing {args.infile} to format {args.format}")
    out = f"{args.outfile}.{args.format}"
    try:
        with Image.open(args.infile) as img:
            img.save(out)
    except OSError:
        print("Could not open image specified in path")
        exit(1)


def filter_command(args):
    print(f"Filter image using {args.filter}")
    try:
        with Image.open(args.infile) as img:
            out = img.filter(available_filters[args.filter])
            out.save(args.outfile)
    except OSError:
        print("Could not open image specified in path")
        exit(1)

def crop_command(args):
    x0, y0, x1, y1 = map(int, args.coords.split(","))
    print(f"Cropping box with coords ({x0}, {y0}) ({x1}, {y1})")
    try:
        with Image.open(args.infile) as img:
            out = img.crop((x0, y0, x1, x1))
            out.save(args.outfile)
    except OSError:
        print("Could not open image specified in path")
        exit(1)

def main(): 
    parser = argparse.ArgumentParser(prog="sitm", description="A simple tool to execute fast image manipulations")
    
    subparsers = parser.add_subparsers(required=True)
    
    # Subparser for the 'resize' command
    resize_parser = subparsers.add_parser("resize", help="Resize an image")
    resize_parser.add_argument("infile", type=str, help="The path of the image to resize")
    resize_parser.add_argument("outfile", type=str, help="Where to save the new image")
    resize_parser.add_argument("size", type=str, help="Size in the format <width>x<height>")
    resize_parser.set_defaults(func=resize_command)

    # Subparser for the 'change-format'
    change_format_parser = subparsers.add_parser("change-format", help="Change the format of an image")
    change_format_parser.add_argument("infile", type=str, help="The path of the image to change format")
    change_format_parser.add_argument("outfile", type=str, help="Where to save the new image")
    change_format_parser.add_argument("format", type=str, help="The new format to convert to")
    change_format_parser.set_defaults(func=change_format_command)

    # Subparser for the 'filter'
    filter_parser = subparsers.add_parser("filter", help="Apply a filter to an image")
    filter_parser.add_argument("infile", type=str, help="The path of the image to filter")
    filter_parser.add_argument("outfile", type=str, help="Where to save the new image")
    filter_parser.add_argument("filter", type=str, help="The new filter to apply", choices=available_filters.keys())
    filter_parser.set_defaults(func=filter_command)

    # Subparser for the 'crop'
    crop_parser = subparsers.add_parser("crop", help="Crop an image")
    crop_parser.add_argument("infile", type=str, help="The path of the image to crop")
    crop_parser.add_argument("outfile", type=str, help="Where to save the new image")
    crop_parser.add_argument("coords", type=str, help="Size in the format <x0>,<y0>,<x1>,<y1>")
    crop_parser.set_defaults(func=crop_command)
    
    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main() 
