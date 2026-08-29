import argparse
from PIL import Image
import numpy as np
import sys
import os

def convert_png_to_ico(input_path, output_path, make_transparent=True):
    try:
        img = Image.open(input_path).convert("RGBA")
    except Exception as e:
        print(f"Error loading image: {e}")
        sys.exit(1)
    
    if make_transparent:
        data = np.array(img)
        # Replace near-white and light-grey background pixels with full transparency
        r, g, b, a = data.T
        white_areas = (r > 200) & (g > 200) & (b > 200)
        data[..., 3][white_areas.T] = 0
        img = Image.fromarray(data)

    img.save(output_path, format="ICO", sizes=[(256, 256), (128, 128), (64, 64), (48, 48), (32, 32), (16, 16)])
    print(f"Successfully converted {input_path} to {output_path}")

def main():
    parser = argparse.ArgumentParser(description="Convert PNG/JPG to ICO with optional background transparency.")
    parser.add_argument("input", help="Path to the input image")
    parser.add_argument("-o", "--output", help="Path to the output ICO image (default: same directory as input)", default=None)
    parser.add_argument("--no-transparent", action="store_true", help="Do not make white background transparent")
    args = parser.parse_args()
    
    if args.output is None:
        input_dir = os.path.dirname(os.path.abspath(args.input))
        input_filename = os.path.splitext(os.path.basename(args.input))[0]
        args.output = os.path.join(input_dir, f"{input_filename}.ico")
        
    convert_png_to_ico(args.input, args.output, make_transparent=not args.no_transparent)

if __name__ == "__main__":
    main()