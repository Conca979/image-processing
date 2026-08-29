import argparse
from PIL import Image
import numpy as np
import sys
import os

def convert_image(input_path, output_path, make_transparent=True):
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

    # Determine output format from extension
    output_ext = output_path.split('.')[-1].lower()

    if output_ext in ['jpg', 'jpeg']:
        # JPEG doesn't support alpha channel.
        # If the image has an alpha channel, paste it onto a white background.
        if img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info):
            background = Image.new("RGB", img.size, (255, 255, 255))
            # Some modes might not split properly, so ensure it's RGBA before splitting
            img_rgba = img.convert("RGBA")
            background.paste(img_rgba, mask=img_rgba.split()[3]) # alpha channel is the mask
            img = background
        else:
            img = img.convert("RGB")

    # If it's an ICO we specify sizes, otherwise let Pillow handle it based on format
    if output_ext == 'ico':
        img.save(output_path, format="ICO", sizes=[(256, 256), (128, 128), (64, 64), (48, 48), (32, 32), (16, 16)])
    else:
        img.save(output_path)
    print(f"Successfully converted {input_path} to {output_path}")

def main():
    parser = argparse.ArgumentParser(description="Convert images between formats with optional background transparency.")
    parser.add_argument("input", help="Path to the input image")
    parser.add_argument("-o", "--output", help="Path to the output image", required=True)
    parser.add_argument("--no-transparent", action="store_true", help="Do not make white background transparent")
    args = parser.parse_args()
    
    convert_image(args.input, args.output, make_transparent=not args.no_transparent)

if __name__ == "__main__":
    main()